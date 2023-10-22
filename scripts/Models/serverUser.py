from PySide2.QtCore import QObject, Signal, Property


class Admins(QObject):
    _name: str = ""
    _email: str = ""
    _phone: str = ""
    _offer: float = 0
    _code: str = ""
    
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
    
    def getEmail(self):
        return self._email
    
    def setEmail(self, value):
        if value:
            self._email = value
            self.changed.emit()
        
    email = Property(str, getEmail, setEmail, notify=changed)
    
    def getPhone(self):
        return self._phone
    
    def setPhone(self, value):
        if value:
            self._phone = value
            
    phone = Property(str, getPhone, setPhone, notify=changed)
    
    def getOffer(self):
        return self._offer
    
    def setOffer(self, value):
        if value:
            self._offer = value
            self.changed.emit()
            
    offer = Property(float, getOffer, setOffer, notify=changed)
    
    
    def getCode(self):
        return self._code
    
    def setCode(self, value):
        if value:
            self._code = value
            self.changed.emit()
            
    code = Property(str, getCode, setCode, notify=changed)
    
    