from PySide2.QtCore import QObject, Signal, Property, Slot, QUrl
from Repositories.adminRepository import AdminRepository
from Services.dal import DAL
from Repositories.configRepository import ConfigRepositories
from Models.config import Config
from API.apiHandler import Apihandler
from updateSoftware import UpdateSoftware
from Services.wifi import WirelessModel
import time
from Services.weighsensorCalibration import WeighSensorCalibration
from Helpers.scannerHelper import ScannerHelper


class SettingPage(QObject):
    ### Settings #######################################################################################################

    ### Models #########################################################################################################
    _configs: Config

    ### Repositories ###################################################################################################
    _adminRepository: AdminRepository

    ### Private ########################################################################################################
    _dal: DAL
    _configsRepository: ConfigRepositories
    _apiHandler: Apihandler
    _lastSoftwareVersion: str
    _wifimodel: WirelessModel
    _weightsensorval: WeighSensorCalibration

    def __init__(self, dal: DAL, scanner: ScannerHelper):
        super().__init__()
        self._dal = dal
        self._adminRepository = AdminRepository(self._dal)
        self._configsRepository = ConfigRepositories(self._dal)
        self._apiHandler = Apihandler(self._dal)
        self._apiHandler.appVersionRecievedSignal.connect(self.set_lastSoftwareVersion)
        self._updateSoftware = None
        self._weightsensorval = WeighSensorCalibration()

        self._scanner = scanner
        self._scanner.IDBarcodeReadSignal.connect(self.test)
        # self._scanner.IDBarcodeReadSignal.dissconnect()

    ### Signals ########################################################################################################
    changedSignal = Signal()
    loginConfirmedSignal = Signal()
    cartInfoClickedSignal = Signal()
    updateAvailableSignal = Signal()

    ### Properties #####################################################################################################
    def get_configs(self):
        return self._configs

    def set_configs(self, val: Config):
        self._configs = val
        self.changedSignal.emit()

    configs = Property(Config, get_configs, set_configs, notify=changedSignal)

    def get_apiHandler(self):
        return self._apiHandler

    def set_apiHandler(self, val: Apihandler):
        self._apiHandler = val
        self.changedSignal.emit()

    apiHandler = Property(Apihandler, get_apiHandler, set_apiHandler, notify=changedSignal)

    def get_lastSoftwareVersion(self):
        return self._lastSoftwareVersion

    @Slot(str)
    def set_lastSoftwareVersion(self, val: str):
        self._lastSoftwareVersion = val
        self.changedSignal.emit()

    lastSoftwareVersion = Property(str, get_lastSoftwareVersion, set_lastSoftwareVersion, notify=changedSignal)

    def get_updateSoftware(self):
        return self._updateSoftware

    def set_updateSoftware(self, val: UpdateSoftware):
        self._updateSoftware = val
        self.changedSignal.emit()

    updateSoftware = Property(UpdateSoftware, get_updateSoftware, set_updateSoftware, notify=changedSignal)

    def getwifiModel(self):
        return self._wifimodel

    wifimodel = Property(QObject, getwifiModel, constant=True)

    def get_weightSensor(self):
        return self._weightsensorval

    def set_weightSensor(self, val):
        self._weightsensorval = val
        self.changedSignal.emit()

    weightsensor = Property(WeighSensorCalibration, get_weightSensor, set_weightSensor, notify=changedSignal)

    ### Sluts ##########################################################################################################
    # @Slot(str, str)
    # def confirm_clicked(self, username: str, password: str):
    #     print(username + "       " + password)
    #     if self._adminRepository.Login(username) and (password == "123456"):
    #         self.loginConfirmedSignal.emit()

    @Slot()
    def cart_infoClicked(self):
        print("cart_infoClicked")
        self.set_configs(self._configsRepository.get_Config())
        print(self._configs.get_appVersion())
        self.cartInfoClickedSignal.emit()
        self._apiHandler.get_appVersion()
        if self._configs.get_appVersion() != self._lastSoftwareVersion:
            self.updateAvailableSignal.emit()
            self.set_updateSoftware(UpdateSoftware())

    @Slot()
    def gotoWifiSettings(self):
        self._wifimodel = WirelessModel()
        # self._wifimodel.threadscanerFinished.connect(self.finishwifiscannerThread)

    @Slot()
    def backFromWifiSettigs(self):
        time.sleep(1)
        self._wifimodel.destroy()
        # del self._wifimodel
        # print("backed")

    @Slot()
    def test(self):
        print("IDBarcodeSignal connected again successfully")

    ### Functions ######################################################################################################

