from PySide2.QtCore import QObject, Signal, Property


class User(QObject):
    _id:int
    _regTime: int = 0
    _rate: int = 0
    _usId: int = 0
    _email:str = ""
    
    def __init__(self):
        super().__init__()
        
    @Signal
    def changed(self):
        pass

    def getId(self):
        return self._id
        
    def setId(self, value):
        if value:
            self._id = value
            self.changed.emit()
            
    id = Property(int, getId, setId, notify=changed)
        
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

    def getEmail(self):
        return self._email
        
    def setEmail(self, value):
        if value:
            self._email = value
            self.changed.emit()
            
    email = Property(str, getEmail, setEmail, notify=changed)
            
    

    
    