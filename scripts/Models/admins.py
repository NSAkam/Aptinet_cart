from PySide2.QtCore import QObject, Signal, Property


class UserModel(QObject):
    _name: str = ""
    
    def __init__(self):
        super().__init__()
        
    @Signal
    def changed(self):
        pass
        
    def getName(self):
        return self._name
        
    def setName(self, value):
        if value:
            self._name = value
            self.changed.emit()
            
    name = Property(str, getName, setName, notify=changed)
    
        
   