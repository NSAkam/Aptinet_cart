from PySide2.QtCore import QObject, Signal, Property


class LoggsModel(QObject):
    _count: int = 0
    _price: int = 0
    _finalprice: int = 0
    _tax: int = 0
    
    @Signal
    def changed(self):
        pass
    
    def __init__(self):
        super().__init__()
        
    def get_count(self):
        return self._count
    
    def set_count(self, value):
        if value:
            self._count = value
            self.changed.emit()
            
    count = Property(int, get_count, set_count, notify=changed)
    
    def get_price(self):
        return self._action
    
    def set_price(self, value):
        if value:
            self._price = value
            self.changed.emit()
            
    price = Property(int, set_price, get_price, notify=changed)
    
    def get_finalprice(self):
        return self._finalprice
    
    def set_finalprice(self, value):
        if value:
            self._finalprice = value
            self.changed.emit()
            
    finalprice = Property(str, get_finalprice, set_finalprice, notify=changed)
    
    def get_tax(self):
        return self._tax
    
    def set_tax(self, value):
        if value:
            self._tax = value
            self.changed.emit()
            
    tax = Property(int, set_tax, get_tax, notify=changed)