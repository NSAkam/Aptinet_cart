from PySide2.QtCore import QObject, Signal, Property


class ConfigModel(QObject):
    _isKg: int = 0
    _currrency: str = 0
    _storeId: int = 0
    
    @Signal
    def changed(self):
        pass
    
    def __init__(self):
        super().__init__()
        
    def getIskg(self):
        return self._isKg
    
    def setIskg(self, value):
        if value:
            self._isKg = value
            self.changed.emit()
            
    isKg = Property(int, getIskg, setIskg, notify=changed)
    
    def getCurrency(self):
        return self._currrency
    
    def setCurrency(self, value):
        if value:
            self._currrency = value
            self.changed.emit()
            
    currency = Property(str, getCurrency, setCurrency, notify=changed)
    
    
    def getStoreid(self):
        return self._storeId
    
    def setStoreid(self, value):
        if value:
            self._storeId = value
            self.changed.emit()
            
    storeId = Property(str, getStoreid, setStoreid, notify=changed)