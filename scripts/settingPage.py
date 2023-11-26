from PySide2.QtCore import QObject, Signal, Property, Slot, QUrl
from Repositories.adminRepository import AdminRepository
from Services.dal import DAL
from Repositories.configRepository import ConfigRepositories
from Models.config import Config
from API.apiHandler import Apihandler
from updateSoftware import UpdateSoftware


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

    def __init__(self):
        super().__init__()
        self._dal = DAL()
        self._adminRepository = AdminRepository(self._dal)
        self._configsRepository = ConfigRepositories(self._dal)
        self._apiHandler = Apihandler(self._dal)
        self._updateSoftware = None

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

    ### Sluts ##########################################################################################################
    @Slot(str, str)
    def confirm_clicked(self, username: str, password: str):
        if self._adminRepository.Login(username) and (password == "123456"):
            self.loginConfirmedSignal.emit()

    @Slot()
    def cart_infoClicked(self):
        self.set_configs(self._configsRepository.get_Config())
        print(self._configs.get_appVersion())
        self.cartInfoClickedSignal.emit()
        self.set_lastSoftwareVersion(self._apiHandler.get_appVersion())
        if self._configs.get_appVersion() != self._lastSoftwareVersion:
            self.updateAvailableSignal.emit()
            self.set_updateSoftware(UpdateSoftware())

    ### Functions ######################################################################################################
