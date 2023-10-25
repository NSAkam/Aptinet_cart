from PySide2.QtCore import QObject, Signal, Property


class SuggestionModel(QObject):
    _pBarcode: str = ""
    _psBarcode: str = ""
    
    @Signal
    def changedSignal(self):
        pass
    
    def __init__(self):
        super().__init__()
    
    def get_pBarode(self):
        return self._pBarcode
    
    def set_pBarcode(self, value):
        self._pBarcode = value
        self.changedSignal.emit()
        
    pBarcode = Property(str, get_pBarode, set_pBarcode, notify=changedSignal)
    
    def get_PsBarcode(self):
        return self._psBarcode
    
    def set_PsBarcode(self, value):
        self._psBarcode = value
        self.changedSignal.emit()
        
    psBarcode = Property(str, get_PsBarcode, set_PsBarcode, notify=changedSignal)