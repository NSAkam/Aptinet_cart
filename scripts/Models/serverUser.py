from PySide2.QtCore import QObject, Signal, Property


class ServerUser(QObject):
    _name: str = ""
    _email: str = ""
    _phone: str = ""
    _offer: float = 0
    _code: str = ""
    
    @Signal
    def changedSignal(self):
        pass
    
    def get_name(self):
        return self._name
    
    def set_name(self, value):
        self._name = value
        self.changedSignal.emit()
            
    name = Property(str, get_name, set_name, notify=changedSignal)
    
    def get_email(self):
        return self._email
    
    def set_email(self, value):
        self._email = value
        self.changedSignal.emit()
        
    email = Property(str, get_email, set_email, notify=changedSignal)
    
    def get_phone(self):
        return self._phone
    
    def set_phone(self, value):
        self._phone = value
        self.changedSignal.emit()
            
    phone = Property(str, get_phone, set_phone, notify=changedSignal)
    
    def get_offer(self):
        return self._offer
    
    def set_offer(self, value):
        self._offer = value
        self.changedSignal.emit()
            
    offer = Property(float, get_offer, set_offer, notify=changedSignal)
    
    
    def get_code(self):
        return self._code
    
    def set_code(self, value):
        self._code = value
        self.changedSignal.emit()
            
    code = Property(str, get_code, set_code, notify=changedSignal)
    
    