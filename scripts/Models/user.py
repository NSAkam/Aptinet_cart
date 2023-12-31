from PySide2.QtCore import QObject, Signal, Property
from Models.serverUser import ServerUser


class User(QObject):
    _id: str
    _usId: str
    _regTime: str = 0
    _rate: int = 0
    _email: str = "Please enter your email address !"
    _factorPrice: float = 0.0
    _finalFactorPrice: float = 0.0
    _offerCode: str = ""
    _loggedInUser: ServerUser

    def __init__(self):
        super().__init__()
        self._loggedInUser = ServerUser()
        self._loggedInUser.set_name("Guest")

    @Signal
    def changedSignal(self):
        pass

    def get_id(self):
        return self._id

    def set_id(self, value):
        self._id = value
        self.changedSignal.emit()

    id = Property(str, get_id, set_id, notify=changedSignal)

    def get_usId(self):
        return self._usId

    def set_usId(self, value):
        self._usId = value
        self.changedSignal.emit()

    usId = Property(str, get_usId, set_usId, notify=changedSignal)

    def get_regtime(self):
        return self._regTime

    def set_regtime(self, value):
        self._regTime = value
        self.changedSignal.emit()

    regTime = Property(str, get_regtime, set_regtime, notify=changedSignal)

    def get_rate(self):
        return self._rate

    def set_rate(self, value):
        self._rate = value
        self.changedSignal.emit()

    rate = Property(str, get_rate, set_rate, notify=changedSignal)

    def get_email(self):
        return self._email

    def set_email(self, value):
        self._email = value
        self.changedSignal.emit()

    email = Property(str, get_email, set_email, notify=changedSignal)

    def get_factorPrice(self):
        return self._factorPrice

    def set_factorPrice(self, value):
        self._factorPrice = value
        self.changedSignal.emit()

    factorPrice = Property(float, get_factorPrice, set_factorPrice, notify=changedSignal)

    def get_finalFactorPrice(self):
        return self._finalFactorPrice

    def set_finalFactorPrice(self, value):
        self._finalFactorPrice = value
        self.changedSignal.emit()

    finalFactorPrice = Property(float, get_finalFactorPrice, set_finalFactorPrice, notify=changedSignal)

    def get_offerCode(self):
        return self._offerCode

    def set_offerCode(self, value):
        self._offerCode = value
        self.changedSignal.emit()

    offerCode = Property(str, get_offerCode, set_offerCode, notify=changedSignal)

    def get_loggedInUser(self):
        return self._loggedInUser

    def set_loggedInUser(self, user: ServerUser):
        self._loggedInUser = user
        self.set_email(user.email)
        self.changedSignal.emit()

    loggedInUser = Property(ServerUser, get_loggedInUser, set_loggedInUser, notify=changedSignal)
