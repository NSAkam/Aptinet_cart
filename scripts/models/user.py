from PySide2.QtCore import QObject, Signal, Property


class User(QObject):
    _name: str = ""
    _email: str = ""
    _phone: str = ""
    _offer: float = 0
    _code: str = ""
    
    def __init__(self):
        super().__init__()
        
    @Signal
    def changed(self):
        pass
        
    def get_name(self):
        return self._name
        
    def set_name(self, value):
        if value:
            self._name = value
            self.changed.emit()
            
    read_user_name = Property(str, get_name, set_name, notify=changed)
    
    def __init__(self):
        super().__init__()
        
    def get_emial(self):
        return self._email
        
    def set_email(self, value):
        if value:
            self._email = value
            self.changed.emit()
            
    read_email = Property(str, get_emial, set_email, notify=changed)
    
    def get_phone(self):
        return self._phone
        
    def set_phone(self, value):
        if value:
            self._phone = value
            self.changed.emit()
            
    read_phone = Property(str, get_phone, set_phone, notify=changed)
    
    def get_offer(self):
        return self._offer
        
    def set_offer(self, value):
        if value:
            self._offer = value
            self.changed.emit()
            
    read_offer = Property(float, get_offer, set_offer, notify=changed)
    
    def get_code(self):
        return self._code
        
    def set_code(self, value):
        if value:
            self._code = value
            self.changed.emit()
            
    read_code = Property(str, get_code, set_code, notify=changed)