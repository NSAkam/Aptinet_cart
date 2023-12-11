from PySide2.QtCore import QObject, Signal, Property
import os


class ServerUser(QObject):
    _id:str = ""
    _loyalityBarcode:str=""
    _name: str = ""
    _email: str = ""
    _phone: str = ""
    _offerPercentage:str=""
    _offerLimitedPercentage:str = ""
    _offerMount:str = ""
    
    @Signal
    def changedSignal(self):
        pass

    def get_id(self):
        return self._id
    
    def set_id(self, value):
        self._id = value
        self.changedSignal.emit()
            
    id = Property(str, get_id, set_id, notify=changedSignal)

    def get_loyalityBarcode(self):
        return self._loyalityBarcode
    
    def set_loyalityBarcode(self, value):
        self._loyalityBarcode = value
        self.changedSignal.emit()
            
    loyalityBarcode = Property(str, get_loyalityBarcode, set_loyalityBarcode, notify=changedSignal)
    
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

    def get_pic(self):
        if (os.path.isfile("/home/aptinet/files/" + self.phone + ".png") == False):
            return "file:///home/aptinet/files/guest.png"
        else:
            return "file:///home/aptinet/files/" + self.phone + ".png"

    pic = Property(str, get_pic, notify=changedSignal)

    def get_offerPercentage(self):
        return self._offerPercentage
    
    def set_offerPercentage(self, value):
        self._offerPercentage = value
        self.changedSignal.emit()
            
    offerPercentage = Property(str, get_offerPercentage, set_offerPercentage, notify=changedSignal)

    def get_offerLimitedPercentage(self):
        return self._offerLimitedPercentage
    
    def set_offerLimitedPercentage(self, value):
        self._offerLimitedPercentage = value
        self.changedSignal.emit()
            
    offerLimitedPercentage = Property(str, get_offerLimitedPercentage, set_offerLimitedPercentage, notify=changedSignal)

    def get_offerMount(self):
        return self._offerMount
    
    def set_offerMount(self, value):
        self._offerMount = value
        self.changedSignal.emit()
            
    offerMount = Property(str, get_offerMount, set_offerMount, notify=changedSignal)
    
    