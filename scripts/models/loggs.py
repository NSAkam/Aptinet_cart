from PySide2.QtCore import QObject, Signal, Property


class LoggsModel(QObject):
    _regtime: int = 0
    _action: int = 0
    _value: str = ""
    
    @Signal
    def changed(self):
        pass
    
    def __init__(self):
        super().__init__()
        
    def get_regtime(self):
        return self._regtime
    
    def set_regtime(self, value):
        if value:
            self._regtime = value
            self.changed.emit()
            
    regtime = Property(int, get_regtime, set_regtime, notify=changed)
    
    def get_action(self):
        return self._action
    
    def set_action(self, value):
        if value:
            self._action = value
            self.changed.emit()
            
    action = Property(int, set_action, get_action, notify=changed)
    
    def get_value(self):
        return self._action
    
    def set_value(self, value):
        if value:
            self._value = value
            self.changed.emit()
            
    value = Property(str, get_value, set_value, notify=changed)
            