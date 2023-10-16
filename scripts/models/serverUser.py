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
    
    def get_name(self):
        return self._name
    
    def set_name(self, value):
        if value:
            self._name = value
            self.changed.emit()
            
    name = Property(str, get_name, set_name, notify=changed)
    
    def get_email(self):
        return self._email
    
    def set_email(self, value):
        if value:
            self._email = value
            self.changed.emit()
        
    email = Property(str, get_email, set_email, notify=changed)
    
    def get_phone(self):
        return self._phone
    
    def set_phone(self, value):
        if value:
            self._phone = value
            
    phone = Property(str, get_phone, set_phone, notify=changed)
    
    def get_offer(self):
        return self._offer
    
    def set_offer(self, value):
        if value:
            self._offer = value
            self.changed.emit()
            
    offer = Property(float, get_offer, set_offer, notify=changed)
    
    
    def get_code(self):
        return self._code
    
    def set_code(self, value):
        if value:
            self._code = value
            self.changed.emit()
            
    code = Property(str, get_code, set_code, notify=changed)
    
    