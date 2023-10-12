from PySide2.QtCore import QObject, Property, Signal, Slot

class Scanner(QObject):
    
    @Signal
    def changed(self):
        pass
    
    def __init__(self, name, type, model) -> None:
        super().__init__()
        self._name = name
        self._type = type
        self._model = model
    
    def get_name(self):
        return self._name
    
    def set_name(self, value):
        self._name = value
        self.changed.emit()
        
    read_name = Property(str, set_name, get_name, notify=changed)
 
    def get_type(self):
        return self._type
    
    def set_type(self, value):
        self._type = value
        self.changed.emit()
        
    read_type = Property(int, set_type, get_type, notify=changed)
        
    def get_model(self):
        return self._model
    
    def set_model(self, value):
        self._model = value
        self.changed.emit()
        
    read_model = Property(int, set_model, get_model, notify=changed)
    
