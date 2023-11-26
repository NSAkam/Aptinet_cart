from PySide2.QtCore import QObject, Signal, Property,Slot,QUrl
from Services.wifi import WirelessModel
from Helpers.scannerHelper import ScannerHelper
from Repositories.adminRepository import AdminRepository
from Services.dal import DAL
from Repositories.configRepository import ConfigRepositories



class SettingPage(QObject):
    ### Settings #######################################################################################################

    ### Models #########################################################################################################
    _configsRepository: ConfigRepositories
    ### Repositories ###################################################################################################
    _adminRepository: AdminRepository

    ### Private ########################################################################################################
    _dal: DAL



    # _wifimodel : WirelessModel
    # _scanner: ScannerHelper


    def __init__(self):
        super().__init__()
        self._dal = DAL()
        self._adminRepository = AdminRepository(self._dal)
        self._configsRepository = ConfigRepositories(self._dal)



    ### Signals ########################################################################################################
    changedSignal = Signal()
    loginConfirmedSignal = Signal()

    ### Properties #####################################################################################################
    def get_configsRepository(self):
        return self._configsRepository

    def set_configsRepository(self, v: ConfigRepositories):
        self._configsRepository = v
        self.changedSignal.emit()

    configsRepository = Property(ConfigRepositories, get_configsRepository, set_configsRepository, notify=changedSignal)
    ### Sluts ##########################################################################################################

    @Slot(str, str)
    def confirm_clicked(self, username: str, password: str):
        if self._adminRepository.Login(username) and (password == "123456"):
            self.loginConfirmedSignal.emit()

    @Slot()
    def cart_infoClicked(self):
        pass


    ### Functions ######################################################################################################
