from PySide2.QtCore import QObject, Signal, Property, Slot, QUrl
from Repositories.adminRepository import AdminRepository
from Services.dal import DAL
from Repositories.configRepository import ConfigRepositories
from Models.config import Config
from API.apiHandler import Apihandler
from updateSoftware import UpdateSoftware,UpdateFiles
from Services.wifi import WirelessModel
from Services.sound import *
from Services.gpio import *
from datetime import datetime
import time
from Services.weighsensorCalibration import WeighSensorCalibration
from Helpers.scannerHelper import ScannerHelper
from Services.uploader import Uploader


class SettingPage(QObject):
    ### Settings #######################################################################################################
    _calibrationPeriod: int = 15
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
    _updateSoftware:UpdateSoftware
    _updateFiles:UpdateFiles
    _uploader : Uploader
    _uploadedPercentage : int = 0
    _lastCalibrationDate: str = ""
    _readBarcode: str = ""


    def __init__(self, dal: DAL, scanner: ScannerHelper):
        super().__init__()
        self._dal = dal
        self._adminRepository = AdminRepository(self._dal)
        self._configsRepository = ConfigRepositories(self._dal)
        self._configs = Config()
        self.set_configs(self._configsRepository.get_Config())
        self._apiHandler = Apihandler(self._dal)
        self._apiHandler.appVersionRecievedSignal.connect(self.set_lastSoftwareVersion)
        self._updateSoftware = None
        self._weightsensorval = WeighSensorCalibration()
        self._scanner = scanner
        self._scanner.readBarcodeSignal.connect(self.scanner_read)
        self._updateFiles = UpdateFiles()



    ### Signals ########################################################################################################
    changedSignal = Signal()
    loginConfirmedSignal = Signal()
    cartInfoClickedSignal = Signal()
    updateAvailableSignal = Signal()
    updateUploadToServerSignal = Signal(int)
    expiredCalibrationSignal = Signal(bool)   # if expired True else False

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

    def get_updateFiles(self):
        return self._updateFiles

    def set_updateFiles(self, val: UpdateSoftware):
        self._updateFiles = val
        self.changedSignal.emit()

    updateFiles = Property(UpdateFiles, get_updateFiles, set_updateFiles, notify=changedSignal)

    def getwifiModel(self):
        return self._wifimodel

    wifimodel = Property(QObject, getwifiModel, constant=True)

    def get_weightSensor(self):
        return self._weightsensorval

    def set_weightSensor(self, val):
        self._weightsensorval = val
        self.changedSignal.emit()

    weightsensor = Property(WeighSensorCalibration, get_weightSensor, set_weightSensor, notify=changedSignal)

    def get_uploadedPercentage(self):
        return self._uploadedPercentage

    @Slot(int)
    def set_uploadedPercentage(self,v:int):
        self._uploadedPercentage = v
        self.updateUploadToServerSignal.emit(v)

    uploadedPercentage = Property(int,get_uploadedPercentage,set_uploadedPercentage,notify=updateUploadToServerSignal)

    def get_lastCalibrationDate(self):
        return self._lastCalibrationDate   # datetime.fromtimestamp(self._configs.get_calibrationDate())

    def set_lastCalibrationDate(self, v: str):
        self._lastCalibrationDate = v
        self.changedSignal.emit()

    lastCalibrationDate = Property(str, get_lastCalibrationDate, set_lastCalibrationDate, notify=changedSignal)

    def get_readBarcode(self):
        return self._readBarcode

    def set_readBarcode(self, v: str):
        self._readBarcode = v
        self.changedSignal.emit()

    readBarcode = Property(str,get_readBarcode, set_readBarcode, notify=changedSignal)

    ### Sluts ##########################################################################################################
    # @Slot(str, str)
    # def confirm_clicked(self, username: str, password: str):
    #     print(username + "       " + password)
    #     if self._adminRepository.Login(username) and (password == "123456"):
    #         self.loginConfirmedSignal.emit()

    @Slot()
    def cart_infoClicked(self):
        self.cartInfoClickedSignal.emit()
        self._apiHandler.get_appVersion()
        if self._configs.get_appVersion() != self._lastSoftwareVersion:
            self.updateAvailableSignal.emit()
            self.set_updateSoftware(UpdateSoftware())

        lastCalibrationDate = datetime.fromtimestamp(float(self._configs.get_calibrationDate()))
        days = (datetime.now() - lastCalibrationDate).days
        if days >= self._calibrationPeriod:
            self.set_lastCalibrationDate(str(lastCalibrationDate.date()))
            self.expiredCalibrationSignal.emit(True)
            print("expired")
        else:
            self.set_lastCalibrationDate(str(lastCalibrationDate.date()))
            self.expiredCalibrationSignal.emit(False)
            print("not expired")



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
    def scanner_read(self):
        self.set_readBarcode(self._scanner._scannerWorker.get_readBytes()[1:-1].decode('latin1'))

    @Slot()
    def startUploadToServer(self):
        # print("startUpload")
        self._uploader = Uploader()
        self._uploader.succeeded.connect(self.uploadFinished)
        self._uploader.setCurrentProgress.connect(self.set_uploadedPercentage)
        self._uploader.start()
    
    @Slot()
    def uploadFinished(self):
        pass

    @Slot()
    def save_calibrationClicked(self):
        date = str(datetime.now().timestamp())
        self._configsRepository.set_calibrationDate(date)
        self._configs.set_calibrationDate(date)

    @Slot(str)
    def select_unit(self, unit: str):
        self._configsRepository.set_quatifire(unit)
        self._configs.set_quatifire(unit)

    @Slot(str)
    def change_tax(self, tax: str):
        if int(float(tax)) < 100:
            self._configsRepository.set_taxPercentage(tax)
            self._configs.set_taxPercentage(int(float(tax)))

    @Slot()
    def sound_testClicked(self):
        playSound("notif")

    @Slot()
    def light_testClicked(self):
        self.turn_onGreenLight()
        time.sleep(3)
        self.turn_offGreenlight()

    ### Functions ######################################################################################################

    def turn_onGreenLight(self):
        self.greenLight = GreenLight(True)
        self.greenLight.finished.connect(self.greenLight.deleteLater)
        self.greenLight.start()

    def turn_offGreenlight(self):
        self.greenLight = GreenLight(False)
        self.greenLight.finished.connect(self.greenLight.deleteLater)
        self.greenLight.start()