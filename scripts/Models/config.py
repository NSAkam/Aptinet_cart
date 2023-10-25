from PySide2.QtCore import QObject, Signal, Property


class ConfigModel(QObject):
    _isKg: int = 0
    _currrency: str = 0
    _storeId: int = 0
    
    @Signal
    def changedSignal(self):
        pass
    
    def __init__(self):
        super().__init__()
        
    def get_iskg(self):
        return self._isKg
    
    def set_iskg(self, value):
        self._isKg = value
        self.changedSignal.emit()
            
    isKg = Property(int, get_iskg, set_iskg, notify=changedSignal)
    
    def get_currency(self):
        return self._currrency
    
    def set_currency(self, value):
        self._currrency = value
        self.changedSignal.emit()
            
    currency = Property(str, get_currency, set_currency, notify=changedSignal)
    
    
    def get_storeId(self):
        return self._storeId
    
    def set_storeId(self, value):
        self._storeId = value
        self.changedSignal.emit()
            
    storeId = Property(str, get_storeId, set_storeId, notify=changedSignal)