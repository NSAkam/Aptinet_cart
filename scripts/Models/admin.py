from PySide2.QtCore import QObject, Signal, Property


class Admin(QObject):
    _barcode:str = ""
    _name: str = ""
    
    @Signal
    def changedSignal(self):
        pass
    
    def __init__(self):
        super().__init__()
    
    def get_name(self):
        return self._name
    
    def set_name(self, value):
        self._name = value
        self.changedSignal.emit()
        
    name = Property(str, get_name, set_name, notify=changedSignal)

    def get_barcode(self):
        return self._barcode
    
    def set_barcode(self, value):
        self._barcode = value
        self.changedSignal.emit()
        
    barcode = Property(str, get_barcode, set_barcode, notify=changedSignal)
    
