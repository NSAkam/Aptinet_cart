from PySide2.QtCore import QObject, Signal, Property


class UserFactoreModel(QObject):
    _count: int = 0
    _price: int = 0
    _finalPrice: int = 0
    _tax: int = 0
    _uId: int = 0
    _productBarcode: str = ""
    
    @Signal
    def changedSignal(self):
        pass
    
    def __init__(self):
        super().__init__()
        
    def get_count(self):
        return self._count
    
    def set_count(self, value):
        self._count = value
        self.changedSignal.emit()
            
    count = Property(int, get_count, set_count, notify=changedSignal)
    
    def get_price(self):
        return self._price
    
    def set_price(self, value):
        self._price = value
        self.changedSignal.emit()
            
    price = Property(int, set_price, get_price, notify=changedSignal)
    
    
    def get_finalPrice(self):
        return self._finalPrice
    
    def set_finalPrice(self, value):
        self._finalPrice = value
        self.changedSignal.emit()
            
    finalPrice = Property(str, get_finalPrice, set_finalPrice, notify=changedSignal)
    
    def get_tax(self):
        return self._tax
    
    def set_tax(self, value):
        self._tax = value
        self.changedSignal.emit()
            
    tax = Property(int, set_tax, get_tax, notify=changedSignal)
    
    
    def get_uId(self):
        return self._uId
    
    def set_uId(self, value):
            self._uId = value
            self.changedSignal.emit()
            
    uId = Property(int, set_uId, get_uId, notify=changedSignal)
    
    
    def get_productBarcode(self):
        return self._productBarcode
    
    def set_productBarcode(self, value):
        self._productBarcode = value
        self.changedSignal.emit()
            
    productBarcode = Property(str, get_productBarcode, set_productBarcode, notify=changedSignal)