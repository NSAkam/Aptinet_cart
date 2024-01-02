import json
import os
import sys
import time
from time import sleep
from threading import Thread
from email_validator import validate_email, EmailNotValidError
from datetime import datetime
import uuid

from PySide2.QtCore import QObject, Signal, Property, Slot

from Models.product import Product
from Models.Helpers.productModel import ProductModel
from Models.user import User
from Models.serverUser import ServerUser

from Services.dal import DAL
from Services.sound import *
from Services.gpio import GreenLight
from Services.weightsensor import WeightSensorWorker
from Services.nfc import nfc
from Services.lang import languageReader
from Services.logStash import LogStash
from Services.restapi import restAPI
from Services.wifi import WirelessModel


from Helpers.scannerHelper import ScannerHelper
# from Helpers.weightSensorHelper import WeightSensorHelper

from Repositories.userRepository import UserRepository
from Repositories.userServerRepository import UserServerRepository
from Repositories.productRepository import ProductRepository
from Repositories.factoreRepository import UserFactoreRepository
from Repositories.adminRepository import AdminRepository


class ShopPage(QObject):
    ####################################################################################################### Settings ###
    _insertProductTime: int = 8  # actual time = n -1
    _timerOffset: int = 3
    # Accept inserted product without checking weight under this limit
    _validInsertedWeightForCalTol: int = 5
    _basketWeightLimit: int = 45000  # grams
    _lightestProductWeight: int = 11  # grams
    _lightestWeightForHeavyProduct: int = 25  # grams
    _lightestWeightForLightWeightProduct: int = 8
    _basketWeightTolerance: int = 20  # better fit: 25
    _pluCodeLength: int = 4
    _mailServiceURL = "https://app.aptinet.com/api/APP/sendMail"
    _saveFactorURL = "https://app.aptinet.com/api/APP/saveFactor"

    ######################################################################################################### Models ###
    _factorList: ProductModel
    _offersList: ProductModel
    _offerTopTen: ProductModel
    _suggestedList: ProductModel
    _pluList: ProductModel
    _pluTopFour: ProductModel
    _bypassList: ProductModel
    _removeList: ProductModel
    _removeLookupList: ProductModel
    _wifimodel: WirelessModel


    ################################################################################################### Repositories ###
    _userRepository: UserRepository
    _userServerRepository: UserServerRepository
    _productRepository: ProductRepository
    _factorRepository: UserFactoreRepository
    _adminRepository: AdminRepository
    ######################################################################################################## Objects ###
    _user: User
    _loggedInUser: ServerUser
    _newProduct: Product
    _lang: languageReader
    _logger: LogStash
    _restAPI: restAPI

    ######################################################################################################## Private ###
    _state: int = 1
    _countDownTimer: int = -60
    _startWeight: int = 0
    _basketWeightShouldBe: int = 0
    _basketWeightRemoveProcess: int = 0
    _basketLoad: int = 0
    _stackViewDepth: int
    _pluStartWeight: int = 0

    _basketIsFull: bool = False
    _inByPass: bool = False
    _loginFinished: bool = False
    _startProcess: bool = False
    _manualBarcodeEntered: bool = False
    _canRemoveProductClick: bool = False
    _trustUser: bool = False
    _shouldBarcodeToBeScannToAddProduct: bool = True
    _lightWeightProductExistInBasket: bool = False
    _inOfferList: bool = False
    _canCreatePLUCheckThread: bool = True
    _requestForSendingEmail: bool = False
    _rated: bool = False

    _enteredEmail: str = ""
    _emailException: str = ""
    _couponCode: str = ""

    ######################################################################################################## Modules ###
    _weightSensor: WeightSensorWorker
    _nfc: nfc

    def __init__(self, dal: DAL, user: User, scanner: ScannerHelper, language: languageReader):
        super().__init__()

        #### Private ##############################################
        self._dal = dal
        self._lang = language
        self._user = user
        self._logger = LogStash(self._dal)
        self._restAPI = restAPI()
        self._restAPI.recived.connect(self.data_recivedFromServer)

        #### Repositories #########################################
        self._userRepository = UserRepository(self._dal)
        self._userServerRepository = UserServerRepository(self._dal)
        self._productRepository = ProductRepository(self._dal)
        self._factorRepository = UserFactoreRepository(self._dal)
        self._adminRepository = AdminRepository(self._dal)
        #### Barcode Scanner ######################################
        self._scanner = scanner
        self._scanner.EAN13ReadSignal.connect(self.barcodeRead)
        self._scanner.IDBarcodeReadSignal.connect(self.IDBarcode_read)
        self._scanner.couponReadSignal.connect(self.apply_couponCode)

        #### WeightSensor #########################################
        self._weightSensor = WeightSensorWorker()
        self._weightSensor.basketweight_changed.connect(
            self.basketWeightChanged)
        self._weightSensor.startWeightchanged.connect(self.read_startWeight)
        self._weightSensor.start()

        #### Models ###############################################
        self._newProduct = Product()
        self._factorList = ProductModel()
        self._offersList = ProductModel()
        self._offersList.initialize_productList(
            self._productRepository.get_offerProducts())
        self._offerTopTen = ProductModel()
        self._offerTopTen.initialize_productList(
            self._productRepository.get_topOfferProducts())
        self._suggestedList = ProductModel()
        self._pluList = ProductModel()
        self._pluTopFour = ProductModel()
        plus = self._productRepository.get_pluProducts()
        self._pluList.initialize_productList(plus)
        if len(plus) > 4:
            self._pluTopFour.initialize_productList(plus[:4])
        else:
            self._pluTopFour.initialize_productList(plus)

        self._bypassList = ProductModel()
        self._removeList = ProductModel()
        self._removeLookupList = ProductModel()

        #### Insert Timer Thread ##################################
        self._canTimerTick = True
        self._timerThread = Thread(target=self.timerSlot)
        self._timerThread.start()

        # end of __init__

    ######################################################################################################## Signals ###
    changedSignal = Signal()

    tempSignal = Signal()

    #### Stack view Signals #######################################
    clearStackViewSignal = Signal()  # clear stack view
    # close top stack view. maybe used for several purpose like close new product scanned stack view
    closeTopStackViewSignal = Signal()
    hideTopBtnSignal = Signal()  # hide manual barcode btn and PLU btn

    showFactorListSignal = Signal()  # show factor list
    # show new product scanned and suggestion list
    showNewProductScannedSignal = Signal()
    showAllOfferListSignal = Signal()  # show all offer list
    showManualBarcodeSignal = Signal()  # show manual barcode view
    showAddPLUItemsSignal = Signal()  # shoe first PLU view
    showWeightedPLUItemsSignal = Signal()  # show weighted PLU view
    showCountedPLUItemsSignal = Signal()  # show counted PLU view
    showTopBtnSignal = Signal()  # show manual barcode btn and PLU btn
    showCheckOutSignal = Signal()  # show check out view
    showPaymentSignal = Signal(int)   # 0 for NFC payment, 1 for Qr payment
    showPaymentPinSignal = Signal()
    showAfterPaymentSignal = Signal()

    basketLoadChangedSignal = Signal(int)

    #### Popup Signals ############################################
    closeAllPopUpSignal = Signal()

    openPopupMessageTimerSignal = Signal(str)
    closePopUpMessageTimer = Signal()

    openPopupMessageSignal = Signal(str)
    closePopupMessageSignal = Signal()

    # pop up weight not match with scanned barcode
    openPopupWeightNotMatchWithBarcodeSignal = Signal()
    closePopupWeightNotMatchWithBarcodeSignal = Signal()

    # add product to basket without scanning barcode
    openPopupNoBarcodeScannedSignal = Signal()
    closePopupNoBarcodeScannedSignal = Signal()

    openPopupDeleteProductSignal = Signal()  # remove product from basket
    closePopupDeleteProductSignal = Signal()

    # change weight at the end of shopping
    openPopUpMessageNotAllowedChangeWeightSignal = Signal()
    closePopUpMessageNotAllowedChangeWeightSignal = Signal()

    openPopupByPassSignal = Signal()  # open by pass pop up
    closePopupByPassSignal = Signal()

    ##################################################################################################### Properties ###
    def getwifiModel(self):
        return self._wifimodel

    wifimodel = Property(QObject, getwifiModel, constant=True)
    
    def get_state(self):
        return self._state

    def set_state(self, state: int):
        self._state = state
        print("state: " + str(state))
        if state == 1:
            self.closeAllPopUpSignal.emit()
            self.turn_offGreenlight()

        else:
            if state != 2:
                self.countDownTimer = -20

    state = Property(int, get_state, set_state, notify=changedSignal)

    def get_newProduct(self):
        return self._newProduct

    def set_newProduct(self, val: Product):
        self._newProduct = val
        self.changedSignal.emit()

    newProduct = Property(Product, get_newProduct,
                          set_newProduct, notify=changedSignal)

    def get_factorList(self):
        return self._factorList

    factorList = Property(QObject, get_factorList, constant=True)

    def get_offersList(self):
        return self._offersList

    offersList = Property(QObject, get_offersList, constant=True)

    def get_offerTopTen(self):
        return self._offerTopTen

    offerTopTen = Property(QObject, get_offerTopTen, constant=True)

    def get_suggestedList(self):
        return self._suggestedList

    suggestedList = Property(QObject, get_suggestedList, constant=True)

    def get_pluList(self):
        return self._pluList

    pluList = Property(QObject, get_pluList, constant=True)

    def get_pluTopFour(self):
        return self._pluTopFour

    pluTopFour = Property(QObject, get_pluTopFour, constant=True)

    def get_bypassList(self):
        return self._bypassList

    bypassList = Property(QObject, get_bypassList, constant=True)

    def get_removeList(self):
        return self._removeList

    removeList = Property(QObject, get_removeList, constant=True)

    def get_removeLookupList(self):
        return self._removeLookupList

    removeLookupList = Property(QObject, get_removeLookupList, constant=True)

    def get_countDownTimer(self):
        return self._countDownTimer

    def set_countDownTimer(self, v: int):
        self._countDownTimer = v
        self.changedSignal.emit()

    countDownTimer = Property(int, get_countDownTimer,
                              set_countDownTimer, notify=changedSignal)

    def get_basketIsFull(self):
        return self._basketIsFull

    def set_basketIsFull(self, v: bool):
        self._basketIsFull = v
        self.changedSignal.emit()

    basketIsFull = Property(bool, get_basketIsFull,
                            set_basketIsFull, notify=changedSignal)

    def get_basketLoad(self):
        return self._basketLoad

    def set_basketLoad(self, v: int):
        self._basketLoad = v
        self.basketLoadChangedSignal.emit(self._basketLoad)
        self.changedSignal.emit()

    basketLoad = Property(int, get_basketLoad,
                          set_basketLoad, notify=changedSignal)

    def get_user(self):
        return self._user

    def set_user(self, user: User):
        self._user = user
        self.changedSignal.emit()

    user = Property(User, get_user, set_user, notify=changedSignal)

    ########################################################################################################## Sluts ###
    @Slot()
    def barcodeRead(self):
        self.closePopUpMessageTimer.emit()
        if not self._inByPass:
            self._logger.insertLog(
                "read product code", self._scanner.get_barcode(), self._user.get_id())
            product = self._productRepository.get_product(
                self._scanner.get_barcode())
            self._shouldBarcodeToBeScannToAddProduct = True
            if product.price == 0:
                validProduct = False
            else:
                validProduct = True

            if validProduct and product.productType == "normal":
                self._bypassList.insertProduct(product.copy_product(), 0)

            if self.state == 1:
                if not self.basketIsFull:
                    if validProduct:
                        if product.meanWeight <= self._lightestWeightForHeavyProduct + self._weightSensor.acceptable_tolerance:
                            self._weightSensor.lightest_weight = self._lightestWeightForLightWeightProduct
                        else:
                            self._weightSensor.lightest_weight = self._lightestWeightForHeavyProduct

                        self.state = 2
                        self.clear_stackView()
                        self.newProduct = product
                        self.countDownTimer = self._insertProductTime + self._timerOffset
                        self._suggestedList.initialize_productList(
                            self._productRepository.get_suggesstionProducts(product.barcode))
                        self.showNewProductScannedSignal.emit()
                        self.hideTopBtnSignal.emit()
                        self._shouldBarcodeToBeScannToAddProduct = True
                    else:
                        self.openPopupMessageTimerSignal.emit(
                            self._lang.lst["mess_Not_valid_Product"])
                        playSound(self._lang.lst["sound_Not_valid_Product"])
                else:
                    self.openPopupMessageTimerSignal.emit(
                        self._lang.lst["mess_Basket_is_full"])
                    playSound(self._lang.lst["sound_Not_valid_Product"])

            elif self.state == 2:
                if self.newProduct.barcode == self._scanner.get_barcode():
                    if self.countDownTimer < self._timerOffset:
                        self.clear_stackView()
                        self.showNewProductScannedSignal.emit()
                        self.hideTopBtnSignal.emit()
                    else:
                        self.closeTopStackViewSignal.emit()
                        self.showNewProductScannedSignal.emit()
                        self.hideTopBtnSignal.emit()
                    self.countDownTimer = self._insertProductTime + self._timerOffset
                else:
                    if validProduct:
                        if product.meanWeight <= self._lightestWeightForHeavyProduct + self._weightSensor.acceptable_tolerance:
                            self._weightSensor.lightest_weight = self._lightestWeightForLightWeightProduct
                        else:
                            self._weightSensor.lightest_weight = self._lightestWeightForHeavyProduct
                        self.clear_stackView()
                        self.newProduct = product
                        self.countDownTimer = self._insertProductTime + self._timerOffset
                        self._suggestedList.initialize_productList(
                            self._productRepository.get_suggesstionProducts(product.barcode))
                        self.showNewProductScannedSignal.emit()
                        self.hideTopBtnSignal.emit()
                    else:
                        self.openPopupMessageTimerSignal.emit(
                            self._lang.lst["mess_Not_valid_Product"])
                        playSound(self._lang.lst["sound_Not_valid_Product"])

            elif self.state == 5:
                if product.productType != "normal":
                    for prod in self._factorList.m_data:
                        if prod._barcode == product._barcode:
                            product.productWeightInBasket = prod.productWeightInBasket
                            if product.productType == "counted":
                                product.countInBasket = prod.countInBasket
                            break

                isAcceptablebarcodeForRemove, self._canRemoveProductClick, removeSuccessfullyBefore = self._removeList.updateValidBarcodeSetForRemove(
                    product)

                if not isAcceptablebarcodeForRemove:
                    if removeSuccessfullyBefore:
                        self.openPopupMessageTimerSignal.emit(
                            self._lang.lst["mess_Please_scan_OTHER_product_that_removed_from_basket"])
                        playSound(
                            self._lang.lst["sound_Please_scan_OTHER_product_that_removed_from_basket"])
                    else:
                        self.openPopupMessageTimerSignal.emit(
                            self._lang.lst["mess_ONLY_scan_product_that_removed_from_basket_please"])
                        playSound(
                            self._lang.lst["sound_ONLY_scan_product_that_removed_from_basket_please"])

                self._trustUser = False
                if len(self._removeList.m_data) == 1:
                    self.openPopupDeleteProductSignal.emit()

            elif self.state == 8:
                self.openPopupMessageTimerSignal.emit(
                    self._lang.lst["mess_Cant_add_product_at_this_session"])
                playSound(
                    self._lang.lst["sound_Cant_add_product_at_this_session"])

    @Slot(int)
    def read_startWeight(self, startWeight: int):
        self._logger.insertLog("start weight", str(
            startWeight), self._user.get_id())
        if abs(startWeight) > 20:
            self.state = -1
            self._basketWeightShouldBe = 0
            self.openPopupMessageSignal.emit(
                self._lang.lst["mess_Please_clear_the_cart"])
            playSound(self._lang.lst["sound_Please_clear_the_cart"])
        else:
            self._basketWeightShouldBe = 0

    @Slot(int, int)
    def basketWeightChanged(self, val2: int, val1: int):
        if not self._inByPass:
            print("--------------> val 2:", val2)
            self.cal_basketLoad(val2)
            self._logger.insertLog("weight change", str(
                val2 - val1), self._user.get_id())
            value: int = val2 - val1

            # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
            # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ADD Weight <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
            # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
            if val2 >= val1:
                if self.state == -1:
                    if self._basketWeightShouldBe - self._basketWeightTolerance <= val2 <= self._basketWeightShouldBe + self._basketWeightTolerance:
                        self.state = 1
                        self.closePopupMessageSignal.emit()

                elif self.state == 1:
                    if not self._shouldBarcodeToBeScannToAddProduct and self.newProduct.get_productType() == "normal":
                        if ((value < self.newProduct.meanWeight + self.newProduct.tolerance) and (
                                value >= self.newProduct.meanWeight - self.newProduct.tolerance)):
                            # insertSound()
                            playSound(self._lang.lst["sound_insert"])
                            self._factorList.insertProduct(self.newProduct, 1)
                            self._bypassList.insertProduct(
                                self.newProduct.copy_product(), 1)
                            # self.cal_basketLoad(val2)
                            self._basketWeightShouldBe = val2
                            self.countDownTimer = -1

                            # self._productsmodel.updateWeight(self.getNewProduct(), val2 - val1)

                        else:
                            self._shouldBarcodeToBeScannToAddProduct = True
                            self.openPopupNoBarcodeScannedSignal.emit()
                            playSound(
                                self._lang.lst["sound_First_take_the_barcode_of_the_product_in_front_of_the_barcode_scanner_then_put_it_in_the_cart"])
                            if abs(value) > 20:
                                # notifSound()
                                playSound(self._lang.lst["sound_notif"])
                            self._basketWeightShouldBe = val1
                            self.state = 4

                    else:
                        self.openPopupNoBarcodeScannedSignal.emit()
                        playSound(
                            self._lang.lst["sound_First_take_the_barcode_of_the_product_in_front_of_the_barcode_scanner_then_put_it_in_the_cart"])
                        if abs(value) > 20:
                            # notifSound()
                            playSound(self._lang.lst["sound_notif"])
                        self._basketWeightShouldBe = val1
                        self.state = 4
                        self._shouldBarcodeToBeScannToAddProduct = True

                elif self.state == 2:
                    if self.newProduct.insertedWeight < self._validInsertedWeightForCalTol:
                        # insertSound()
                        playSound(self._lang.lst["sound_insert"])
                        self._productRepository.updateProduductWeight(
                            self.newProduct, val2 - val1)
                        self._factorList.insertProduct(self.newProduct, 1)
                        self._bypassList.insertProduct(
                            self.newProduct.copy_product(), 1)
                        # self.cal_basketLoad(val2)
                        if self.newProduct.meanWeight > self._lightestWeightForHeavyProduct + self._weightSensor.acceptable_tolerance:
                            self._weightSensor.lightest_weight = self._lightestWeightForHeavyProduct
                        self.clear_stackView()
                        self.state = 1
                        self._basketWeightShouldBe = val2
                        self.countDownTimer = -11
                        self._shouldBarcodeToBeScannToAddProduct = True

                    else:
                        if (value < self.newProduct.meanWeight + self.newProduct.tolerance) and (
                                value >= self.newProduct.meanWeight - self.newProduct.tolerance):
                            # insertSound()
                            playSound(self._lang.lst["sound_insert"])
                            self._productRepository.updateProduductWeight(
                                self.newProduct, val2 - val1)
                            self._factorList.insertProduct(self._newProduct, 1)
                            self._bypassList.insertProduct(self._newProduct, 1)
                            # self.cal_basketLoad(val2)
                            if self.newProduct.meanWeight > self._lightestWeightForHeavyProduct + self._weightSensor.acceptable_tolerance:
                                self._weightSensor.lightest_weight = self._lightestWeightForHeavyProduct
                            self.clear_stackView()
                            self.state = 1
                            self._basketWeightShouldBe = val2
                            self.countDownTimer = -1
                            self._shouldBarcodeToBeScannToAddProduct = False
                        else:
                            self.openPopupWeightNotMatchWithBarcodeSignal.emit()
                            playSound(
                                self._lang.lst["sound_Please_put_the_product_you_scanned_into_the_cart"])
                            self._basketWeightShouldBe = val1
                            self.state = 3
                            self._shouldBarcodeToBeScannToAddProduct = True

                elif self.state == 3:
                    if self._basketWeightShouldBe - self._basketWeightTolerance <= val2 <= self._basketWeightShouldBe + self._basketWeightTolerance:
                        self._basketWeightShouldBe = val2
                        self.state = 1
                        self.closePopupWeightNotMatchWithBarcodeSignal.emit()
                        self.clear_stackView()
                    else:
                        self.openPopupMessageTimerSignal.emit(
                            self._lang.lst["mess_please_remove_not_scanned_product"])
                        playSound(
                            self._lang.lst["sound_please_remove_not_scanned_product"])
                        # notifSound()

                elif self.state == 4:
                    if self._basketWeightShouldBe - self._basketWeightTolerance <= val2 <= self._basketWeightShouldBe + self._basketWeightTolerance:
                        self._basketWeightShouldBe = val2
                        self.closePopupNoBarcodeScannedSignal.emit()
                        self.state = 1
                        self.clear_stackView()
                    elif self._basketWeightShouldBe + self._basketWeightTolerance <= val2:
                        self.openPopupMessageTimerSignal.emit(
                            self._lang.lst["mess_please_remove_not_scanned_products_and_then_insert_them_one_by_one"])
                        playSound(
                            self._lang.lst["sound_please_remove_not_scanned_products_and_then_insert_them_one_by_one"])
                        # notifSound()

                elif self.state == 5:
                    if self._basketWeightShouldBe - self._basketWeightTolerance <= val2 <= self._basketWeightShouldBe + self._basketWeightTolerance:
                        self._basketWeightShouldBe = val2
                        self.closePopupDeleteProductSignal.emit()
                        self.state = 1
                        self.clear_stackView()
                        self._removeList.clearData()
                        self._trustUser = False
                    else:
                        self.openPopupMessageSignal.emit(
                            self._lang.lst["mess_please_remove_inserted_product_from_basket_and_first_complete_remove_process_and_then_insert_product"])
                        playSound(
                            self._lang.lst["sound_please_remove_inserted_product_from_basket_and_first_complete_remove_process_and_then_insert_product"])
                        # notifSound()
                        self.state = 6
                        self._basketWeightRemoveProcess = val1

                elif self.state == 6:
                    if self._basketWeightShouldBe - self._basketWeightTolerance <= val2 <= self._basketWeightShouldBe + self._basketWeightTolerance:
                        self._basketWeightShouldBe = val2
                        self.state = 1
                        self.closePopupMessageSignal.emit()
                        self.closePopupDeleteProductSignal.emit()
                    elif self._basketWeightRemoveProcess - self._basketWeightTolerance <= val2 <= self._basketWeightRemoveProcess + self._basketWeightTolerance:
                        self._basketWeightRemoveProcess = val2
                        self.state = 5
                        self.closePopupMessageSignal.emit()

                elif self.state == 7:
                    if self._basketWeightRemoveProcess - self._basketWeightTolerance <= val2 <= self._basketWeightRemoveProcess + self._basketWeightTolerance:
                        self._basketWeightRemoveProcess = val2
                        self.state = 5
                        self.closePopupMessageSignal.emit()
                    elif self._basketWeightShouldBe - self._basketWeightTolerance <= val2 <= self._basketWeightShouldBe + self._basketWeightTolerance:
                        self._basketWeightShouldBe = val2
                        self.state = 1
                        self.clear_stackView()
                        self.closePopupMessageSignal.emit()
                        self.closePopupDeleteProductSignal.emit()
                        self._removeList.clearData()
                        self._trustUser = False

                elif self.state == 8:
                    self.openPopupMessageSignal.emit(
                        self._lang.lst["mess_Cant_add_or_remove_product_in_this_session"])
                    playSound(
                        self._lang.lst["sound_Cant_add_or_remove_product_in_this_session"])
                    self._basketWeightShouldBe = val1
                    self.state = 9
                    # notifSound

                elif self.state == 9:
                    if self._basketWeightShouldBe - self._basketWeightTolerance <= val2 <= self._basketWeightShouldBe + self._basketWeightTolerance:
                        self.state = 8
                        self.closePopupMessageSignal.emit()

                elif self.state == 10:
                    self.openPopupMessageSignal.emit(
                        self._lang.lst["mess_Cant_add_or_remove_product_in_this_session"])
                    playSound(
                        self._lang.lst["sound_Cant_add_or_remove_product_in_this_session"])
                    self._basketWeightShouldBe = val1
                    self.state = 11
                    # notifSound()

                elif self.state == 11:
                    if self._basketWeightShouldBe - self._basketWeightTolerance <= val2 <= self._basketWeightShouldBe + self._basketWeightTolerance:
                        self.state = 10
                        self.closePopupMessageSignal.emit()

                elif self.state == 12:
                    if abs(val2 - self._basketWeightShouldBe) > 50:
                        # self._basketWeightShouldBe = val1
                        self.turn_offGreenlight()
                        # self.openPopupMessageSignal.emit(
                        #     self._lang.lst["mess_Cant_add_or_remove_product_in_this_session"])
                        # playSound(
                        #     self._lang.lst["sound_Cant_add_or_remove_product_in_this_session"])
                        self.state = 13

                elif self.state == 13:
                    if self._basketWeightShouldBe - self._basketWeightTolerance <= val2 <= self._basketWeightShouldBe + self._basketWeightTolerance:
                        self.state = 12
                        self._basketWeightShouldBe = val2
                        self.closePopupMessageSignal.emit()
                        self.turn_onGreenLight()

                elif self.state == 14:
                    self.newProduct.set_productWeightInBasket(
                        val2 - self._pluStartWeight)

                elif self.state == 15:
                    self.newProduct.set_productWeightInBasket(
                        val2 - self._pluStartWeight)

            # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
            # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> REMOVE WEIGHT <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
            # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
            if val2 < val1:
                if self.state == -1:
                    if self._basketWeightShouldBe - self._basketWeightTolerance <= val2 <= self._basketWeightShouldBe + self._basketWeightTolerance:
                        self.state = 1
                        self.closePopupMessageSignal.emit()

                elif self.state == 1:
                    self._shouldBarcodeToBeScannToAddProduct = True
                    self._removeList.validBarcodeSetForRemove(
                        self._factorList.m_data, abs(value))
                    if not len(self._removeList.m_validBarcodeSetForDelete) == 0:
                        self._removeLookupList.clearData()
                        for prod in self._factorList.m_data:
                            if prod._productType != "normal":
                                self._removeLookupList.insertProduct(
                                    prod, prod.countInBasket)
                        self.openPopupDeleteProductSignal.emit()
                        # notifSound2()
                        playSound(self._lang.lst["sound_notif2"])
                        self._basketWeightShouldBe = val1
                        self.state = 5

                elif self.state == 2:
                    self._shouldBarcodeToBeScannToAddProduct = True
                    self._removeList.validBarcodeSetForRemove(
                        self._factorList.m_data, abs(value))
                    self.clear_stackView()
                    self.openPopupDeleteProductSignal.emit()
                    # notifSound2()
                    playSound(self._lang.lst["sound_notif2"])
                    self._basketWeightShouldBe = val1
                    self.countDownTimer = -20
                    self.state = 5

                elif self.state == 3:
                    if self._basketWeightShouldBe - self._basketWeightTolerance <= val2 < self._basketWeightShouldBe + self._basketWeightTolerance:
                        self._basketWeightShouldBe = val2
                        self.closePopupWeightNotMatchWithBarcodeSignal.emit()
                        self.clear_stackView()
                        self.state = 1

                elif self.state == 4:
                    if self._basketWeightShouldBe - self._basketWeightTolerance <= val2 <= self._basketWeightShouldBe + self._basketWeightTolerance:
                        self._basketWeightShouldBe = val2
                        self.closePopupNoBarcodeScannedSignal.emit()
                        self.clear_stackView()
                        self.state = 1

                elif self.state == 5:
                    self.openPopupMessageSignal.emit(
                        self._lang.lst["mess_Please_replace_product_that_removed_from_basket_and_after_complete_current_remove_process_remove_another_product"])
                    playSound(
                        self._lang.lst["sound_Please_replace_product_that_removed_from_basket_and_after_complete_current_remove_process_remove_another_product"])
                    # notifSound()
                    self.state = 7
                    self._basketWeightRemoveProcess = val1

                elif self.state == 6:
                    if self._basketWeightRemoveProcess - self._basketWeightTolerance <= val2 <= self._basketWeightRemoveProcess + self._basketWeightTolerance:
                        self._basketWeightRemoveProcess = val2
                        self.state = 5
                        self.closePopupMessageSignal.emit()

                elif self.state == 7:
                    if self._basketWeightRemoveProcess - self._basketWeightTolerance <= val2 <= self._basketWeightRemoveProcess + self._basketWeightTolerance:
                        self._basketWeightRemoveProcess = val2
                        self.setState(5)
                        self.closePopupMessage.emit()
                    elif self._basketWeightShouldBe - self._basketWeightTolerance <= val2 <= self._basketWeightShouldBe + self._basketWeightTolerance:
                        self._basketWeightShouldBe = val2
                        self.clear_stackView()
                        self.state = 1
                        self.closePopupMessage.emit()
                        self.closePopupDeleteProduct.emit()
                        self._removeList.clearData()
                        self._trustUser = False

                elif self.state == 8:
                    self.openPopupMessageSignal.emit(
                        self._lang.lst["mess_Cant_add_or_remove_product_in_this_session"])
                    playSound(
                        self._lang.lst["sound_Cant_add_or_remove_product_in_this_session"])
                    self._basketWeightShouldBe = val1
                    self.state = 9
                    # notifSound()

                elif self.state == 9:
                    if self._basketWeightShouldBe - self._basketWeightTolerance <= val2 <= self._basketWeightShouldBe + self._basketWeightTolerance:
                        self.state = 8
                        self.closePopupMessageSignal.emit()

                elif self.state == 10:
                    self.openPopupMessageSignal.emit(
                        self._lang.lst["mess_Cant_add_or_remove_product_in_this_session"])
                    playSound(
                        self._lang.lst["sound_Cant_add_or_remove_product_in_this_session"])
                    self._basketWeightShouldBe = val1
                    self.state = 11
                    # notifSound()

                elif self.state == 11:
                    if self._basketWeightShouldBe - self._basketWeightTolerance <= val2 <= self._basketWeightShouldBe + self._basketWeightTolerance:
                        self.state = 10
                        self.closePopupMessageSignal.emit()

                elif self.state == 12:
                    if abs(val2 - self._basketWeightShouldBe) > 50:
                        # self._basketWeightShouldBe = val1
                        # self.openPopupMessageSignal.emit(
                        #     self._lang.lst["mess_Cant_add_or_remove_product_in_this_session"])
                        # playSound(
                        #     self._lang.lst["sound_Cant_add_or_remove_product_in_this_session"])
                        self.turn_offGreenlight()
                        self.state = 13

                elif self.state == 13:
                    if self._basketWeightShouldBe - self._basketWeightTolerance <= val2 <= self._basketWeightShouldBe + self._basketWeightTolerance:
                        self.state = 12
                        self._basketWeightShouldBe = val2
                        self.closePopupMessageSignal.emit()
                        self.turn_onGreenLight()

                elif self.state == 14:
                    self.newProduct.set_productWeightInBasket(
                        val2 - self._pluStartWeight)

                elif self.state == 15:
                    self.newProduct.set_productWeightInBasket(
                        val2 - self._pluStartWeight)

    @Slot()
    def timerSlot(self):
        while self._canTimerTick:
            if self.state == 2 or self.state == 1:
                self.countDownTimer = self.countDownTimer - 1
                sleep(1)

            if self.countDownTimer == self._timerOffset:
                if self.state == 2:
                    self.clear_stackView()
                    # self.closeTopStackViewSignal.emit()
                    # sleep(1)
            if self.countDownTimer == 0:
                if self.state == 2:
                    self.state = 1
                    # self.clearStackView()
                    # self.closeAllPopUps.emit()
                    # self.turn_offGreenlight()
                    self._shouldBarcodeToBeScannToAddProduct = True
                    # self._weightSensor.lightest_weight = self._lightestWeightForHeavyProduct

            if self.countDownTimer == -10:
                if self.state == 1:
                    self._shouldBarcodeToBeScannToAddProduct = True
                    # self._weightSensor.lightest_weight = self._lightestWeightForHeavyProduct

    @Slot()
    def IDBarcode_read(self):
        self._logger.insertLog(
            "ID cart scanned", self._scanner.get_IDBarcode(), self._user.get_id())
        if self._adminRepository.Login(self._scanner.get_IDBarcode()):
            if not self._inByPass:
                self._inByPass = True
                self.clear_stackView()
                self.closeAllPopUpSignal.emit()
                self.openPopupByPassSignal.emit()

    @Slot()
    def nfc_read(self):
        if self.state == 10:
            self._logger.insertLog("nfc read", "", self._user.get_id())
            self.showPaymentPinSignal.emit()

    @Slot()
    def tempSlot(self):
        self.openPopupMessageTimerSignal.emit(
            self._lang.lst["mess_Please_check_your_email_address"] + self._emailException)
        playSound(self._lang.lst["sound_Please_check_your_email_address"])
        self._requestForSendingEmail = False


    @Slot()
    def gotoWifiSettings(self):
        self._wifimodel = WirelessModel()
        # self._wifimodel.threadscanerFinished.connect(self.finishwifiscannerThread)

    @Slot()
    def backFromWifiSettigs(self):
        time.sleep(1)
        self._wifimodel.destroy()
        self._inByPass = False
        self._state = 1
        # del self._wifimodel
        # print("backed")

    ####################################################################################################### UI Sluts ###
    @Slot()
    def call_forHelpClicked(self):
        self._logger.insertLog("call for help clicked",
                               "", self._user.get_id())
        playSound(self._lang.lst["sound_call_for_help"])

    @Slot()
    def cancel_newProductClicked(self):
        self.clear_stackView()
        self.countDownTimer = 0
        if self.state == 2:
            self.state = 1
            self._shouldBarcodeToBeScannToAddProduct = True

    @Slot()
    def see_allOfferListClicked(self):
        if self.state == 1 and self._inOfferList == False:
            self.showAllOfferListSignal.emit()
            self._inOfferList = True

    @Slot()
    def close_allOfferListClicked(self):
        if self.state == 1:
            self.clear_stackView()
            self._inOfferList = False

    @Slot()
    def manual_barcodeClicked(self):
        if self.state == 1:
            self.showManualBarcodeSignal.emit()
            self.hideTopBtnSignal.emit()

    @Slot()
    def cancel_manualBarcodeClicked(self):
        if self.state == 1:
            self.clear_stackView()

    @Slot(str)
    def confirm_manualBarcodeClicked(self, barcode: str):
        if self.state == 1:
            if len(barcode) == self._scanner.get_productBarcodeLength():
                if self._productRepository.get_product(barcode).price != 0:
                    self.clear_stackView()
                    self._scanner._barcode = barcode
                    self.barcodeRead()
                else:
                    self.openPopupMessageTimerSignal.emit(
                        self._lang.lst["mess_Please_check_entered_barcode"])
                    playSound(
                        self._lang.lst["sound_Please_check_entered_barcode"])
            else:
                self.openPopupMessageTimerSignal.emit(
                    self._lang.lst["mess_please_enter"] + str(self._scanner.get_productBarcodeLength()) + self._lang.lst["mess_digits_barcode"])
            playSound(
                self._lang.lst["sound_please_enter_correct_digits_barcode"])

    @Slot()
    def show_addPLUItemsClicked(self):  # not in state 5
        if self.state == 1:
            self.showAddPLUItemsSignal.emit()
            self.hideTopBtnSignal.emit()
            self.newProduct = Product()

    @Slot()
    def back_addPLUItemsClicked(self):
        self.clear_stackView()
        if self.state == 14 or self.state == 15:
            if self._basketWeightShouldBe - self._basketWeightTolerance <= self._weightSensor.basketweight <= self._basketWeightShouldBe + self._basketWeightTolerance:
                self.state = 1
            else:
                self._shouldBarcodeToBeScannToAddProduct = True
                self.openPopupNoBarcodeScannedSignal.emit()
                playSound(
                    self._lang.lst["sound_First_take_the_barcode_of_the_product_in_front_of_the_barcode_scanner_then_put_it_in_the_cart"])
                self.state = 4

    @Slot(str)
    def item_PLUClicked(self, pluCode: str):
        self.newProduct = self._productRepository.get_product(pluCode)
        self._logger.insertLog("lookup by name", pluCode, self._user.get_id())
        if self.newProduct.get_productType() == "weighted":
            self.state = 14
            self.showWeightedPLUItemsSignal.emit()
            self.openPopupMessageSignal.emit(
                self._lang.lst["mess_Taring_Please_dont_move_basket"])
            playSound(self._lang.lst["sound_Taring_Please_dont_move_basket"])
            if self._canCreatePLUCheckThread:
                self._PLUThread = Thread(target=self.taringPLU)
                self._PLUThread.start()

        elif self.newProduct.get_productType() == "counted":
            self.state = 15
            self.showCountedPLUItemsSignal.emit()
            self.openPopupMessageSignal.emit(
                self._lang.lst["mess_Taring_Please_dont_move_basket"])
            playSound(self._lang.lst["sound_Taring_Please_dont_move_basket"])
            if self._canCreatePLUCheckThread:
                self._PLUThread = Thread(target=self.taringPLU)
                self._PLUThread.start()

    @Slot()
    def confirm_PLUItemClicked(self):
        if self.state == 14:
            if self._weightSensor.isstable:
                if self.newProduct.productWeightInBasket != 0:
                    self._logger.insertLog("add weighted product", str(self._newProduct.productWeightInBasket),
                                           self._user.get_id())
                    self._factorList.insertProduct(self.newProduct, 1)
                    self._bypassList.insertProduct(
                        self.newProduct.copy_product(), 1)
                    self.state = 1
                    self.clear_stackView()
                    self._basketWeightShouldBe = self._pluStartWeight + \
                        self.newProduct.productWeightInBasket
                    self.cal_basketLoad(self._basketWeightShouldBe)
                    # insertSound()
                    playSound(self._lang.lst["sound_insert"])
                else:
                    self.openPopupMessageTimerSignal.emit(
                        self._lang.lst["mess_You_select_zero_weight"])
                    playSound(self._lang.lst["sound_You_select_zero_weight"])

            else:
                self.openPopupMessageTimerSignal.emit(
                    self._lang.lst["mess_Please_wait"])
                playSound(self._lang.lst["sound_Please_wait"])
        elif self.state == 15:
            if self._weightSensor.isstable:
                if self.newProduct.countInBasket != 0:
                    self._logger.insertLog("add counted product", str(self._newProduct.countInBasket),
                                           self._user.get_id())
                    self._factorList.insertProduct(
                        self.newProduct, self.newProduct.countInBasket)
                    self._bypassList.insertProduct(
                        self.newProduct.copy_product(), self.newProduct.countInBasket)
                    self.state = 1
                    self.clear_stackView()
                    self._basketWeightShouldBe = self._weightSensor.readbasketweight()
                    self.cal_basketLoad(self._basketWeightShouldBe)
                    # insertSound()
                    playSound(self._lang.lst["sound_insert"])
                else:
                    self.openPopupMessageTimerSignal.emit(
                        self._lang.lst["mess_You_select_zero_count"])
                    playSound(self._lang.lst["sound_You_select_zero_count"])

            else:
                self.openPopupMessageTimerSignal.emit(
                    self._lang.lst["mess_Please_wait"])
                playSound(self._lang.lst["sound_Please_wait"])

    @Slot(str)
    def search_PLUItem(self, PLUCode: str):
        self.newProduct = self._productRepository.get_product(PLUCode)

    @Slot()
    def increase_PLUClicked(self):
        if self.state == 15:
            self.newProduct.countInBasket = self.newProduct.countInBasket + 1

    @Slot()
    def decrease_PLUClicked(self):
        if self.state == 15:
            if self.newProduct.countInBasket > 0:
                self.newProduct.countInBasket = self.newProduct.countInBasket - 1

    @Slot()
    def product_removeConfirmClicked(self):
        if self._trustUser:
            self._logger.insertLog("remove product on trust user", str(
                len(self._removeList.m_data)), self._user.get_id())
            # deleteSound()
            playSound(self._lang.lst["sound_remove"])
            self._canRemoveProductClick = False
            self._factorList.removeProducts(self._removeList.m_data)
            self._bypassList.removeProductsUpdateBypass(
                self._removeList.m_data)
            self._removeList.clearData()
            self.state = 1
            self._trustUser = False
            self.closePopupDeleteProductSignal.emit()
            self.clear_stackView()

        else:
            if not self._canRemoveProductClick:
                # notifSound2()
                self.openPopupMessageTimerSignal.emit(
                    self._lang.lst["mess_Please_scann_all_product_that_remove_from_basket"])
                playSound(
                    self._lang.lst["sound_Please_scann_all_product_that_remove_from_basket"])
                # self._trustUser = True
            else:
                self._logger.insertLog("normal remove product", str(
                    len(self._removeList.m_data)), self._user.get_id())
                # deleteSound()
                playSound(self._lang.lst["sound_remove"])
                self._canRemoveProductClick = False
                self._factorList.removeProducts(self._removeList.m_data)
                self._bypassList.removeProductsUpdateBypass(
                    self._removeList.m_data)
                self._removeList.clearData()
                self.state = 1
                self._trustUser = False
                self.closePopupDeleteProductSignal.emit()
                self.clear_stackView()

    @Slot(str)
    def product_removeManualBarcodeEntered(self, barcode: str):
        if self.state == 5:
            if len(barcode) == self._scanner.get_productBarcodeLength() or len(barcode) == self._pluCodeLength:
                self._scanner._barcode = barcode
                self.barcodeRead()
            else:
                self.openPopupMessageTimerSignal.emit(
                    self._lang.lst["mess_Please_recheck_entered_code"])
                playSound(self._lang.lst["sound_Please_recheck_entered_code"])

    @Slot(str)
    def product_removeLookupSelected(self, plu: str):
        self.product_removeManualBarcodeEntered(plu)

    @Slot(int)
    def product_removeIncreaseClicked(self, index: int):
        self._scanner.barcode = self.removeList.m_data[index].barcode
        self.barcodeRead()

    @Slot(int)
    def product_removeDecreaseClicked(self, index: int):
        self.removeList.m_validBarcodeSetForDelete.append(
            self.removeList.m_data[index].barcode)
        self.removeList.decreaseClicked(index)

    @Slot()
    def accept_byPassClicked(self):
        if self._weightSensor.isstable:
            self._logger.insertLog(
                "operator confirmed cart", "", self._user.get_id())
            self._factorList.clearData()
            self._factorList.insert_productList(self._bypassList.m_data)
            self._removeList.clearData()
            self.state = 1
            self.clear_stackView()
            self._inByPass = False
            self.closeAllPopUpSignal.emit()
            self.closePopupByPassSignal.emit()

            self.state = 1
            self._countDownTimer = -60
            self._basketWeightShouldBe = self._weightSensor.readbasketweight()
            self._basketWeightRemoveProcess = 0
            self.cal_basketLoad(self._basketWeightShouldBe)
            self._manualBarcodeEntered = False
            self._canRemoveProductClick = False
            self._trustUser = False
            self._shouldBarcodeToBeScannToAddProduct = True
            self._pluStartWeight = 0

        else:
            self.openPopupMessageTimerSignal.emit(
                self._lang.lst["mess_Please_wait"])
            playSound(self._lang.lst["sound_Please_wait"])

    @Slot(int)
    def bypass_increaseClicked(self, index: int):
        self._bypassList.increaseClicked(index)

    @Slot(int)
    def bypass_decreaseClicked(self, index: int):
        self._bypassList.decreaseClicked(index)

    @Slot()
    def checkout_clicked(self):
        if self.state == 1:
            if len(self._factorList.m_data) > 0:
                self._logger.insertLog("check out", str(
                    len(self._factorList.m_data)), self._user.get_id())
                self.state = 8
                self.showCheckOutSignal.emit()
            else:
                self.openPopupMessageTimerSignal.emit(
                    self._lang.lst["mess_Yor_factor_is_empty"])
                playSound(self._lang.lst["sound_Yor_factor_is_empty"])

    @Slot()
    def checkout_backClicked(self):
        if self.state == 8:
            self._logger.insertLog("back from check out",
                                   "", self._user.get_id())
            self.state = 1
            self.clear_stackView()

    @Slot(str)
    def apply_couponCode(self, code):
        if self.state == 8:
            if code == "221222":
                self._couponCode = "221222"
                self._logger.insertLog(
                    "apply coupon", str(code), self._user.get_id())
                self.factorList.set_offerCouponPercentage(10.0)
            else:
                self.openPopupMessageTimerSignal.emit(
                    self._lang.lst["mess_Invalid_code_please_check_the_code"])
                playSound(
                    self._lang.lst["sound_Invalid_code_please_check_the_code"])

    @Slot()
    def payment_clicked(self):
        if self.state == 8:
            self._logger.insertLog(
                "choose nfc for payment", "", self._user.get_id())
            self.showPaymentSignal.emit(0)
            self.state = 10
            self._nfc = nfc()
            self._nfc.nfcReaderSignal.connect(self.nfc_read)

    @Slot()
    def payment_viaQRClicked(self):
        if self.state == 8:
            self._logger.insertLog(
                "choose Qr for payment", "", self._user.get_id())
            self.showPaymentSignal.emit(1)
            self.state = 10

    @Slot()
    def payment_QRClicked(self):   # this ia a demo for payment through Qr code
        if self.state == 10:
            self.state = 12
            self.showAfterPaymentSignal.emit()
            self.save_factorLocal()
            self.turn_onGreenLight()

    @Slot()
    def payment_backClicked(self):
        if self.state == 10:
            self.state = 8

    @Slot(str)
    def enter_pinPayment(self, pin: str):
        print(pin)
        if self.state == 10:
            if pin == "2212":
                self.state = 12
                self.showAfterPaymentSignal.emit()
                self.save_factorLocal()
                self.turn_onGreenLight()
            else:
                self.openPopupMessageTimerSignal.emit(
                    self._lang.lst["mess_Invalid_pin_code_entered_Please_try_again"])
                playSound(
                    self._lang.lst["sound_Invalid_pin_code_entered_Please_try_again"])

    @Slot(str)
    def send_factorEmailClicked(self, emailAddress: str):
        if not self._requestForSendingEmail:
            self._requestForSendingEmail = True
            self._enteredEmail = emailAddress
            self.openPopupMessageSignal.emit(
                self._lang.lst["mess_Your_factor_will_be_send_to"] + self._enteredEmail)
            self._logger.insertLog(
                "request for send factor", emailAddress, self._user.get_id())
            # playSound(self._lang.lst["sound_Your_factor_will_be_send_to"])

            self._emailThread = Thread(target=self.send_emailFactorThread)
            self._emailThread.start()

    @Slot(int)
    def rate_cart(self, rate: int):
        if not self._rated:
            self._rated = True
            self._logger.insertLog("rate", str(rate), self._user.get_id())
            print(rate)
            self._userRepository.updateRate(self._user.get_id(), str(rate))
            self.openPopupMessageTimerSignal.emit(
                self._lang.lst["mess_Tanks_for_yor_rating"])
            playSound(self._lang.lst["sound_Tanks_for_yor_rating"])

    @Slot(str)
    def search_plu(self, s: str):
        print(s)
        self._pluList.searchByName(s)

    ###################################################################################################### Functions ###
    def print_states(self):
        if self.state == -1:
            print("\nState " + str(self._states) +
                  " : Start with weight in basket or out of calibrate.\n")
        elif self.state == 1:
            print("\nState " + str(self._states) + " : Stable.\n")
        elif self.state == 2:
            print("\nState " + str(self._states) +
                  " : A Barcode was read and waiting for Weight to add.\n")
        elif self.state == 3:
            print("\nState " + str(self._states) +
                  " : Inserted Weight not match with read Barcode.\n")
        elif self.state == 4:
            print("\nState " + str(
                self._states) + " : Inserted Weight without barcode.(match with last product or non valid insert weight)\n")
        elif self.state == 5:
            print("\nState " + str(self._states) +
                  " : Weight removed. waiting to read barcode\n")
        elif self.state == 6:
            print("\nState " + str(self._states) +
                  " : Insert Invalid Weight While Remove Product.\n")
        elif self.state == 7:
            print("\nState " + str(self._states) +
                  " : 1+ steps removed Weight.\n")
        elif self.state == 8:
            print("\nState " + str(self._states) + " : checkout clicked.\n")
        elif self.state == 9:
            print("\nState " + str(self._states) +
                  " : weight change in checkout.\n")
        elif self.state == 10:
            print("\nState " + str(self._states) +
                  " : waiting for payment in payment page.\n")
        elif self.state == 11:
            print("\nState " + str(self._states) +
                  " : weight change while waiting for payment.\n")
        elif self.state == 12:
            print("\nState " + str(self._states) +
                  " : go to after payment page after successful payment.\n")
        elif self.state == 13:
            print("\nState " + str(self._states) +
                  " : weight change after payment.\n")
        elif self.state == 14:
            print("\nState " + str(self._states) +
                  " : weighted PLU product selected.\n")
        elif self.state == 15:
            print("\nState " + str(self._states) +
                  " : counted PLU product selected.\n")

    def add_productToFactor(self, p: Product, c: int, u: bool, w2: int, w1: int):
        # insertSound()
        playSound(self._lang.lst["sound_insert"])
        self._factorList.insertProduct(p, c)
        self._bypassList.insertProduct(p.copy_product(), c)
        if u:
            pass
            # self._factorList.updateWeight(p, w2 - w1)
        self._basketWeightShouldBe = w2
        self.cal_basketLoad(w2)

    def cal_basketLoad(self, weight: int):
        load = int((weight - self._startWeight) /
                   self._basketWeightLimit * 100)
        load = min(max(load, 0), 100)
        self._logger.insertLog("basket load", str(load), self._user.get_id())
        print("------------------ load :", load)
        self.set_basketLoad(load)
        self.set_basketIsFull(
            True) if load == 100 else self.set_basketIsFull(False)

    def turn_onGreenLight(self):
        self.greenLight = GreenLight(True)
        self.greenLight.finished.connect(self.greenLight.deleteLater)
        self.greenLight.start()

    def turn_offGreenlight(self):
        self.greenLight = GreenLight(False)
        self.greenLight.finished.connect(self.greenLight.deleteLater)
        self.greenLight.start()

    def check_productWeight(self, product: Product):
        if product.meanWeight <= self._lightestWeightForHeavyProduct + self._weightSensor.acceptable_tolerance:
            self._lightWeightProductExistInBasket = True

    def adjust_wightSensorSensitivity(self, weight: int = -1):
        if self._lightWeightProductExistInBasket:
            self._weightSensor.lightest_weight = self._lightestWeightForLightWeightProduct

        elif 0 < weight <= self._lightestWeightForHeavyProduct + self._weightSensor.acceptable_tolerance:
            self._weightSensor.lightest_weight = self._lightestWeightForLightWeightProduct
        else:
            self._weightSensor.lightest_weight = self._lightestWeightForHeavyProduct

    def clear_stackView(self):
        self.showTopBtnSignal.emit()
        self.clearStackViewSignal.emit()
        self._inOfferList = False
        if len(self._factorList.m_data) > 0:
            self.showFactorListSignal.emit()

    def taringPLU(self):
        self._canCreatePLUCheckThread = False
        taring = True
        while taring:
            if self._weightSensor._canread:
                self._pluStartWeight = self._weightSensor._BasketWeight2
                taring = False
        self._basketWeightShouldBe = self._pluStartWeight
        self.closePopupMessageSignal.emit()
        self._canCreatePLUCheckThread = True

    def send_emailFactorThread(self):
        try:
            v = validate_email(self._enteredEmail)
            standardEmail = v["email"]

            self._userRepository.updateEmail(
                self._user.get_id(), self._enteredEmail)

            factor = {}
            factor["emailAddress"] = standardEmail
            factor["paymentTime"] = str(datetime.now())
            with open("/home/aptinet/basketName.txt", 'r') as f:
                factor["basketName"] = f.readline()

            if self._user.get_loggedInUser().get_id() != "":
                factor["userId"] = self._user.get_loggedInUser().get_id()
            else:
                factor["userId"] = self._user.get_id()

            factor["totalCount"] = str(self._factorList.get_totalCount())
            factor["totalPrice"] = "{:.2f}".format(
                self._factorList.get_pricenodiscount())
            factor["totalFinalPrice"] = "{:.2f}".format(
                self._factorList.get_finalprice())
            factor["totalTax"] = "{:.2f}".format(self._factorList.get_tax())
            factor["totalSaving"] = "{:.2f}".format(
                self._factorList.getProfit())
            factor["priceToPay"] = "{:.2f}".format(
                self._factorList.get_priceToPay())
            if self._factorList.get_offerCouponPercentage() != 0:
                factor["coupon"] = ""
            else:
                factor["coupon"] = "221222"

            factor["products"] = []
            for p in self._factorList.m_data:
                prod = {}
                prod["barcode"] = p.get_barcode()
                prod["name"] = p.get_name()
                if p.get_productType == "weighted":
                    prod["count"] = "1"
                    prod["weight"] = str(p.get_productWeightInBasket())
                else:
                    prod["count"] = str(p.get_countInBasket())
                    prod["weight"] = ""

                prod["productPrice"] = p.get_priceQML()
                prod["productTotalPrice"] = p.get_totalPriceQML()
                prod["productFinalPrice"] = p.get_finalPriceQML()
                prod["productTotalFinalPrice"] = p.get_totalFinalPriceQML()
                prod["productSaving"] = p.get_totalSavingQML()
                prod["productTax"] = p.get_totalTaxQML()
                factor["products"].append(prod)
            jsonFactorString = json.dumps(factor)
            # with open("/home/aptinet/factor.json", 'w', encoding='utf-8') as f:
            #     f.write(jsonFactorString)

            self._restAPI.Post(self._mailServiceURL, jsonFactorString)
            self.closePopupMessageSignal.emit()
            self._requestForSendingEmail = False

        except EmailNotValidError as e:
            self.closePopupMessageSignal.emit()
            self._emailException = str(e)
            self.tempSignal.connect(self.tempSlot)
            self.tempSignal.emit()

    def save_factorLocal(self):
        try:
            self._userRepository.updateFactorprices(self._user.get_id(), str(
                self._factorList.get_pricenodiscount()), str(self._factorList.get_finalprice()), self._couponCode)
            self.send_factorToServer()
            for prod in self._factorList.m_data:
                count = ""
                weight = ""
                if prod.productType == "weighted":
                    count = "1"
                    weight = prod.mountQML
                else:
                    count = prod.mountQML
                    weight = ""
                self._factorRepository.insertFactor(self._user.get_id(), prod.barcode, count, weight,
                                                    prod.get_priceQML(), prod.get_finalPriceQML(),
                                                    str(prod._taxPercentage), prod.savingQML)
        except:
            print("cant save factor locally")

    def send_factorToServer(self):
        factor = {}
        factor["paymentTime"] = str(datetime.now())
        with open("/home/aptinet/basketName.txt", 'r') as f:
            factor["basketName"] = f.readline()

        if self._user.get_loggedInUser().get_id() != "":
            factor["userId"] = self._user.get_loggedInUser().get_id()
        else:
            factor["userId"] = self._user.get_id()

        factor["totalCount"] = str(self._factorList.get_totalCount())
        factor["totalPrice"] = "{:.2f}".format(
            self._factorList.get_pricenodiscount())
        factor["totalFinalPrice"] = "{:.2f}".format(
            self._factorList.get_finalprice())
        factor["totalTax"] = "{:.2f}".format(self._factorList.get_tax())
        factor["totalSaving"] = "{:.2f}".format(self._factorList.getProfit())
        factor["priceToPay"] = "{:.2f}".format(
            self._factorList.get_priceToPay())
        if self._factorList.get_offerCouponPercentage() != 0:
            factor["coupon"] = ""
        else:
            factor["coupon"] = "221222"

        factor["products"] = []
        for p in self._factorList.m_data:
            prod = {}
            prod["barcode"] = p.get_barcode()
            prod["name"] = p.get_name()
            if p.get_productType == "weighted":
                prod["count"] = "1"
                prod["weight"] = str(p.get_productWeightInBasket())
            else:
                prod["count"] = str(p.get_countInBasket())
                prod["weight"] = ""

            prod["productPrice"] = p.get_priceQML()
            prod["productTotalPrice"] = p.get_totalPriceQML()
            prod["productFinalPrice"] = p.get_finalPriceQML()
            prod["productTotalFinalPrice"] = p.get_totalFinalPriceQML()
            prod["productSaving"] = p.get_totalSavingQML()
            prod["productTax"] = p.get_totalTaxQML()
            factor["products"].append(prod)
        jsonFactorString = json.dumps(factor)
        self._restAPI.Post(self._saveFactorURL, jsonFactorString)
    
    @Slot(str)
    def data_recivedFromServer(self,s:str):
        if(s is not "-1"):
            self.closePopupMessageSignal.emit()
            self._requestForSendingEmail = False

