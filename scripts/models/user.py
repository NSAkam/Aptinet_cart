from PySide2.QtCore import QObject, Signal, Property


class User(QObject):
    _regtime: int = 0
    _rate: int = 0
    
    def __init__(self):
        super().__init__()
        
    @Signal
    def changed(self):
        pass
        
    def get_regtime(self):
        return self._regtime
        
    def set_regtime(self, value):
        if value:
            self._regtime = value
            self.changed.emit()
            
    regtime = Property(str, get_regtime, set_regtime, notify=changed)
    
        
    def get_rate(self):
        return self._rate
        
    def set_rate(self, value):
        if value:
            self._rate = value
            self.changed.emit()
            
    rate = Property(str, get_rate, set_rate, notify=changed)
    

    
    