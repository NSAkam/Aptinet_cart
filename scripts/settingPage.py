from PySide2.QtCore import QObject, Signal, Property,Slot,QUrl
from Services.wifi import WirelessModel
from Helpers.scannerHelper import ScannerHelper


class SettingPage(QObject):

    _wifimodel : WirelessModel
    _scanner: ScannerHelper

    def __init__(self):
        super().__init__()