from PySide2.QtCore import QObject, Signal, Property


class SuggestionModel(QObject):
    _pBarcode: str = ""
    _psBarcode: str = ""
    
    @Signal
    def changed(self):
        pass
    
    def __init__(self):
        super().__init__()
    
    def getPbarcode(self):
        return self._pBarcode
    
    def setPbarcode(self, value):
        self._pBarcode = value
        self.changed.emit()
        
    pBarcode = Property(str, getPbarcode, setPbarcode, notify=changed)
    
    def getPsbarcode(self):
        return self._psBarcode
    
    def setPsbarcode(self, value):
        self._psBarcode = value
        self.changed.emit()
        
    psBarcode = Property(str, getPsbarcode, setPsbarcode, notify=changed)