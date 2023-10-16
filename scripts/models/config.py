from PySide2.QtCore import QObject, Signal, Property


class ConfigModel(QObject):
    _iskg: int = 0
    _currrency: str = 0
    
    @Signal
    def changed(self):
        pass
    
    def __init__(self):
        super().__init__()
        
    def get_iskg(self):
        return self._iskg
    
    def set_iskg(self, value):
        if value:
            self._iskg = value
            self.changed.emit()
            
    iskg = Property(int, get_iskg, set_iskg, notify=changed)
    
    def get_currency(self):
        return self._currrency
    
    def set_currency(self, value):
        if value:
            self._currrency = value
            self.changed.emit()
            
    read_currency = Property(str, get_currency, set_currency, notify=changed)