from PySide2.QtCore import QObject, Signal, Property, Slot, QUrl
from shopPage import ShopPage
from settingPage import SettingPage
from Helpers.scannerHelper import ScannerHelper
from Services.gpio import GreenLight, Fan
from Services.dal import DAL
from Helpers.batteryHelper import BatteryHelper

from Repositories.adminRepository import AdminRepository
from Repositories.userRepository import UserRepository
from Repositories.userServerRepository import UserServerRepository
from Repositories.configRepository import ConfigRepositories
from Models.user import User
from Models.lang import Lang
from Models.Helpers.langModel import LangModel
import os
import sys
from Services.lang import languageReader


class Logic(QObject):
    ### Settings #######################################################################################################

    ### Models #########################################################################################################

    ### Repositories ###################################################################################################
    _adminRepository: AdminRepository
    _userRepository: UserRepository
    _userServerRepository: UserServerRepository
    _configRepository: ConfigRepositories

    ### Private ########################################################################################################
    _shopPage: ShopPage
    _settingPage: SettingPage
    _greenLightWorkerThread: GreenLight
    _fan: Fan
    _dal: DAL
    _user: User
    _phoneNumber: str = ""

    ### Modules ########################################################################################################
    _scanner: ScannerHelper
    _battery: BatteryHelper

    ### Language #######################################################################################################
    _lang: languageReader
    _langList: LangModel

    def __init__(self) -> None:
        path = "/home/aptinet/languages/"
        self._langList.insert_languageList([Lang(".".join(f.split(".")[:-1])) for f in os.listdir(path)])

        super().__init__()

        self.turnoff_greenLight()
        self._fan = Fan()
        self._fan.turn_onFan()
        self._dal = DAL()

        self._scanner = ScannerHelper()
        self._scanner.IDBarcodeReadSignal.connect(self.go_toSettingClicked)
        # self._scanner.goToSettingSignal.connect(self.go_toSettingClicked)
        self._scanner.start()

        self._battery = BatteryHelper()
        # self._battery.start()

        self._configRepository = ConfigRepositories(self._dal)
        self.set_lang(languageReader(self._configRepository.get_lang()))
        self._adminRepository = AdminRepository(self._dal)
        self._userRepository = UserRepository(self._dal)
        self._userServerRepository = UserServerRepository(self._dal)
        self._user = self._userRepository.create_user()
        if self._user.get_id() == -1:
            print("User not Created")
            # os.execl(sys.executable, sys.executable, *sys.argv)

    ### Signals ########################################################################################################
    changedSignal = Signal()
    goToShopPageSignal = Signal()
    goToSettingPageSignal = Signal()
    validPhoneNumberSignal = Signal()
    showPopupMessageTimerSignal = Signal(str)
    languageChangedSignal = Signal()

    ### Properties #####################################################################################################
    def get_lang(self):
        return self._lang

    def set_lang(self, v):
        self._lang = v
        self.changedSignal.emit()

    lang = Property(languageReader, get_lang, set_lang, notify=changedSignal)

    def get_lanList(self):
        return self._langList

    langList = Property(LangModel, get_lanList, constant=True)

    def get_shopPage(self):
        return self._shopPage

    def set_shopPage(self, val: ShopPage):
        self._shopPage = val
        self.changedSignal.emit()

    shopPage = Property(ShopPage, get_shopPage,
                        set_shopPage, notify=changedSignal)

    def get_settingPage(self):
        return self._settingPage

    def set_settingPage(self, val: SettingPage):
        self.changedSignal.emit()
        self._settingPage = val

    settingPage = Property(SettingPage, get_settingPage,
                           set_settingPage, notify=changedSignal)

    ### Sluts ##########################################################################################################
    @Slot(str)
    def login_phoneNumber(self, phoneNumber: str):
        serverUser = self._userServerRepository.loginByPhone(phoneNumber)
        if not serverUser.get_id() == "":
            self._user.set_loggedInUser(serverUser)
            # self._phoneNumber = phoneNumber
            self.validPhoneNumberSignal.emit()
        else:
            self.showPopupMessageTimerSignal.emit("not valid phone number")

    @Slot(str)
    def enter_sentCode(self, sentCode: str):
        if sentCode == "2212":
            self.continue_clicked()
        else:
            self.showPopupMessageTimerSignal.emit("not valid code")

    @Slot()
    def login_loyaltyCartClicked(self):
        self._scanner.loyaltyCardBarcodeReadSignal.connect(
            self.login_loyaltyCart)

    @Slot()
    def login_loyaltyCart(self):
        serverUser = self._userServerRepository.loginByloyalityBarcode(
            self._scanner.get_loyaltyCardBarcode())
        if not serverUser.get_id() == "":
            self._scanner.loyaltyCardBarcodeReadSignal.disconnect()
            self._user.set_loggedInUser(serverUser)
            self.continue_clicked()
        else:
            self.showPopupMessageTimerSignal.emit("not valid loyalty card")

    @Slot(str)
    def login_loyaltyCode(self, loyaltyCode: str):
        serverUser = self._userServerRepository.loginByloyalityBarcode(
            loyaltyCode)
        if not serverUser.get_id() == "":
            self._user.set_loggedInUser(serverUser)
            self.continue_clicked()
        else:
            self.showPopupMessageTimerSignal.emit("not valid loyalty code")

    @Slot()
    def login_loyaltyCartBackClicked(self):
        self._scanner.loyaltyCardBarcodeReadSignal.disconnect()

    @Slot()
    def continue_clicked(self):
        self._scanner.IDBarcodeReadSignal.disconnect()
        self.set_shopPage(ShopPage(self._dal, self._user, self._scanner))
        self.goToShopPageSignal.emit()

    # @Slot()
    # def go_toShoppingClicked(self):
    #     self._scanner.IDBarcodeReadSignal.disconnect()
    #     self.set_shopPage(ShopPage(self._dal, self._user, self._scanner))
    #     self.goToShopPageSignal.emit()

    @Slot()
    def go_toSettingClicked(self):
        self._scanner.IDBarcodeReadSignal.disconnect()
        self.set_settingPage(SettingPage(self._dal, self._scanner))
        self._scanner.go_outOfLogic()
        if self._adminRepository.Login(self._scanner.get_IDBarcode()):
            self.goToSettingPageSignal.emit()
        else:
            print("Not Authorized !!!")

    @Slot(str)
    def language_Changed(self, v):
        if v == "arabic":
            self._configRepository.set_lang("arabic")
            self.languageChangedSignal.emit()
        elif v == "en":
            self._configRepository.set_lang("en")
            self.languageChangedSignal.emit()
        else:
            self._configRepository.set_lang("en")

    @Slot()
    def reset_app(self):
        os.execl(sys.executable, sys.executable, *sys.argv)

    @Slot()
    def turnoff(self):
        os.system("sudo shutdown now")

    ### Functions ######################################################################################################
    def turnoff_greenLight(self):
        self._greenLightWorkerThread = GreenLight(False)
        self._greenLightWorkerThread.finished.connect(
            self._greenLightWorkerThread.deleteLater)
        self._greenLightWorkerThread.start()


