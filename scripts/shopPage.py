import os
import sys
import time
from time import sleep
from threading import Thread

from PySide2.QtCore import QObject, Signal, Property, Slot

from Models.product import Product
from Models.Helpers.productModel import ProductModel
from Models.user import User
from Models.serverUser import ServerUser

from Services.dal import DAL
from Services.sound import *
from Services.gpio import GreenLight
from Services.weightsensor import WeightSensorWorker

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
    _state: int = 0
    _countDownTimer: int = -60
    _startWeight: int = 0
    _basketWeightShouldBe: int = 0
    _basketWeightRemoveProcces: int = 0
    _basketLoad: int = 0
    _stackViewDepth: int
    _basketIsFull: bool = False
    _inByPass: bool = False
    _loginFinished: bool = False
    _startProcess: bool = False
    _manualBarcodeEntered: bool = False
    _canRemoveProductClick: bool = False
    _trustUser: bool = False
    _shouldBarcodeToBeScannToAddProduct: bool = True
    _lightWeightProductExistInBasket: bool = False
    _initFactorListFlag: bool = False

    ######################################################################################################## Modules ###
    # _scanner: ScannerHelper
    _weightSensor: WeightSensorWorker

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
        self._scanner.loyaltyCardBarcodeReadSignal.connect(self.read_loyaltyCardBarcode)
        self._scanner.IDBarcodeReadSignal.connect(self.test)
        # self._scanner.start()

        #### WeightSensor #########################################
        self._weightSensor = WeightSensorWorker()
        self._weightSensor.basketweight_changed.connect(self.basketWeightChanged)
        self._weightSensor.start()

        # self._weightSensor = WeightSensorHelper()
        # self._weightSensor.stepBasketWeightChangedSignal.connect(self.basketWeightChanged)

        #### Models ###############################################
        self._newProduct = Product()
        self._factorList = ProductModel()
        self._offersList = ProductModel()
        self._offersList.insert_productList(self._productRepository.get_offerProducts())
        self._offerTopTen = ProductModel()
        self._offerTopTen.insert_productList(self._productRepository.get_topOfferProducts())
        self._suggestedList = ProductModel()
        self._pluList = ProductModel()
        self._pluTopFour = ProductModel()
        plus = self._productRepository.get_pluProducts()
        self._pluList.insert_productList(plus)
        if len(plus) > 4:
            self._pluTopFour.insert_productList(plus[:4])
        else:
            self._pluTopFour.insert_productList(plus)

        self._bypassList = ProductModel()
        self._removeList = ProductModel()

        #### User #################################################
        self._user = user

        #### Insert Timer Thread ##################################
        self._canTimerTick = True
        self._timerThread = Thread(target=self.timerSlot)
        self._timerThread.start()

        ###########################################################

    ######################################################################################################## Signals ###
    changedSignal = Signal()
    successfulLoginSignal = Signal()
    closeAllPopUpSignal = Signal()
    hideOfferListSignal = Signal()
    # visibleProductListDeleteSignal = Signal()

    # showStartUpShoppingLabelSignal = Signal(bool)
    initFactorListSignal = Signal()

    openPopupMessageTimerSignal = Signal(str)
    clodePopUpMessageTimer = Signal()

    openPopupMessageSignal = Signal(str)
    closePopupMessageSignal = Signal()

    showNewProductScannedSignal = Signal()  # pop up new product scanned
    # closeNewProductScannedSignal = Signal()

    # closeNewStackViewHandlerSignal = Signal()
    closeTopStackViewSignal = Signal()  # close top stack view. maybe used for several purpose like close new product scanned stack view

    openPopupWeightNotMatchWithBarcodeSignal = Signal()  # pop up weight not match with scanned barcode
    closePopupWeightNotMatchWithBarcodeSignal = Signal()

    openPopupNoBarcodeScannedSignal = Signal()
    closePopupNoBarcodeScannedSignal = Signal()  # add product to basket with out scanning barcode

    openPopupDeleteProductSignal = Signal()  # remove product from basket
    closePopupDeleteProductSignal = Signal()

    openPopUpMessageNotAllowedChangeWeightSignal = Signal()  # change weifgt at the end of shopping
    closePopUpMessageNotAllowedChangeWeightSignal = Signal()

    ##################################################################################################### Properties ###
    def get_state(self):
        return self._state

    def set_state(self, state: int):
        self._state = state
        print("state: " + str(state))
        if state == 1 or state == 8:
            # self.clearStackView()
            self.closeAllPopUpSignal.emit()
            self.turn_offGreenlight()
        elif state == 10:
            self.turn_onGreenLight()
        else:
            self.turn_offGreenlight()

        # self._logStash.newChangeState(
        #     self._datetime.time, self._states, self._userID)

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
        self._shouldBarcodeToBeScannToAddProduct = True
        if not self._inByPass:
            # self.hideOfferListSignal.emit()
            product = self._productRepository.get_product(self._scanner.get_barcode())

            self._bypassList.insertProduct(product.copy_product(), 0)

            if self.state == 1:
                if not self.basketIsFull:
                    # self.adjust_wightSensorSensitivity(product.meanWeight)
                    self.state = 2
                    self.newProduct = product
                    self.countDownTimer = self._insertProductTime + self._timerOffset
                    self._suggestedList.insert_productList(
                        self._productRepository.get_suggesstionProducts(product.barcode))
                    self.showNewProductScannedSignal.emit()

                    if self._manualBarcodeEntered:
                        self._manualBarcodeEntered = False

                else:
                    pass  # pop up message timer basket is full

            elif self.state == 2:
                if self.newProduct.barcode == self._scanner.get_barcode():
                    if 0 <= self.countDownTimer < self._timerOffset:
                        self.showNewProductScannedSignal.emit()
                        self.countDownTimer = self._insertProductTime
                    else:
                        self.countDownTimer = self._insertProductTime



                else:
                    self.newProduct = product
                    self.adjust_wightSensorSensitivity(product.meanWeight)
                    self.countDownTimer = self._insertProductTime
                    self._suggestedList = self._productRepository.get_suggesstionProducts(product.barcode)
                    self.showNewProductScannedSignal.emit()

            elif self.state == 5:
                isAcceptablebarcodeForRemove, self._canRemoveProductClick, removeSuccessfullyBefore = self._removeList.updateValidBarcodeSetForRemove(
                    product)

                if not isAcceptablebarcodeForRemove:
                    if removeSuccessfullyBefore:
                        pass  # pop up timer "لطفا سایر کالاهایی که از سبد خارج کرده اید را جلوی بارکد خوان بگیرید"
                    else:
                        pass  # pop up timer "لطفا فقط کالایی که از سبد خارج کرده اید را جلوی بارکد خوان بگیرید"
                else:
                    pass
                self._trustUser = False
                # if len(self._removeList.m_data) == 1:
                #     self.openPopupDeleteProductSignal.emit()

    @Slot(int, int)
    def basketWeightChanged(self, val2: int, val1: int):
        print(val1, val2)
        if not self._inByPass:
            self.hideOfferListSignal.emit()
            value: int = val2 - val1
            # self._logStash.newChangeWeight(self._datetime.time, value, self._userID)

            # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ADD WEIGHT <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
            if val2 >= val1:
                if self.state == 1:
                    if not self._shouldBarcodeToBeScannToAddProduct:
                        if ((value < self.newProduct.meanWeight + self.newProduct.tolerance) and (
                                value >= self.newProduct.meanWeight - self.newProduct.tolerance)):
                            # insertSound()
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
                                # notifSound()
                                pass
                            self._basketWeightShouldBe = val1
                            self.state = 4

                    else:
                        self.openPopupNoBarcodeScannedSignal.emit()
                        if abs(value) > 20:
                            # notifSound()
                            pass
                        self._basketWeightShouldBe = val1
                        self.state = 4

                elif self.state == 2:
                    if self.newProduct.insertedWeight < self._validInsertedWeightForCalTol:
                        # insertSound()
                        self._factorList.insertProduct(self.newProduct, 1)
                        self._bypassList.insertProduct(self.newProduct.copy_product(), 1)

                        # self._productsmodel.updateWeight(self.getNewProduct(), val2 - val1)

                        # self.check_productWeight(self.newProduct) <---------------- usable when update product
                        if (
                                val2 - val1) <= self._lightestWeightForHeavyProduct + self._weightSensor.acceptable_tolerance:
                            self._lightWeightProductExistInBasket = True

                        self.adjust_wightSensorSensitivity(val2 - val1)
                        self.state = 1
                        self._basketWeightShouldBe = val2
                        self.closeTopStackViewSignal.emit()
                        self.countDownTimer = -11
                        self._shouldBarcodeToBeScannToAddProduct = True
                        if not self._initFactorListFlag:
                            self.initFactorListSignal.emit()
                            self._initFactorListFlag = True

                    else:
                        if (value < self.newProduct.meanWeight + self.newProduct.tolerance) and (
                                value >= self.newProduct.meanWeight - self.newProduct.tolerance):
                            # insertSound()

                            # self.showStartUpShoppingLabelSignal.emit(False)
                            self._factorList.insertProduct(self._newProduct, 1)
                            self._bypassList.insertProduct(self._newProduct, 1)

                            # self._productsmodel.updateWeight(self.getNewProduct(), val2 - val1)

                            # self.check_productWeight(self._newProduct)

                            # if self.getNewProduct().getAvgWeight() > self._lightest_weight_for_heavy_weight_product + self._weighsensor.acceptable_tolerance:
                            #     self._weighsensor.lightest_weight = self._lightest_weight_for_heavy_weight_product
                            self.state = 1
                            self._basketWeightShouldBe = val2
                            self.closeTopStackViewSignal.emit()
                            self.countDownTimer = -1
                            self._shouldBarcodeToBeScannToAddProduct = False
                            if not self._initFactorListFlag:
                                self.initFactorListSignal.emit()
                                self._initFactorListFlag = True

                        else:
                            self.openPopupWeightNotMatchWithBarcodeSignal.emit()
                            # notifSound()
                            self._basketWeightShouldBe = val1
                            self.state = 3

                elif self.state == 3:
                    if self._basketWeightShouldBe - self._basketWeightTolerance <= val2 <= self._basketWeightShouldBe + self._basketWeightTolerance:
                        self._basketWeightShouldBe = val2
                        self.state = 2
                        self.closePopupWeightNotMatchWithBarcodeSignal.emit()
                    else:
                        pass  # "لطفا کالایی که بدون اسکن کردن در سبد قرار داده اید را از آن خارج کنید."
                        # notifSound()

                elif self.state == 4:
                    if self._basketWeightShouldBe - self._basketWeightTolerance <= val2 <= self._basketWeightShouldBe + self._basketWeightTolerance:
                        self._basketWeightShouldBe = val2
                        self.closePopupNoBarcodeScannedSignal.emit()
                        self.state = 1
                    elif self._basketWeightShouldBe + self._basketWeightTolerance <= val2:
                        self.openPopupMessageTimerSignal.emit(
                            "لطفا کالایی که بدون اسکن کردن در سبد قرار داده اید را از سبد خارج کرده و مجددا اقدام به اضافه کردن یک به یک آن ها کنید.")
                        # notifSound()

                elif self.state == 5:
                    if self._basketWeightShouldBe - self._basketWeightTolerance <= val2 <= self._basketWeightShouldBe + self._basketWeightTolerance:
                        self._basketWeightShouldBe = val2
                        self.closePopupDeleteProductSignal.emit()
                        self.state = 1
                        self._removeList.clearData()
                        self._trustUser = False
                    else:
                        self.openPopupMessageSignal.emit(
                            "لطفا کالایی که در سبد قرار داده اید را برداشته و فرآیند حذف را کامل کنید. سپس اقدام به اضافه کردن کالای مورد نظر کنید")
                        # notifSound()
                        self.state = 6
                        self._basketWeightRemoveProcces = val1

                elif self.state == 6:
                    if self._basketWeightShouldBe - self._basketWeightTolerance <= val2 <= self._basketWeightShouldBe + self._basketWeightTolerance:
                        self._basketWeightShouldBe = val2
                        self.state = 1
                        self.closePopupMessageSignal.emit()
                        self.closePopupDeleteProductSignal.emit()
                    elif self._basketWeightRemoveProcces - self._basketWeightTolerance <= val2 <= self._basketWeightRemoveProcces + self._basketWeightTolerance:
                        self._basketWeightRemoveProcces = val2
                        self.state = 5
                        self.closePopupMessageSignal.emit()

                elif self.state == 7:
                    if self._basketWeightRemoveProcces - self._basketWeightTolerance <= val2 <= self._basketWeightRemoveProcces + self._basketWeightTolerance:
                        self._basketWeightRemoveProcces = val2
                        self.state = 5
                        self.closePopupMessageSignal.emit()
                    elif self._basketWeightShouldBe - self._basketWeightTolerance <= val2 <= self._basketWeightShouldBe + self._basketWeightTolerance:
                        self._basketWeightShouldBe = val2
                        self.state = 1
                        self.closePopupMessageSignal.emit()
                        self.closePopupDeleteProductSignal.emit()
                        self._removeList.clearData()
                        self._trustUser = False

                elif self.state == 8:
                    if self._basketWeightShouldBe - self._basketWeightTolerance <= val2 <= self._basketWeightShouldBe + self._basketWeightTolerance:
                        self._basketWeightShouldBe = val2
                        self.state = 1
                    else:
                        self.state = 9
                        self._basketWeightShouldBe = val1
                        self.openPopUpMessageNotAllowedChangeWeightSignal.emit()

                #         if not self._paymentCartScanned:
                #             if abs(val2 - self._basketWeightShouldBe) >= 100:
                #                 self.state = 9
                #                 self.openPopUpMessageNotAllowedChangeWeight.emit()
                #                 notifSound()
                #                 self._basketWeightShouldBe = val1

                elif self.state == 9:
                    if self._basketWeightShouldBe - self._basketWeightTolerance <= val2 <= self._basketWeightShouldBe + self._basketWeightTolerance:
                        self._basketWeightShouldBe = val2
                        self.state = 1
                        self.closePopupWeightNotMatchWithBarcodeSignal.emit()

            # # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
            # # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> REMOVE WEIGHT <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
            # # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

            if val2 < val1:
                if self.state == 1:
                    self._removeList.validBarcodeSetForRemove(self._factorList.m_data, abs(value))
                    if not len(self._removeList.m_validBarcodeSetForDelete) == 0:
                        self.openPopupDeleteProductSignal.emit()
                        # notifSound2()
                        self._basketWeightShouldBe = val1
                        self.state = 5

                elif self.state == 2:
                    self._removeList.validBarcodeSetForRemove(self._factorList.m_data, abs(value))
                    self.openPopupDeleteProductSignal.emit()
                    # notifSound2()
                    self._basketWeightShouldBe = val1
                    self.countDownTimer = -20
                    self.closeTopStackViewSignal.emit()
                    self.state = 5

                elif self.state == 3:
                    if self._basketWeightShouldBe - self._basketWeightTolerance <= val2 < self._basketWeightShouldBe + self._basketWeightTolerance:
                        self._basketWeightShouldBe = val2
                        self.closePopupWeightNotMatchWithBarcodeSignal.emit()
                        # self.closeTopStackViewSignal.emit()
                        self.state = 2

                elif self.state == 4:
                    if self._basketWeightShouldBe - self._basketWeightTolerance <= val2 <= self._basketWeightShouldBe + self._basketWeightTolerance:
                        self._basketWeightShouldBe = val2
                        self.closePopupNoBarcodeScannedSignal.emit()
                        self.state = 1

                elif self.state == 5:
                    self.openPopupMessageSignal.emit(
                        "لطفا کالایی که از سبد برداشته اید در سبد قرار دهید و پس از اتمام فرآید حذف کالای قبلی مجددا اقدام به حذف آن کالا کنید")
                    # notifSound()
                    self.state = 7
                    self._basketWeightRemoveProcces = val1

                elif self.state == 6:
                    if self._basketWeightRemoveProcces - self._basketWeightTolerance <= val2 <= self._basketWeightRemoveProcces + self._basketWeightTolerance:
                        self._basketWeightRemoveProcces = val2
                        self.state = 5
                        self.closePopupMessageSignal.emit()

                elif self.state == 7:
                    if self._basketWeightShouldBe - self._basketWeightTolerance <= val2 <= self._basketWeightShouldBe + self._basketWeightTolerance:
                        self._basketWeightShouldBe = val2
                        self.state = 1

                elif self.state == 8:
                    self.state = 9
                    self.openPopUpMessageNotAllowedChangeWeightSignal.emit()
                    # notifSound()
                    self._basketWeightShouldBe = val1

                    # if not self._paymentCartScanned:
                    #     if abs(value) >= 100:
                    #         self.state = 9
                    #         self.openPopUpMessageNotAllowedChangeWeight.emit()
                    #         notifSound()
                    #         self._basketweightShouldBe = val1

                elif self.state == 9:
                    # if abs(value) >= 30:
                    if self._basketWeightShouldBe - self._basketWeightTolerance <= val2 <= self._basketWeightShouldBe + self._basketWeightTolerance:
                        self._basketWeightShouldBe = val2
                        self.closePopUpMessageNotAllowedChangeWeightSignal.emit()
                        self.state = 8
                        # if self._successfulPayment:
                        #     self.state =10
                        #     self.showAfterPayment.emit()
                        # else:
                        #     self.state = 8

            #     elif self.state == 10:
            #         # if abs(val2 - val1) >= 50:
            #         #     self.state = 11
            #         #     self._basketweightShouldBe = val1
            #         #     self.openPopupFullMessageTimer.emit(
            #         #         "در صورتی که بازرس خروج شما را تایید کرده است، محصولات را از سبد خارج کنید!")
            #         #     # notifSound()
            #         pass
            #
            #     elif self.state == 11:
            #         # if abs(val2 - val1) >= 30:
            #         #     if self._basketweightShouldBe - self._basketWeightTolerance <= val2 <= self._basketweightShouldBe + self._basketWeightTolerance:
            #         #         self.state = 10
            #         #         self._basketweightShouldBe = val2
            #         #         self.closePopUpMessageNotAllowedToAddProduct.emit()
            #         pass

    @Slot()
    def timerSlot(self):
        while self._canTimerTick:
            if self.state == 2 or self.state == 1:
                self.countDownTimer = self.countDownTimer - 1
                sleep(1)
                print("timer: " + str(self.countDownTimer))
            if self.countDownTimer == self._timerOffset:
                if self.state == 2:
                    self.closeTopStackViewSignal.emit()
                    print("close")
                    # print("close stack view emit")
                    # sleep(1)
            if self.countDownTimer == 0:
                if self.state == 2:
                    self.state = 1
                    # self.clearStackView()
                    # self.closeAllPopUps.emit()
                    # self.turn_offGreenlight()
                    self._shouldBarcodeToBeScannToAddProduct = True
                    # self._weighsensor.lightest_weight = self._lightest_weight_for_heavy_weight_product
            if self.countDownTimer == -10:
                if self.state == 1:
                    self._shouldBarcodeToBeScannToAddProduct = True
                    # self._weighsensor.lightest_weight = self._lightest_weight_for_heavy_weight_product

    @Slot(str)
    def enter_phoneNumberClicked(self, phoneNumber: str):
        serverUser = self._userServerRepository.loginByPhone(phoneNumber)
        if not serverUser.get_id() == "":
            self._user.set_loggedInUser(serverUser)
            self.successfulLoginSignal.emit()
            self.login_finished()

        else:
            pass  # pop up nat valid phone number

    @Slot()
    def read_loyaltyCardBarcode(self):
        serverUser = self._userServerRepository.loginByloyalityBarcode(self._scanner.get_loyaltyCardBarcode())
        if not serverUser.get_id() == "":
            self._user.set_loggedInUser(serverUser)
            self.successfulLoginSignal.emit()
            self.login_finished()

        else:
            pass  # pop up timer

    @Slot(str)
    def enter_loyaltyCardBarcode(self, loyaltyCode: str):
        serverUser = self._userServerRepository.loginByloyalityBarcode(loyaltyCode)
        if not serverUser.get_id() == "":
            self._user.set_loggedInUser(serverUser)
            self.successfulLoginSignal.emit()
            self.login_finished()
        else:
            pass  # pop up timer

    @Slot()
    def login_finished(self):
        self.set_state(1)

    @Slot(int)
    def stackview_depthChanged(self, Depth: int):
        self._stackViewDepth = Depth

    @Slot()
    def productRemoveClicked(self):
        if self._trustUser:
            self.closePopupDeleteProductSignal.emit()
            # deleteSound()
            self._canRemoveProductClick = False
            self._factorList.removeProducts(self._removeList.m_data)
            print(len(self._removeList.m_data))
            self._bypassList.removeProductsUpdateBypass(self._removeList.m_data)
            self._removeList.clearData()
            self.state = 1
            self._trustUser = False
        else:
            if not self._canRemoveProductClick:
                self.openPopupMessageTimerSignal.emit(
                    "لطفا تمام کالایی که از سبد خارج کرده اید را جلوی بارکد خوان بگیرید")
                # notifSound2()
                self._trustUser = True
            else:
                self.closePopupDeleteProductSignal.emit()
                # deleteSound()
                self._canRemoveProductClick = False
                self._factorList.removeProducts(self._removeList.m_data)
                print(len(self._removeList.m_data))
                self._bypassList.removeProductsUpdateBypass(self._removeList.m_data)
                self._removeList.clearData()
                self._trustUser = False
                self.state = 1

    @Slot()
    def test(self):
        print("IDBarcodeSignal connected again successfully")

    ###################################################################################################### Functions ###
    def print_states(self):
        if self._state == 0:
            print("login")
        if self._state == 1:
            print("stable")
        elif self._state == 2:
            print("\nState " + str(self._state) + " : A barcode is read and waiting to add the item.\n")

    def add_productToFactor(self, p: Product, c: int, u: bool, w2: int, w1: int):
        # insertSound()
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

    def clear_stackView(self):
        while self._stackViewDepth > 1:
            self.closeNewStackViewtHandler.emit()

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

    def clearStackView(self):
        if self._initFactorListFlag:
            while self._stackViewDepth > 1:
                self.closeTopStackViewSignal.emit()
        else:
            while self._stackViewDepth > 0:
                self.closeTopStackViewSignal.emit()


