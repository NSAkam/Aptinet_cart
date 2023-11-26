from PySide2.QtCore import QObject, Signal, Property, Slot, QUrl
# from shopPage import ShopPage
from settingPage import SettingPage
from Helpers.scannerHelper import ScannerHelper
from Services.gpio import GreenLight
import os
import sys


class Logic(QObject):
    ### Settings #######################################################################################################

    ### Models #########################################################################################################

    ### Repositories ###################################################################################################

    ### Private ########################################################################################################
    # _shopPage: ShopPage
    _settingPage: SettingPage
    _greenLightWorkerThread: GreenLight

    def __init__(self) -> None:
        super().__init__()
        self.turnoff_greenLight()

    ### Signals ########################################################################################################
    changedSignal = Signal()
    goToShopPageSignal = Signal()
    goToSettingPageSignal = Signal()

    ### Properties #####################################################################################################
    # def get_shopPage(self):
    #     return self._shopPage

    # def set_shopPage(self, val: ShopPage):
    #     self.changedSignal.emit()
    #     self._shopPage = val
    #
    # shopPage = Property(ShopPage, get_shopPage, set_shopPage, notify=changedSignal)

    def get_settingPage(self):
        return self._settingPage

    def set_settingPage(self, val: SettingPage):
        self.changedSignal.emit()
        self._settingPage = val

    settingPage = Property(SettingPage, get_settingPage, set_settingPage, notify=changedSignal)

    ### Sluts ##########################################################################################################
    # @Slot()
    # def go_toShoppingClicked(self):
    #     self.goToShopPageSignal.emit()
    #     self.set_shopPage(ShopPage())

    @Slot()
    def go_toSettingClicked(self):
        self.goToSettingPageSignal.emit()
        self.set_settingPage(SettingPage())

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