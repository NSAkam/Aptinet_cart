from PySide2.QtCore import QObject, Signal, Property


class LoggsModel(QObject):
    _regTime: int = 0
    _action: int = 0
    _value: str = ""
    _userId: int = 0
    
    @Signal
    def changed(self):
        pass
    
    def __init__(self):
        super().__init__()
        
    def getRegtime(self):
        return self._regTime
    
    def setRegtime(self, value):
        if value:
            self._regTime = value
            self.changed.emit()
            
    regTime = Property(int, getRegtime, setRegtime, notify=changed)
    
    def getAction(self):
        return self._action
    
    def setAction(self, value):
        if value:
            self._action = value
            self.changed.emit()
            
    action = Property(int, setAction, getAction, notify=changed)
    
    def getValue(self):
        return self._value
    
    def setValue(self, value):
        if value:
            self._value = value
            self.changed.emit()
            
    value = Property(str, getValue, setValue, notify=changed)
    
    
    def getUserid(self):
        return self._userId
    
    def setUserid(self, value):
        if value:
            self._userId = value
            self.changed.emit()
            
    userId = Property(str, getUserid, setUserid, notify=changed)
            