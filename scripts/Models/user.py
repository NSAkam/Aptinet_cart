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
    def changedSignal(self):
        pass

    def get_id(self):
        return self._id
        
    def set_id(self, value):
        self._id = value
        self.changedSignal.emit()
            
    id = Property(int, get_id, set_id, notify=changedSignal)
        
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
   
    
    def get_usId(self):
        return self._usId
        
    def set_usId(self, value):
        self._usId = value
        self.changedSignal.emit()
    
    usId = Property(str, get_usId, set_usId, notify=changedSignal)

    def get_email(self):
        return self._email
        
    def set_email(self, value):
        self._email = value
        self.changedSignal.emit()
            
    email = Property(str, get_email, set_email, notify=changedSignal)
            
    

    
    