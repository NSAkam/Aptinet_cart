from PySide2.QtCore import QObject, Signal, Property,Slot,QUrl
from shopPage import ShopPage
from settingPage import SettingPage
from Helpers.scannerHelper import ScannerHelper
from Services.gpio import *


class Logic(QObject): 
    _shopPage : ShopPage
    _settingPage : SettingPage

    def __init__(self) -> None:
        super().__init__()
        ### Turn off lights At the Start
        self.gpioWorkerThread = GpioWorker(False)
        self.gpioWorkerThread.finished.connect(self.gpioWorkerThread.deleteLater)
        self.gpioWorkerThread.start()
        
    @Signal
    def changed(self):
        pass

    #Properties #############################################
    def getShopPage(self):
        return self._shopPage
    
    def setShopPage(self,val):
        self._shopPage = val
        self.changed.emit()
    
    shoppage = Property(ShopPage,getShopPage,setShopPage,notify=changed)
    
    def getSettingPage(self) -> SettingPage:
        return self._settingPage

    def setSettingPage(self,val) -> None:
        self._settingPage = val

    settingPage = Property(SettingPage,getSettingPage,setSettingPage,notify=changed)

    @Slot()
    def gotoShopping(self):
        self.setShopPage(ShopPage())

    @Slot()
    def gotoSetting(self) -> None:
        self.setSettingPage(SettingPage())
    