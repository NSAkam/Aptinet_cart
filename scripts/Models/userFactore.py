from PySide2.QtCore import QObject, Signal, Property


class UserFactoreModel(QObject):
    _count: int = 0
    _price: int = 0
    _finalPrice: int = 0
    _tax: int = 0
    _uId: int = 0
    _productBarcode: str = ""
    
    @Signal
    def changed(self):
        pass
    
    def __init__(self):
        super().__init__()
        
    def getCount(self):
        return self._count
    
    def setCount(self, value):
        if value:
            self._count = value
            self.changed.emit()
            
    count = Property(int, getCount, setCount, notify=changed)
    
    def getPrice(self):
        return self._price
    
    def setPrice(self, value):
        if value:
            self._price = value
            self.changed.emit()
            
    price = Property(int, setPrice, getPrice, notify=changed)
    
    
    def getFinalprice(self):
        return self._finalPrice
    
    def setFinalprice(self, value):
        if value:
            self._finalPrice = value
            self.changed.emit()
            
    finalPrice = Property(str, getFinalprice, setFinalprice, notify=changed)
    
    def getTax(self):
        return self._tax
    
    def setTax(self, value):
        if value:
            self._tax = value
            self.changed.emit()
            
    tax = Property(int, setTax, getTax, notify=changed)
    
    
    def getUid(self):
        return self._uId
    
    def setUid(self, value):
        if value:
            self._uId = value
            self.changed.emit()
            
    uId = Property(int, setUid, getUid, notify=changed)
    
    
    def getProductbarcode(self):
        return self._productBarcode
    
    def setProductbarcode(self, value):
        if value:
            self._productBarcode = value
            self.changed.emit()
            
    productBarcode = Property(str, getProductbarcode, setProductbarcode, notify=changed)