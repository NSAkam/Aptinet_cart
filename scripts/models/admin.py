from PySide2.QtCore import QObject, Signal, Property


class AdminModel(QObject):
    _name: str = ""
    
    @Signal
    def changed(self):
        pass
    
    def __init__(self):
        super().__init__()
    
    def get_name(self):
        return self._name
    
    def set_name(self, value):
        self._name = value
        self.changed.emit()
        
    name = Property(str, get_name, set_name, notify=changed)
    
