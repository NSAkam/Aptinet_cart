from PySide2.QtCore import QObject, Signal, Property, Slot, QUrl
from shopPage import ShopPage
from settingPage import SettingPage
from Helpers.scannerHelper import ScannerHelper
from Services.gpio import GreenLight, Fan
from Services.dal import DAL
from Repositories.adminRepository import AdminRepository
import os
import sys


class Logic(QObject):
    ### Settings #######################################################################################################

    ### Models #########################################################################################################

    ### Repositories ###################################################################################################
    _adminRepository: AdminRepository

    ### Private ########################################################################################################
    _shopPage: ShopPage
    _settingPage: SettingPage
    _greenLightWorkerThread: GreenLight
    _fan: Fan
    _dal: DAL

    ### Modules ########################################################################################################
    _scanner: ScannerHelper

    def __init__(self) -> None:
        super().__init__()
        self.turnoff_greenLight()
        self._fan = Fan()
        self._fan.turn_onFan()
        self._dal = DAL()

        self._scanner = ScannerHelper()
        self._scanner.IDBarcodeReadSignal.connect(self.go_toSettingClicked)
        # self._scanner.goToSettingSignal.connect(self.go_toSettingClicked)
        self._scanner.start()

        self._adminRepository = AdminRepository(self._dal)

    ### Signals ########################################################################################################
    changedSignal = Signal()
    goToShopPageSignal = Signal()
    goToSettingPageSignal = Signal()

    ### Properties #####################################################################################################
    def get_shopPage(self):
        return self._shopPage

    def set_shopPage(self, val: ShopPage):
        self._shopPage = val
        self.changedSignal.emit()

    shopPage = Property(ShopPage, get_shopPage, set_shopPage, notify=changedSignal)

    def get_settingPage(self):
        return self._settingPage

    def set_settingPage(self, val: SettingPage):
        self.changedSignal.emit()
        self._settingPage = val

    settingPage = Property(SettingPage, get_settingPage, set_settingPage, notify=changedSignal)

    ### Sluts ##########################################################################################################
    @Slot()
    def go_toShoppingClicked(self):
        self.set_shopPage(ShopPage(self._dal, self._scanner))
        self._scanner.go_outOfLogic()
        self.goToShopPageSignal.emit()

    @Slot()
    def go_toSettingClicked(self):
        self.set_settingPage(SettingPage(self._dal, self._scanner))
        self._scanner.go_outOfLogic()
        if self._adminRepository.Login(self._scanner.get_IDBarcode()):
            self.goToSettingPageSignal.emit()
        else:
            print("Not Authorized !!!")

    @Slot()
    def reset_app(self):
        os.execl(sys.executable, sys.executable, *sys.argv)

    @Slot()
    def turnoff(self):
        os.system("sudo shutdown now")

    ### Functions ######################################################################################################
    def turnoff_greenLight(self):
        self._greenLightWorkerThread = GreenLight(False)
        self._greenLightWorkerThread.finished.connect(self._greenLightWorkerThread.deleteLater)
        self._greenLightWorkerThread.start()

