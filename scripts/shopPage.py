import os
import sys
import time
from threading import Thread
from PySide2.QtCore import QObject, Signal, Property, Slot
from Models.product import Product
from Models.Helpers.productModel import ProductModel
from Models.user import User
from Models.serverUser import ServerUser
# from Services.weightsensor import WeightSensorWorker
from Services.dal import DAL
from Helpers.scannerHelper import ScannerHelper
from Helpers.weightSensorHelper import WeightSensorHelper
from Services.sound import *
from Services.gpio import GreenLight

from Repositories.userRepository import UserRepository
from Repositories.userServerRepository import UserServerRepository


class ShopPage(QObject):
    ### Settings #######################################################################################################
    _insertProductTime: int = 8  # actual time = n -1
    _validInsertedWeightForCalTol: int = 3  # Accept inserted product without checking weight under this limit
    _basketWeightLimit: int = 20000  # grams
    _lightestProductWeight: int = 11  # grams

    ### Models #########################################################################################################
    _factorList: ProductModel
    _suggestedProducts: ProductModel
    _offersProducts: ProductModel
    _bypassList: ProductBypassModel
    _newProduct: Product

    ### Repositories ###################################################################################################
    _userRepository: UserRepository
    _userServerRepository: UserServerRepository

    ### Private ########################################################################################################
    _state: int = 0
    _inBypass: bool = False
    _countDownTimer: int = -60
    _startWeight: int = 0
    _basketWeightShouldBe: int = 0
    _basketIsFull: bool = False
    _basketLoad: int = 0
    _user: User
    _loggedInUser: ServerUser
    #####################################################
    _scanner: ScannerHelper
    _weightSensor: WeightSensorHelper

    def __init__(self):
        super().__init__()
        dal = DAL()

        self._startProcess = None


        #### Barcode Scanner ######################################
        self._scanner = ScannerHelper()
        self._scanner.EAN13ReadSignal.connect(self.barcodeRead)
        self._scanner.loyaltyCardBarcodeReadSignal.connect(self.read_loyaltyCardBarcode)
        self._scanner.start()

        #### WeightSensor #########################################
        self._weightSensor = WeightSensorHelper()
        self._weightSensor.stepBasketWeightChangedSignal.connect(self.basketWeightChanged)
        self._weightSensor.start()

        #### Models ###############################################
        self._factorList = ProductModel(dal)
        self._suggestedProducts = ProductModel(dal)
        self._offersProducts = ProductModel(dal)
        self._bypassList = ProductBypassModel(dal)

        #### User #################################################
        self._userRepository = UserRepository(dal)
        self._userServerRepository = UserServerRepository(dal)
        self._user = self._userRepository.create_user()
        if self._user.get_id() == -1:
            os.execl(sys.executable, sys.executable, *sys.argv)   # restart app

        #### Insert Timer Thread ##################################
        self._canTimerTick = True
        self._timerThread = Thread(target=self.timerSlot)
        self._timerThread.start()

        ###########################################################


    ### Signals ########################################################################################################
    changedSignal = Signal()
    goToSoppingPageSignal = Signal()
    showNewProductScannedSignal = Signal()
    successfulLoginSignal = Signal()

    ### Properties #####################################################################################################
    def get_countDownTimer(self):
        return self._countDownTimer

    def set_countDownTimer(self, v: int):
        self._countDownTimer = v
        self.changedSignal.emit()

    countDownTimer = Property(int, get_countDownTimer, set_countDownTimer, notify=changedSignal)

    def get_newProduct(self):
        return self._newProduct

    def set_newProduct(self, v: Product):
        self._newProduct = v
        self.changedSignal.emit()

    newProduct = Property(Product, get_newProduct, set_newProduct, notify=changedSignal)

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

    ### Sluts ##########################################################################################################    @Slot()
    def barcodeRead(self):
        product = self._factorList.get_productByBarcode(self._scanner.get_barcode())
        self._bypassList.insertProduct(product.copy_product(), 0)

        if self._state == 1:
            self.set_countDownTimer(self._insertProductTime)
            self.set_newProduct(product)
            self.set_state(2)

    @Slot()
    def basketWeightChanged(self, val2: int, val1: int):
        if not self._inBypass:
            ###############################################
            #### ADD WEIGHT ###############################
            ###############################################

            if val2 > val1:
                if not self._startProcess:
                    self._startProcess = True
                    self._startWeight = val1

                value = val2 - val1

                if self._state == 1:
                    pass

                elif self._state == 2:
                    if self._newProduct.getInsertedweight() < self._validInsertedWeightForCalTol:
                        self.add_productToFactor(self._newProduct, 1, True, val2, val1)

                    # else:
                    #     if


                elif self._state == 3:
                    pass
                elif self._state == 4:
                    pass
                elif self._state == 5:
                    pass
                elif self._state == 6:
                    pass
                elif self._state == 7:
                    pass

            ###############################################
            #### REMOVE WEIGHT ############################
            ###############################################
            else:   # val2 < val1
                if self._startProcess:
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
        else:
            pass   # pop up nat valid phone number

    @Slot()
    def read_loyaltyCardBarcode(self):
        serverUser = self._userServerRepository.loginByloyalityBarcode(self._scanner.get_loyaltyCardBarcode())
        if not serverUser.get_id() == "":
            self._user.set_loggedInUser(serverUser)
            self.successfulLoginSignal.emit()

    ### Functions ######################################################################################################

    def get_state(self):
        return self._state

    def set_state(self, v: int):
        self._state = v

    def print_states(self):
        if self._state == 1:
            print("stable")
        elif self._state == 2:
            print("\nState " + str(self._state) + " : A barcode is read and waiting to add the item.\n")

    def add_productToFactor(self, p: Product, c: int, u: bool, w2: int, w1: int):
        insertSound()
        self._factorList.insertProduct(p, c)
        self._bypassList.insertProduct(p.copy_product(), c)
        if u:
            self._factorList.updateWeight(p, w2 - w1)
        self._basketWeightShouldBe = w2
        self.cal_basketLoad(w2)

    def cal_basketLoad(self, weight: int):
        load = int((weight - self._startWeight) / self._basketWeightLimit * 100)
        load = min(max(load, 0), 100)
        self.set_basketLoad(load)
        self.set_basketIsFull(True) if load == 100 else self.set_basketIsFull(False)


