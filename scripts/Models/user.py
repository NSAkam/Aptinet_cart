from PySide2.QtCore import QObject, Signal, Property


class User(QObject):
    _regTime: int = 0
    _rate: int = 0
    _usId: int = 0
    
    def __init__(self):
        super().__init__()
        
    @Signal
    def changed(self):
        pass
        
    def getRegtime(self):
        return self._regTime
        
    def setRegtime(self, value):
        if value:
            self._regTime = value
            self.changed.emit()
            
    regTime = Property(str, getRegtime, setRegtime, notify=changed)
    
        
    def getRate(self):
        return self._rate
        
    def setRate(self, value):
        if value:
            self._rate = value
            self.changed.emit()
            
    rate = Property(str, getRate, setRate, notify=changed)
   
    
    def getUsid(self):
        return self._usId
        
    def setUsid(self, value):
        if value:
            self._usId = value
            self.changed.emit()
            
    usId = Property(str, getUsid, setUsid, notify=changed)
    

    
    