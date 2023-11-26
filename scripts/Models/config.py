from PySide2.QtCore import QObject, Signal, Property


class Config(QObject):
    _storeId: int = 0
    _isKg: bool = 0
    _currency: str = ""
    _appVersion: str = ""
    _dbVersion: str = ""
    _imagesVersion: str = ""
    _basketName: str = ""

    @Signal
    def changedSignal(self):
        pass

    def __init__(self):
        super().__init__()

    def get_storeId(self):
        return self._storeId

    def set_storeId(self, value):
        self._storeId = value
        self.changedSignal.emit()

    storeId = Property(int, get_storeId, set_storeId, notify=changedSignal)

    def get_iskg(self):
        return self._isKg

    def set_iskg(self, value):
        self._isKg = value
        self.changedSignal.emit()

    isKg = Property(bool, get_iskg, set_iskg, notify=changedSignal)

    def get_currency(self):
        return self._currency

    def set_currency(self, value):
        self._currency = value
        self.changedSignal.emit()

    currency = Property(str, get_currency, set_currency, notify=changedSignal)

    def get_appVersion(self):
        return self._appVersion

    def set_appVersion(self, value):
        self._appVersion = value
        self.changedSignal.emit()

    appVersion = Property(str, get_appVersion, set_appVersion, notify=changedSignal)

    def get_dbVersion(self):
        return self._dbVersion

    def set_dbVersion(self, value):
        self._dbVersion = value
        self.changedSignal.emit()

    dbVersion = Property(str, get_dbVersion, set_dbVersion, notify=changedSignal)

    def get_imagesVersion(self):
        return self._imagesVersion

    def set_imagesVersion(self, value):
        self._imagesVersion = value
        self.changedSignal.emit()

    imagesVersion = Property(str, get_imagesVersion, set_imagesVersion, notify=changedSignal)

    def get_basketName(self):
        return self._basketName

    def set_basketName(self, value):
        self._basketName = value
        self.changedSignal.emit()

    basketName = Property(str, get_basketName, set_basketName, notify=changedSignal)
