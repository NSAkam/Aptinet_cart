from PySide2.QtCore import QObject, Signal, Property,Slot,QUrl
from Services.wifi import WirelessModel
from Helpers.scannerHelper import ScannerHelper
from Repositories.adminRepository import AdminRepository
from Services.dal import DAL



class SettingPage(QObject):
    ### Settings #######################################################################################################

    ### Models #########################################################################################################

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

    ### Signals ########################################################################################################
    loginConfirmedSignal = Signal()

    ### Properties #####################################################################################################

    ### Sluts ##########################################################################################################

    @Slot(str, str)
    def confirm_clicked(self, username: str, password: str):
        if self._adminRepository.Login(username) and (password == "123456"):
            self.loginConfirmedSignal.emit()

    @Slot()
    def cart_infoClicked(self):
        pass


    ### Functions ######################################################################################################
