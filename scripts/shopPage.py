import os
import sys
import time
from time import sleep
from threading import Thread
from email_validator import validate_email, EmailNotValidError

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

from Helpers.scannerHelper import ScannerHelper
# from Helpers.weightSensorHelper import WeightSensorHelper

from Repositories.userRepository import UserRepository
from Repositories.userServerRepository import UserServerRepository
from Repositories.productRepository import ProductRepository


class ShopPage(QObject):
    ####################################################################################################### Settings ###
    _insertProductTime: int = 8  # actual time = n -1
    _timerOffset: int = 3
    _validInsertedWeightForCalTol: int = 3  # Accept inserted product without checking weight under this limit
    _basketWeightLimit: int = 20000  # grams
    _lightestProductWeight: int = 11  # grams
    _lightestWeightForHeavyProduct: int = 25  # grams
    _lightestWeightForLightWeightProduct: int = 8
    _basketWeightTolerance: int = 50  # better fit: 25

    ######################################################################################################### Models ###
    _factorList: ProductModel
    _offersList: ProductModel
    _offerTopTen: ProductModel
    _suggestedList: ProductModel
    _pluList: ProductModel
    _pluTopFour: ProductModel
    _bypassList: ProductModel
    _removeList: ProductModel

    ################################################################################################### Repositories ###
    _userRepository: UserRepository
    _userServerRepository: UserServerRepository
    _productRepository: ProductRepository

    ######################################################################################################## Objects ###
    _user: User
    _loggedInUser: ServerUser
    _newProduct: Product

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

    ######################################################################################################## Modules ###
    _weightSensor: WeightSensorWorker
    _nfc: nfc

    def __init__(self, dal: DAL, user: User, scanner: ScannerHelper):
        super().__init__()

        #### Private ##############################################
        self._dal = dal

        #### Repositories #########################################
        self._userRepository = UserRepository(self._dal)
        self._userServerRepository = UserServerRepository(self._dal)
        self._productRepository = ProductRepository(self._dal)

        #### Barcode Scanner ######################################
        self._scanner = scanner
        self._scanner.EAN13ReadSignal.connect(self.barcodeRead)
        self._scanner.IDBarcodeReadSignal.connect(self.IDBarcode_read)

        #### WeightSensor #########################################
        self._weightSensor = WeightSensorWorker()
        self._weightSensor.basketweight_changed.connect(self.basketWeightChanged)
        self._weightSensor.startWeightchanged.connect(self.read_startWeight)
        self._weightSensor.start()

        #### Models ###############################################
        self._newProduct = Product()
        self._factorList = ProductModel()
        self._offersList = ProductModel()
        self._offersList.initialize_productList(self._productRepository.get_offerProducts())
        self._offerTopTen = ProductModel()
        self._offerTopTen.initialize_productList(self._productRepository.get_topOfferProducts())
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

        #### User #################################################
        self._user = user

        #### Insert Timer Thread ##################################
        self._canTimerTick = True
        self._timerThread = Thread(target=self.timerSlot)
        self._timerThread.start()

        ########################################################### end of __init__

    ######################################################################################################## Signals ###
    changedSignal = Signal()

    #### Stack view Signals #######################################
    clearStackViewSignal = Signal()  # clear stack view
    closeTopStackViewSignal = Signal()  # close top stack view. maybe used for several purpose like close new product scanned stack view
    hideTopBtnSignal = Signal()  # hide manual barcode btn and PLU btn

    showFactorListSignal = Signal()  # show factor list
    showNewProductScannedSignal = Signal()  # show new product scanned and suggestion list
    showAllOfferListSignal = Signal()  # show all offer list
    showManualBarcodeSignal = Signal()  # show manual barcode view
    showAddPLUItemsSignal = Signal()  # shoe first PLU view
    showWeightedPLUItemsSignal = Signal()  # show weighted PLU view
    showCountedPLUItemsSignal = Signal()  # show counted PLU view
    showTopBtnSignal = Signal()  # show manual barcode btn and PLU btn
    showCheckOutSignal = Signal()  # show check out view
    showPaymentSignal = Signal(int)   # 0 for NFC payment, 1 for Qr paymeny
    showAfterPaymentSignal = Signal()

    #### Popup Signals ############################################
    closeAllPopUpSignal = Signal()

    openPopupMessageTimerSignal = Signal(str)
    closePopUpMessageTimer = Signal()

    openPopupMessageSignal = Signal(str)
    closePopupMessageSignal = Signal()

    openPopupWeightNotMatchWithBarcodeSignal = Signal()  # pop up weight not match with scanned barcode
    closePopupWeightNotMatchWithBarcodeSignal = Signal()

    openPopupNoBarcodeScannedSignal = Signal()  # add product to basket without scanning barcode
    closePopupNoBarcodeScannedSignal = Signal()

    openPopupDeleteProductSignal = Signal()  # remove product from basket
    closePopupDeleteProductSignal = Signal()

    openPopUpMessageNotAllowedChangeWeightSignal = Signal()  # change weight at the end of shopping
    closePopUpMessageNotAllowedChangeWeightSignal = Signal()

    openPopupByPassSignal = Signal()  # open by pass pop up
    closePopupByPassSignal = Signal()

    ##################################################################################################### Properties ###
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

    newProduct = Property(Product, get_newProduct, set_newProduct, notify=changedSignal)

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

    def get_countDownTimer(self):
        return self._countDownTimer

    def set_countDownTimer(self, v: int):
        self._countDownTimer = v
        self.changedSignal.emit()

    countDownTimer = Property(int, get_countDownTimer, set_countDownTimer, notify=changedSignal)

    def get_basketIsFull(self):
        return self._basketIsFull

    def set_basketIsFull(self, v: bool):
        self._basketIsFull = v
        self.changedSignal.emit()

    basketIsFull = Property(bool, get_basketIsFull, set_basketIsFull, notify=changedSignal)

    def get_basketLoad(self):
        return self._basketLoad

    def set_basketLoad(self, v: int):
        self._basketLoad = v
        self.changedSignal.emit()

    basketLoad = Property(int, get_basketLoad, set_basketLoad, notify=changedSignal)

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
            product = self._productRepository.get_product(self._scanner.get_barcode())
            if product.price == 0:
                validProduct = False
            else:
                validProduct = True

            if validProduct:
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
                        self.openPopupMessageTimerSignal.emit("Not valid Product !")
                else:
                    self.openPopupMessageTimerSignal.emit("Basket is full !")

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
                        self._suggestedList = self._productRepository.get_suggesstionProducts(product.barcode)
                        self.showNewProductScannedSignal.emit()
                        self.hideTopBtnSignal.emit()
                    else:
                        self.openPopupMessageTimerSignal.emit("Not valid Product !")

            elif self.state == 5:
                isAcceptablebarcodeForRemove, self._canRemoveProductClick, removeSuccessfullyBefore = self._removeList.updateValidBarcodeSetForRemove(
                    product)

                if not isAcceptablebarcodeForRemove:
                    if removeSuccessfullyBefore:
                        self.openPopupMessageTimerSignal.emit("Please scan other product that removed from basket !")
                    else:
                        self.openPopupMessageTimerSignal.emit("ONLY scan product that removed from basket, please.")

                self._trustUser = False
                if len(self._removeList.m_data) == 1:
                    self.openPopupDeleteProductSignal.emit()

            elif self.state == 8:
                self.openPopupMessageTimerSignal.emit("Can't add product at this session.")

    @Slot(int)
    def read_startWeight(self, startWeight: int):
        if abs(startWeight) > 20:
            self.state = -1
            self._basketWeightShouldBe = 0
            self.openPopupMessageSignal.emit("Please clear the cart !")
        else:
            self._basketWeightShouldBe = 0

    @Slot(int, int)
    def basketWeightChanged(self, val2: int, val1: int):
        if not self._inByPass:
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
                            insertSound()
                            self._factorList.insertProduct(self.newProduct, 1)
                            self._bypassList.insertProduct(self.newProduct.copy_product(), 1)
                            self.cal_basketLoad(val2)
                            self._basketWeightShouldBe = val2
                            self.countDownTimer = -1

                            # self._productsmodel.updateWeight(self.getNewProduct(), val2 - val1)

                        else:
                            self._shouldBarcodeToBeScannToAddProduct = True
                            self.openPopupNoBarcodeScannedSignal.emit()
                            if abs(value) > 20:
                                notifSound()
                                pass
                            self._basketWeightShouldBe = val1
                            self.state = 4

                    else:
                        self.openPopupNoBarcodeScannedSignal.emit()
                        if abs(value) > 20:
                            notifSound()
                            pass
                        self._basketWeightShouldBe = val1
                        self.state = 4

                elif self.state == 2:
                    if self.newProduct.insertedWeight < self._validInsertedWeightForCalTol:
                        insertSound()
                        self._productRepository.updateProduductWeight(self.newProduct, val2 - val1)
                        self._factorList.insertProduct(self.newProduct, 1)
                        self._bypassList.insertProduct(self.newProduct.copy_product(), 1)
                        if self.newProduct.meanWeight > self._lightestWeightForHeavyProduct + self._weightSensor.acceptable_tolerance:
                            self._weightSensor.lightest_weight = self._lightestWeightForHeavyProduct
                        self.state = 1
                        self._basketWeightShouldBe = val2
                        self.clear_stackView()
                        self.countDownTimer = -11
                        self._shouldBarcodeToBeScannToAddProduct = True

                    else:
                        if (value < self.newProduct.meanWeight + self.newProduct.tolerance) and (
                                value >= self.newProduct.meanWeight - self.newProduct.tolerance):
                            insertSound()
                            self._productRepository.updateProduductWeight(self.newProduct, val2 - val1)
                            self._factorList.insertProduct(self._newProduct, 1)
                            self._bypassList.insertProduct(self._newProduct, 1)
                            if self.newProduct.meanWeight > self._lightestWeightForHeavyProduct + self._weightSensor.acceptable_tolerance:
                                self._weightSensor.lightest_weight = self._lightestWeightForHeavyProduct
                            self.state = 1
                            self._basketWeightShouldBe = val2
                            self.clear_stackView()
                            self.countDownTimer = -1
                            self._shouldBarcodeToBeScannToAddProduct = False
                        else:
                            self.openPopupWeightNotMatchWithBarcodeSignal.emit()
                            notifSound()
                            self._basketWeightShouldBe = val1
                            self.state = 3

                elif self.state == 3:
                    if self._basketWeightShouldBe - self._basketWeightTolerance <= val2 <= self._basketWeightShouldBe + self._basketWeightTolerance:
                        self._basketWeightShouldBe = val2
                        self.state = 1
                        self.closePopupWeightNotMatchWithBarcodeSignal.emit()
                        self.clear_stackView()
                    else:
                        self.openPopupMessageTimerSignal.emit("please remove not scanned product !")
                        notifSound()

                elif self.state == 4:
                    if self._basketWeightShouldBe - self._basketWeightTolerance <= val2 <= self._basketWeightShouldBe + self._basketWeightTolerance:
                        self._basketWeightShouldBe = val2
                        self.closePopupNoBarcodeScannedSignal.emit()
                        self.state = 1
                        self.clear_stackView()
                    elif self._basketWeightShouldBe + self._basketWeightTolerance <= val2:
                        self.openPopupMessageTimerSignal.emit(
                            "please remove not scanned products and then insert them one by one !")
                        notifSound()

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
                            "please remove inserted product from basket and first complete remove process and then insert product!")
                        notifSound()
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
                    self.openPopupMessageSignal.emit("Cant add or remove product in this session.")
                    self._basketWeightShouldBe = val1
                    self.state = 9
                    notifSound

                elif self.state == 9:
                    if self._basketWeightShouldBe - self._basketWeightTolerance <= val2 <= self._basketWeightShouldBe + self._basketWeightTolerance:
                        self.state = 8
                        self.closePopupMessageSignal.emit()

                elif self.state == 10:
                    self.openPopupMessageSignal.emit("Cant add or remove product in this session.")
                    self._basketWeightShouldBe = val1
                    self.state = 11
                    notifSound()

                elif self.state == 11:
                    if self._basketWeightShouldBe - self._basketWeightTolerance <= val2 <= self._basketWeightShouldBe + self._basketWeightTolerance:
                        self.state = 10
                        self.closePopupMessageSignal.emit()

                elif self.state == 12:
                    if abs(val2 - self._basketWeightShouldBe) > 50:
                        # self._basketWeightShouldBe = val1
                        self.turn_offGreenlight()
                        self.openPopupMessageSignal.emit("Cant add or remove product in this session.")
                        self.state = 13

                elif self.state == 13:
                    if self._basketWeightShouldBe - self._basketWeightTolerance <= val2 <= self._basketWeightShouldBe + self._basketWeightTolerance:
                        self.state = 12
                        self._basketWeightShouldBe = val2
                        self.closePopupMessageSignal.emit()
                        self.turn_onGreenLight()

                elif self.state == 14:
                    self.newProduct.set_productWeightInBasket(val2 - self._pluStartWeight)

            # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
            # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> REMOVE WEIGHT <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
            # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
            if val2 < val1:
                if self.state == -1:
                    if self._basketWeightShouldBe - self._basketWeightTolerance <= val2 <= self._basketWeightShouldBe + self._basketWeightTolerance:
                        self.state = 1
                        self.closePopupMessageSignal.emit()

                elif self.state == 1:
                    self._removeList.validBarcodeSetForRemove(self._factorList.m_data, abs(value))
                    if not len(self._removeList.m_validBarcodeSetForDelete) == 0:
                        self.openPopupDeleteProductSignal.emit()
                        notifSound2()
                        self._basketWeightShouldBe = val1
                        self.state = 5

                elif self.state == 2:
                    self._removeList.validBarcodeSetForRemove(self._factorList.m_data, abs(value))
                    self.clear_stackView()
                    self.openPopupDeleteProductSignal.emit()
                    notifSound2()
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
                        "Please replace product that removed from basket and after complete current remove process, remove another product !")
                    notifSound()
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
                    self.openPopupMessageSignal.emit("Cant add or remove product in this session.")
                    self._basketWeightShouldBe = val1
                    self.state = 9
                    notifSound()

                elif self.state == 9:
                    if self._basketWeightShouldBe - self._basketWeightTolerance <= val2 <= self._basketWeightShouldBe + self._basketWeightTolerance:
                        self.state = 8
                        self.closePopupMessageSignal.emit()

                elif self.state == 10:
                    self.openPopupMessageSignal.emit("Cant add or remove product in this session.")
                    self._basketWeightShouldBe = val1
                    self.state = 11
                    notifSound()

                elif self.state == 11:
                    if self._basketWeightShouldBe - self._basketWeightTolerance <= val2 <= self._basketWeightShouldBe + self._basketWeightTolerance:
                        self.state = 10
                        self.closePopupMessageSignal.emit()

                elif self.state == 12:
                    if abs(val2 - self._basketWeightShouldBe) > 50:
                        # self._basketWeightShouldBe = val1
                        self.openPopupMessageSignal.emit("Cant add or remove product in this session.")
                        self.turn_offGreenlight()
                        self.state = 13

                elif self.state == 13:
                    if self._basketWeightShouldBe - self._basketWeightTolerance <= val2 <= self._basketWeightShouldBe + self._basketWeightTolerance:
                        self.state = 12
                        self._basketWeightShouldBe = val2
                        self.closePopupMessageSignal.emit()
                        self.turn_onGreenLight()

                elif self.state == 14:
                    self.newProduct.set_productWeightInBasket(val2 - self._pluStartWeight)

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
        if not self._inByPass:
            self._inByPass = True
            self.clear_stackView()
            self.closeAllPopUpSignal.emit()
            self.openPopupByPassSignal.emit()

    @Slot()
    def nfc_read(self):
        if self.state == 10:
            self.state = 12
            self.showAfterPaymentSignal.emit()
            self.turn_onGreenLight()

    ####################################################################################################### UI Sluts ###
    @Slot()
    def call_forHelpClicked(self):
        playSound("notif")

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
        if self.state == 1 or self.state == 5:
            self.showManualBarcodeSignal.emit()
            self.hideTopBtnSignal.emit()

    @Slot()
    def cancel_manualBarcodeClicked(self):
        if self.state == 1:
            self.clear_stackView()
        elif self.state == 5:
            self.closeTopStackViewSignal.emit()

    @Slot(str)
    def confirm_manualBarcodeClicked(self, barcode: str):
        print(barcode)
        if self.state == 1:
            if len(barcode) == self._scanner.get_productBarcodeLength():
                if self._productRepository.get_product(barcode).price != 0:
                    self.clear_stackView()
                    self._scanner._barcode = barcode
                    self.barcodeRead()
                else:
                    self.openPopupMessageTimerSignal.emit("Please check entered barcode !")
            else:
                self.openPopupMessageTimerSignal.emit(
                    "please enter " + str(self._scanner.get_productBarcodeLength()) + " digits barcode !")
        elif self.state == 5:
            if len(barcode) == self._scanner.get_productBarcodeLength():
                self.closeTopStackViewSignal.emit()
                self._scanner.barcode = barcode
                self.barcodeRead()
            else:
                self.openPopupMessageTimerSignal.emit(
                    "please enter " + str(self._scanner.get_productBarcodeLength()) + " digits barcode !")

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
            self.state = 1

    @Slot(str)
    def item_PLUClicked(self, pluCode: str):
        self.newProduct = self._productRepository.get_product(pluCode)
        if self.newProduct.get_productType() == "weighted":
            self.state = 14
            self.showWeightedPLUItemsSignal.emit()
            self.openPopupMessageSignal.emit("Taring ! Please don't move basket.")
            taring = True
            while taring:
                if self._weightSensor._canread:
                    self._pluStartWeight = self._weightSensor._BasketWeight2
                    taring = False
            self.closePopupMessageSignal.emit()
        elif self.newProduct.get_productType() == "counted":
            self.state = 15
            self.showCountedPLUItemsSignal.emit()

    @Slot()
    def confirm_PLUItemClicked(self):
        if self.state == 14:
            if self._weightSensor.isstable:
                self._factorList.insertProduct(self.newProduct, 1)
                self._bypassList.insertProduct(self.newProduct.copy_product(), 1)
                self.state = 1
                self.clear_stackView()
                self._basketWeightShouldBe = self._pluStartWeight + self.newProduct.productWeightInBasket
                self.cal_basketLoad(self._basketWeightShouldBe)
                insertSound()
            else:
                self.openPopupMessageTimerSignal.emit("Please wait !")
        elif self.state == 15:
            if self._weightSensor.isstable:
                self._factorList.insertProduct(self.newProduct, self.newProduct.countInBasket)
                self._bypassList.insertProduct(self.newProduct.copy_product(), self.newProduct.countInBasket)
                self.state = 1
                self.clear_stackView()
                self._basketWeightShouldBe = self._weightSensor.readbasketweight()
                self.cal_basketLoad(self._basketWeightShouldBe)
                insertSound()
            else:
                self.openPopupMessageTimerSignal.emit("Please wait !")

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
            deleteSound()
            self._canRemoveProductClick = False
            self._factorList.removeProducts(self._removeList.m_data)
            self._bypassList.removeProductsUpdateBypass(self._removeList.m_data)
            self._removeList.clearData()
            self.state = 1
            self._trustUser = False
            self.closePopupDeleteProductSignal.emit()
            self.clear_stackView()

        else:
            if not self._canRemoveProductClick:
                notifSound2()
                self.openPopupMessageTimerSignal.emit("Please scann all product that remove from basket !")
                self._trustUser = True
            else:
                deleteSound()
                self._canRemoveProductClick = False
                self._factorList.removeProducts(self._removeList.m_data)
                self._bypassList.removeProductsUpdateBypass(self._removeList.m_data)
                self._removeList.clearData()
                self.state = 1
                self._trustUser = False
                self.closePopupDeleteProductSignal.emit()
                self.clear_stackView()

    @Slot(str)
    def product_removeManualBarcodeEntered(self, barcode: str):
        pass

    @Slot(int)
    def product_removeIncreaseClicked(self, index: int):
        pass

    @Slot(int)
    def product_removeDecreaseClicked(self, index: int):
        pass

    @Slot()
    def accept_byPassClicked(self):
        if self._weightSensor.isstable:
            self._factorList.clearData()
            self._factorList.insert_productList(self._bypassList.m_data)
            self.state = 1
            self.clear_stackView()
            self._inByPass = False
            self.closeAllPopUpSignal.emit()

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
            self.openPopupMessageTimerSignal.emit("Please Wait !")

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
                self.state = 8
                self.showCheckOutSignal.emit()
            else:
                self.openPopupMessageTimerSignal.emit("Yor factor is empty !")

    @Slot()
    def checkout_backClicked(self):
        if self.state == 8:
            self.state = 1
            self.clear_stackView()

    @Slot(str)
    def apply_couponCode(self, code):
        if code == "2212":
            self.factorList.set_offerCouponPercentage(10.0)
        else:
            self.openPopupMessageTimerSignal.emit("Invalid code, please check the code !")

    @Slot()
    def payment_clicked(self):
        if self.state == 8:
            self.showPaymentSignal.emit(0)
            self.state = 10
            self._nfc = nfc()
            self._nfc.nfcReaderSignal.connect(self.nfc_read)

    @Slot()
    def payment_viaQRClicked(self):
        if self.state == 8:
            self.showPaymentSignal.emit(1)
            self.state = 10

    @Slot()
    def payment_QRClicked(self):   # this ia a demo for payment through Qr code
        if self.state == 10:
            self.state = 12
            self.showAfterPaymentSignal.emit()
            self.turn_onGreenLight()

    @Slot()
    def payment_backClicked(self):
        if self.state == 10:
            self.state = 8

    @Slot(str)
    def send_factorEmailClicked(self, emailAddress: str):
        try:
            v = validate_email(emailAddress)
            email = v["email"]
            print(email)
        except EmailNotValidError as e:
            print(str(e))
            self.openPopupMessageTimerSignal.emit(str(e))


    ###################################################################################################### Functions ###
    def print_states(self):
        if self.state == -1:
            print("\nState " + str(self._states) + " : Start with weight in basket or out of calibrate.\n")
        elif self.state == 1:
            print("\nState " + str(self._states) + " : Stable.\n")
        elif self.state == 2:
            print("\nState " + str(self._states) + " : A Barcode was read and waiting for Weight to add.\n")
        elif self.state == 3:
            print("\nState " + str(self._states) + " : Inserted Weight not match with read Barcode.\n")
        elif self.state == 4:
            print("\nState " + str(
                self._states) + " : Inserted Weight without barcode.(match with last product or non valid insert weight)\n")
        elif self.state == 5:
            print("\nState " + str(self._states) + " : Weight removed. waiting to read barcode\n")
        elif self.state == 6:
            print("\nState " + str(self._states) + " : Insert Invalid Weight While Remove Product.\n")
        elif self.state == 7:
            print("\nState " + str(self._states) + " : 1+ steps removed Weight.\n")
        elif self.state == 8:
            print("\nState " + str(self._states) + " : checkout clicked.\n")
        elif self.state == 9:
            print("\nState " + str(self._states) + " : weight change in checkout.\n")
        elif self.state == 10:
            print("\nState " + str(self._states) + " : waiting for payment in payment page.\n")
        elif self.state == 11:
            print("\nState " + str(self._states) + " : weight change while waiting for payment.\n")
        elif self.state == 12:
            print("\nState " + str(self._states) + " : go to after payment page after successful payment.\n")
        elif self.state == 13:
            print("\nState " + str(self._states) + " : weight change after payment.\n")
        elif self.state == 14:
            print("\nState " + str(self._states) + " : weighted PLU product selected.\n")
        elif self.state == 15:
            print("\nState " + str(self._states) + " : counted PLU product selected.\n")

    def add_productToFactor(self, p: Product, c: int, u: bool, w2: int, w1: int):
        insertSound()
        self._factorList.insertProduct(p, c)
        self._bypassList.insertProduct(p.copy_product(), c)
        if u:
            # self._factorList.updateWeight(p, w2 - w1)
            print("------------------------->update ?")
        self._basketWeightShouldBe = w2
        self.cal_basketLoad(w2)

    def cal_basketLoad(self, weight: int):
        load = int((weight - self._startWeight) / self._basketWeightLimit * 100)
        load = min(max(load, 0), 100)
        self.set_basketLoad(load)
        self.set_basketIsFull(True) if load == 100 else self.set_basketIsFull(False)

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

