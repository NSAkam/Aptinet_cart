import os
import sys
import time
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
    _validInsertedWeightForCalTol: int = 3  # Accept inserted product without checking weight under this limit
    _basketWeightLimit: int = 20000  # grams
    _lightestProductWeight: int = 11  # grams
    _lightestWeightForHeavyProduct: int = 25   # grams
    _lightestWeightForLightWeightProduct: int = 8
    _basketWeightTolerance: int = 50   # better fit: 25

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
    _basketLoad: int = 0
    _stackViewDepth: int
    _basketIsFull: bool = False
    _inBypass: bool = False
    _loginFinished: bool = False
    _startProcess: bool = False
    _manualBarcodeEntered: bool = False
    _canRemoveProductClick: bool = False
    _trustUser: bool = False
    _shouldBarcodeToBeScannToAddProduct: bool = True
    _lightWeightProductExistInBasket: bool = False


    ######################################################################################################## Modules ###
    _scanner: ScannerHelper
    _weightSensor: WeightSensorWorker

    def __init__(self):
        super().__init__()

        #### Private ##############################################
        dal = DAL()

        #### Repositories #########################################
        self._userRepository = UserRepository(dal)
        self._userServerRepository = UserServerRepository(dal)
        self._productRepository = ProductRepository(dal)

        #### Barcode Scanner ######################################
        self._scanner = ScannerHelper()
        self._scanner.EAN13ReadSignal.connect(self.barcodeRead)
        self._scanner.loyaltyCardBarcodeReadSignal.connect(self.read_loyaltyCardBarcode)
        self._scanner.start()

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
        self._user = self._userRepository.create_user()
        if self._user.get_id() == -1:
            os.execl(sys.executable, sys.executable, *sys.argv)   # restart app

        #### Insert Timer Thread ##################################
        self._canTimerTick = True
        self._timerThread = Thread(target=self.timerSlot)
        self._timerThread.start()

        ###########################################################

    ######################################################################################################## Signals ###
    changedSignal = Signal()
    showNewProductScannedSignal = Signal()
    successfulLoginSignal = Signal()
    closeAllPopUpSignal = Signal()
    clodePopUpMessageTimer = Signal()
    hideOfferListSignal = Signal()
    visibleProductListDeleteSignal = Signal()

    showStartUpShoppingLabelSignal = Signal(bool)

    closeNewStackViewHandlerSignal = Signal()

    openPopupWeightNotMatchWithBarcodeSignal = Signal()
    closePopupWeightNotMatchWithBarcodeSignal = Signal()

    ##################################################################################################### Properties ###
    def get_state(self):
        return self._state

    def set_state(self, state: int):
        self._state = state
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
        if not self._inBypass:
            # self.hideOfferListSignal.emit()
            product = self._productRepository.get_product(self._scanner.get_barcode())

            self._bypassList.insertProduct(product.copy_product(), 0)

            if self.state == 1:
                if not self.basketIsFull:
                    self.adjust_wightSensorSensitivity(product.meanWeight)
                    self.state = 2
                    self.newProduct = product
                    self.countDownTimer = self._insertProductTime
                    self._suggestedList = self._productRepository.get_suggesstionProducts(product.barcode)
                    self.showNewProductScannedSignal.emit()

                    if self._manualBarcodeEntered:
                        self._manualBarcodeEntered = False

                else:
                    pass   # pop up message timer basket is full

            elif self.state == 2:
                if self.newProduct.barcode == self._scanner.get_barcode():
                    self.countDownTimer = self._insertProductTime
                else:
                    self.newProduct = product
                    self.adjust_wightSensorSensitivity(product.meanWeight)
                    self.countDownTimer = self._insertProductTime
                    self._suggestedList = self._productRepository.get_suggesstionProducts(product.barcode)
                    self.showNewProductScannedSignal.emit()


            elif self.state == 5:
                isAcceptablebarcodeForRemove, self._canRemoveProductClick, removeSuccessfullyBefore = self._removeList.updateValidBarcodeSetForRemove(
                    self._scanner.barcode)

                if not isAcceptablebarcodeForRemove:
                    if removeSuccessfullyBefore:
                        pass   # pop up timer "لطفا سایر کالاهایی که از سبد خارج کرده اید را جلوی بارکد خوان بگیرید"
                    else:
                        pass   # pop up timer "لطفا فقط کالایی که از سبد خارج کرده اید را جلوی بارکد خوان بگیرید"
                else:
                    pass
                self._trustUser = False
                if len(self._removeList.m_data) == 1:
                    self.visibleProductListDeleteSignal.emit()

    @Slot()
    def basketWeightChanged(self, val2: int, val1: int):
        if not self._inByPass:
            self.hideOfferListSignal.emit()
            value: int = val2 - val1
            # self._logStash.newChangeWeight(self._datetime.time, value, self._userID)

            # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ADD WEIGHT <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
            if val2 >= val1:
                if self._states == 1:
                    if not self._shouldBarcodeToBeScannToAddProduct:
                        if ((value < self.newProduct.meanWeight + self.newProduct.tolerance) and (value >= self.newProduct.meanWeight - self.newProduct.tolerance)):
                            # insertSound()
                            self._factorList.insertProduct(self.newProduct, 1)
                            self._bypassList.insertProduct(self.newProduct.copy_product(), 1)
                            self.cal_basketLoad(val2)
                            self._basketWeightShouldBe = val2
                            self._countdownTimer = -1

                            # self._productsmodel.updateWeight(self.getNewProduct(), val2 - val1)

                        else:
                            self._shouldBarcodeToBeScannToAddProduct = True
                            self.openPopupNoBarcodeScanned.emit()
                            if abs(value) > 20:
                                notifSound()
                            self._basketWeightShouldBe = val1
                            self.setState(4)

                    else:
                        self.openPopupNoBarcodeScanned.emit()
                        if (abs(value) > 20):
                            notifSound()
                        self._basketWeightShouldBe = val1
                        self.setState(4)

                elif self._states == 2:
                    if self.newProduct.insertedWeight < self._validInsertedWeightForCalTol:
                        # insertSound()
                        self.showStartUpShoppingLabelSignal.emit(False)
                        self._factorList.insertProduct(self.newProduct, 1)
                        self._bypassList.insertProduct(self.newProduct.copy_product(), 1)

                        # self._productsmodel.updateWeight(self.getNewProduct(), val2 - val1)

                        # self.check_productWeight(self.newProduct) <---------------- usable when update product
                        if (val2 - val1) <= self._lightestWeightForHeavyProduct + self._weightSensor.acceptable_tolerance:
                            self._lightWeightProductExistInBasket = True

                        self.adjust_wightSensorSensitivity(val2 - val1)
                        self.setState(1)
                        self._basketWeightShouldBe = val2
                        self.closeNewStackViewHandlerSignal.emit()
                        self._countdownTimer = -11
                        self._shouldBarcodeToBeScannToAddProduct = True

                    else:
                        if (value < self.newProduct.meanWeight + self.newProduct.tolerance) and (value >= (value < self.newProduct.meanWeight - self.newProduct.tolerance)):
                            insertSound()
                            self.showStartUpShoppingLabelSignal.emit(False)
                            self._factorList.insertProduct(self._newProduct, 1)
                            self._bypassList.insertProduct(self._newProduct, 1)

                            # self._productsmodel.updateWeight(self.getNewProduct(), val2 - val1)

                            self.check_productWeight(self._newProduct)

                            # if self.getNewProduct().getAvgWeight() > self._lightest_weight_for_heavy_weight_product + self._weighsensor.acceptable_tolerance:
                            #     self._weighsensor.lightest_weight = self._lightest_weight_for_heavy_weight_product
                            self.setState(1)
                            self._basketWeightShouldBe = val2
                            self.closeNewStackViewHandlerSignal.emit()
                            self._countdownTimer = -1
                            self._shouldBarcodeToBeScannToAddProduct = False

                        else:
                            self.openPopupWeightNotMatchWithBarcodeSignal.emit()
                            # notifSound()
                            self._basketWeightShouldBe = val1
                            self.setState(3)

                elif self._states == 3:
                    if self._basketWeightShouldBe - self._basketWeightTolerance <= val2 <= self._basketWeightShouldBe + self._basketWeightTolerance:
                        self._basketWeightShouldBe = val2
                        self.setState(2)
                        self.closePopupWeightNotMatchWithBarcodeSignal.emit()
                    else:
                        pass   # "لطفا کالایی که بدون اسکن کردن در سبد قرار داده اید را از آن خارج کنید."
                        # notifSound()

                elif self._states == 4:
                    if self._basketWeightShouldBe - self._basketweightTolerance <= val2 <= self._basketWeightShouldBe + self._basketweightTolerance:
                        self._basketWeightShouldBe = val2
                        self.closePopupNoBarcodeScanned.emit()
                        self.setState(1)
                    elif self._basketWeightShouldBe + self._basketweightTolerance <= val2:
                        self.openPopupMessageTimer.emit(
                            "لطفا کالایی که بدون اسکن کردن در سبد قرار داده اید را از سبد خارج کرده و مجددا اقدام به اضافه کردن یک به یک آن ها کنید.")
                        notifSound()
                        # if not self.lwire.isRunning():
                        #     self.lwire = L_Wire("error")
                        #     self.lwire.start()
                        self.l_wire(3)

                elif self._states == 5:
                    if self._basketWeightShouldBe - self._basketweightTolerance <= val2 <= self._basketWeightShouldBe + self._basketweightTolerance:
                        self._basketWeightShouldBe = val2
                        self.closePopupDeleteProduct.emit()
                        self.setState(1)
                        self._maybeDeletedProducts.clearData()
                        self._trustUser = False
                    else:
                        self.openPopupMessage.emit(
                            "لطفا کالایی که در سبد قرار داده اید را برداشته و فرآیند حذف را کامل کنید. سپس اقدام به اضافه کردن کالای مورد نظر کنید")
                        notifSound()
                        self.setState(6)
                        # if not self.lwire.isRunning():
                        #     self.lwire = L_Wire("error")
                        #     self.lwire.start()
                        self.l_wire(3)
                        self._basketweightRemoveProcces = val1

                elif self._states == 6:
                    if self._basketWeightShouldBe - self._basketweightTolerance <= val2 <= self._basketWeightShouldBe + self._basketweightTolerance:
                        self._basketWeightShouldBe = val2
                        self.setState(1)
                        self.closePopupMessage.emit()
                        self.closePopupDeleteProduct.emit()
                    elif self._basketweightRemoveProcces - self._basketweightTolerance <= val2 <= self._basketweightRemoveProcces + self._basketweightTolerance:
                        self._basketweightRemoveProcces = val2
                        self.setState(5)
                        self.closePopupMessage.emit()

                elif self._states == 7:
                    if self._basketweightRemoveProcces - self._basketweightTolerance <= val2 <= self._basketweightRemoveProcces + self._basketweightTolerance:
                        self._basketweightRemoveProcces = val2
                        self.setState(5)
                        self.closePopupMessage.emit()
                    elif self._basketWeightShouldBe - self._basketweightTolerance <= val2 <= self._basketWeightShouldBe + self._basketweightTolerance:
                        self._basketWeightShouldBe = val2
                        self.setState(1)
                        self.closePopupMessage.emit()
                        self.closePopupDeleteProduct.emit()
                        self._maybeDeletedProducts.clearData()
                        self._trustUser = False

                elif self._states == 8:
                    if not self._paymentCartScanned:
                        if abs(val2 - self._basketWeightShouldBe) >= 100:
                            self.setState(9)
                            self.openPopUpMessageNotAllowedChangeWeight.emit()
                            notifSound()
                            self._basketWeightShouldBe = val1

                elif self._states == 9:
                    # if abs(value) >= 30:
                    # if not self._paymentCartScanned:

                    if self._basketWeightShouldBe - self._basketweightTolerance <= val2 <= self._basketWeightShouldBe + self._basketweightTolerance:
                        self._basketWeightShouldBe = val2
                        self.closePopUpMessageNotAllowedChangeWeight.emit()
                        if self._successfulPayment:
                            self.setState(10)
                            self.showAfterPayment.emit()
                        else:
                            self.setState(8)

                elif self._states == 10:
                    # if abs(value) >= 150:
                    #     self.setState(11)
                    #     self._basketweightShouldBe = val1
                    #     self.openPopUpMessageNotAllowedToAddProduct.emit()
                    #     # notifSound()
                    pass

                elif self._states == 11:
                    # if abs(value) >= 30:
                    #     if self._basketweightShouldBe - self._basketweightTolerance <= val2 <= self._basketweightShouldBe + self._basketweightTolerance:
                    #         self.setState(10)
                    #         self._basketweightShouldBe = val2
                    #         self.closePopUpMessageNotAllowedToAddProduct.emit()
                    pass

            # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
            # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> REMOVE WEIGHT <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
            # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

            if val2 < val1:
                if len(self._historyList) == 2:
                    if self._historyList[1] - self._basketweightTolerance <= abs(value) <= self._historyList[
                            1] + self._basketweightTolerance:
                        self._historyList.append(val2 - val1)
                    else:
                        self._historyList = []
                else:
                    self._historyList = []

                if self._states == 1:
                    self._maybeDeletedProducts.validBarcodeSetForRemove(
                        self.getProductModel().m_data, abs(value))
                    if not len(self._maybeDeletedProducts.m_validBarcodeSetForDelete) == 0:
                        self.openPopupDeleteProduct.emit()
                        notifSound2()
                        self._basketWeightShouldBe = val1
                        self.setState(5)

                elif self._states == 2:
                    # waiting time = # * 0.010(s)
                    self._maybeDeletedProducts.validBarcodeSetForRemove(
                        self.getProductModel().m_data, abs(value))
                    self.openPopupDeleteProduct.emit()
                    notifSound2()
                    self._basketWeightShouldBe = val1
                    self._countdownTimer = -20
                    # self.setNewProductsVisibleHandler(False)
                    self.closeNewStackViewtHandler.emit()
                    self.setState(5)

                elif self._states == 3:
                    if self._basketWeightShouldBe - self._basketweightTolerance <= val2 < self._basketWeightShouldBe + self._basketweightTolerance:
                        self._basketWeightShouldBe = val2
                        self.closePopupNotbarcodedProduct.emit()
                        if len(self._historyList) == 3:
                            self.setState(1)
                        else:
                            self.setState(2)

                elif self._states == 4:
                    if self._basketWeightShouldBe - self._basketweightTolerance <= val2 <= self._basketWeightShouldBe + self._basketweightTolerance:
                        self._basketWeightShouldBe = val2
                        self.closePopupNoBarcodeScanned.emit()
                        self.setState(1)

                elif self._states == 5:
                    self.openPopupMessage.emit(
                        "لطفا کالایی که از سبد برداشته اید در سبد قرار دهید و پس از اتمام فرآید حذف کالای قبلی مجددا اقدام به حذف آن کالا کنید")
                    notifSound()
                    self.setState(7)
                    # if not self.lwire.isRunning():
                    #     self.lwire = L_Wire("error")
                    #     self.lwire.start()
                    self.l_wire(3)
                    self._basketweightRemoveProcces = val1

                elif self._states == 6:
                    if self._basketweightRemoveProcces - self._basketweightTolerance <= val2 <= self._basketweightRemoveProcces + self._basketweightTolerance:
                        self._basketweightRemoveProcces = val2
                        self.setState(5)
                        self.closePopupMessage.emit()

                elif self._states == 7:
                    if self._basketWeightShouldBe - self._basketweightTolerance <= val2 <= self._basketWeightShouldBe + self._basketweightTolerance:
                        self._basketWeightShouldBe = val2
                        self.setState(1)

                elif self._states == 8:
                    # if not self._paymentCartScanned:
                    #     if abs(value) >= 100:
                    #         self.setState(9)
                    #         self.openPopUpMessageNotAllowedChangeWeight.emit()
                    #         notifSound()
                    #         self._basketweightShouldBe = val1
                    pass

                elif self._states == 9:
                    # if abs(value) >= 30:
                    if self._basketWeightShouldBe - self._basketweightTolerance <= val2 <= self._basketWeightShouldBe + self._basketweightTolerance:
                        self._basketWeightShouldBe = val2
                        self.closePopUpMessageNotAllowedChangeWeight.emit()
                        if self._successfulPayment:
                            self.setState(10)
                            self.showAfterPayment.emit()
                        else:
                            self.setState(8)

                elif self._states == 10:
                    # if abs(val2 - val1) >= 50:
                    #     self.setState(11)
                    #     self._basketweightShouldBe = val1
                    #     self.openPopupFullMessageTimer.emit(
                    #         "در صورتی که بازرس خروج شما را تایید کرده است، محصولات را از سبد خارج کنید!")
                    #     # notifSound()
                    pass

                elif self._states == 11:
                    # if abs(val2 - val1) >= 30:
                    #     if self._basketweightShouldBe - self._basketweightTolerance <= val2 <= self._basketweightShouldBe + self._basketweightTolerance:
                    #         self.setState(10)
                    #         self._basketweightShouldBe = val2
                    #         self.closePopUpMessageNotAllowedToAddProduct.emit()
                    pass








    @Slot()
    def timerSlot(self):
        while self._canTimerTick:
            self.set_countDownTimer(self.get_countDownTimer() - 1)
            time.sleep(1)

    @Slot(str)
    def enter_phoneNumberClicked(self, phoneNumber: str):
        serverUser = self._userServerRepository.loginByPhone(phoneNumber)
        if not serverUser.get_id() == "":
            self._user.set_loggedInUser(serverUser)
            self.successfulLoginSignal.emit()
            self.login_finished()

        else:
            pass   # pop up nat valid phone number

    @Slot()
    def read_loyaltyCardBarcode(self):
        serverUser = self._userServerRepository.loginByloyalityBarcode(self._scanner.get_loyaltyCardBarcode())
        if not serverUser.get_id() == "":
            self._user.set_loggedInUser(serverUser)
            self.successfulLoginSignal.emit()
            self.login_finished()

        else:
            pass   # pop up timer

    @Slot(str)
    def enter_loyaltyCardBarcode(self, loyaltyCode: str):
        serverUser = self._userServerRepository.loginByloyalityBarcode(loyaltyCode)
        if not serverUser.get_id() == "":
            self._user.set_loggedInUser(serverUser)
            self.successfulLoginSignal.emit()
            self.login_finished()
        else:
            pass   # pop up timer

    @Slot()
    def login_finished(self):
        self.set_state(1)

    @Slot(int)
    def stackview_depthChanged(self, Depth: int):
        self._stackViewDepth = Depth

    ###################################################################################################### Functions ###
    def print_states(self):
        if self._state == 0:
            print("login")
        if self._state == 1:
            print("stable")
        elif self._state == 2:
            print("\nState " + str(self._state) + " : A barcode is read and waiting to add the item.\n")

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
