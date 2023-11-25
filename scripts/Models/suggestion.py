from PySide2.QtCore import QObject, Signal, Property


class SuggestionModel(QObject):
    _Productid: str = ""
    _Productidsuggested: str = ""
    
    @Signal
    def changedSignal(self):
        pass
    
    def __init__(self):
        super().__init__()
    
    def get_pBarode(self):
        return self._Productid
    
    def set_Productid(self, value):
        self._Productid = value
        self.changedSignal.emit()
        
    Productid = Property(str, get_pBarode, set_Productid, notify=changedSignal)
    
    def get_Productidsuggested(self):
        return self._Productidsuggested
    
    def set_Productidsuggested(self, value):
        self._Productidsuggested = value
        self.changedSignal.emit()
        
    Productidsuggested = Property(str, get_Productidsuggested, set_Productidsuggested, notify=changedSignal)