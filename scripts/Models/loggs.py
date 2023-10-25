from PySide2.QtCore import QObject, Signal, Property


class LoggsModel(QObject):
    _regTime: int = 0
    _action: int = 0
    _value: str = ""
    _userId: int = 0
    
    @Signal
    def changedSignal(self):
        pass
    
    def __init__(self):
        super().__init__()
        
    def get_regtime(self):
        return self._regTime
    
    def set_regtime(self, value):
        self._regTime = value
        self.changedSignal.emit()
            
    regTime = Property(int, get_regtime, set_regtime, notify=changedSignal)
    
    def get_action(self):
        return self._action
    
    def set_action(self, value):
        self._action = value
        self.changedSignal.emit()
            
    action = Property(int, set_action, get_action, notify=changedSignal)
    
    def get_value(self):
        return self._value
    
    def set_value(self, value):
        self._value = value
        self.changedSignal.emit()
            
    value = Property(str, get_value, set_value, notify=changedSignal)
    
    
    def get_userId(self):
        return self._userId
    
    def set_userId(self, value):
        self._userId = value
        self.changedSignal.emit()
            
    userId = Property(str, get_userId, set_userId, notify=changedSignal)
            