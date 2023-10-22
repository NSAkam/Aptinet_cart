from PySide2.QtCore import QObject, Signal, Property


class Product(QObject):
    _name: str = ""
    _description: str = ""
    _rate: int = 0
    _commentCount: int = 0
    _w1: int = 0
    _w2: int = 0
    _w3: int = 0
    _w4: int = 0
    _w5: int = 0
    _w6: int = 0
    _w7: int = 0
    _w8: int = 0
    _w9: int = 0
    _w10: int = 0
    _price: int = 0
    _finalPrice: int = 0
    _meanWeight: int = 0
    _tolerance: int = 0
    _insertedWeight: int = 0
    _barcode: str = ""
    _isOffer: bool = False
    _isPlu: bool = False
    _tax: float = 0.0
    _qr: str = ""
    _taxPrice: int = 0
    
    def __init__(self):
        super().__init__()
        
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
            
    
    def getDescription(self):
        return self._description
        
    def setDescription(self, value):
        if value:
            self._description = value
            self.changed.emit()
            
    description = Property(str, getDescription, setDescription, notify=changed)
           
    def getRate(self):
        return self._rate
        
    def setRate(self, value):
        if value:
            self._rate = value
            self.changed.emit()
            
    rate = Property(int, getRate, setRate, notify=changed)
            
    
    def getCommentcount(self):
        return self._commentCount
        
    def setCommentcount(self, value):
        if value:
            self._commentCount = value
            self.changed.emit()
            
    commentCount = Property(int, getCommentcount, setCommentcount, notify=changed)
            
    def getW1(self):
        return self._w1
        
    def setW1(self, value):
        if value:
            self._w1 = value
            self.changed.emit()
            
    w1 = Property(int, getW1, setW1, notify=changed)
            
    def getW2(self):
        return self._w2
        
    def setW2(self, value):
        if value:
            self._w2 = value
            self.changed.emit()
            
    w2 = Property(int, getW2, setW2, notify=changed)
            
    def getW3(self):
        return self._w3
        
    def setW3(self, value):
        if value:
            self._w3 = value
            self.changed.emit()
            
    w3 = Property(int, getW3, setW3, notify=changed)
            
    def getW4(self):
        return self._w4
        
    def setW4(self, value):
        if value:
            self._w4 = value
            self.changed.emit()
            
    w4 = Property(int, getW4, setW4, notify=changed)
            
    def getW5(self):
        return self._w5
        
    def setW5(self, value):
        if value:
            self._w5 = value
            self.changed.emit()
            
    w5 = Property(int, getW5, setW5, notify=changed)
            
    
    def getW6(self):
        return self._w6
        
    def setW6(self, value):
        if value:
            self._w6 = value
            self.changed.emit()
            
    w6 = Property(int, getW6, setW6, notify=changed)
            
    
    def getW7(self):
        return self._w7
        
    def setW7(self, value):
        if value:
            self._w7 = value
            self.changed.emit()
            
    w7 = Property(int, getW7, setW7, notify=changed)
            
    
    def getW8(self):
        return self._w8
        
    def setW8(self, value):
        if value:
            self._w8 = value
            self.changed.emit()
            
    w8 = Property(int, getW8, setW8, notify=changed)
            
    
    def getW9(self):
        return self._w9
        
    def setW9(self, value):
        if value:
            self._w9 = value
            self.changed.emit()
            
    w9 = Property(int, getW9, setW9, notify=changed)
            
    
    def getW10(self):
        return self._w10
        
    def setW10(self, value):
        if value:
            self._w10 = value
            self.changed.emit()
            
    w10 = Property(int, getW10, setW10, notify=changed)
            
    
    def getPrice(self):
        return self._price
        
    def setPrice(self, value):
        if value:
            self._price = value
            self.changed.emit()
            
    price = Property(int, getPrice, setPrice, notify=changed)
            
    
    def getFinalprice(self):
        return self._finalPrice
        
    def setFinalprice(self, value):
        if value:
            self._finalPrice = value
            self.changed.emit()
            
    finalPrice = Property(int, getFinalprice, setFinalprice, notify=changed)
            
    
    def getMeanweight(self):
        return self._meanWeight
        
    def setMeanweight(self, value):
        if value:
            self._meanWeight = value
            self.changed.emit()
            
    meanWeight = Property(int, getMeanweight, setMeanweight, notify=changed)
            
    
    def getTolerance(self):
        return self._tolerance
        
    def setTolerance(self, value):
        if value:
            self._tolerance = value
            self.changed.emit()
            
    tolerance = Property(int, getTolerance, setTolerance, notify=changed)
            
    
    def getInsertedweight(self):
        return self._insertedWeight
        
    def setInsertedweight(self, value):
        if value:
            self._insertedWeight = value
            self.changed.emit()
            
    insertedWeight = Property(int, getInsertedweight, setInsertedweight, notify=changed)
            
    
    def getBarcode(self):
        return self._barcode
        
    def setBarcode(self, value):
        if value:
            self._barcode = value
            self.changed.emit()
            
    barcode = Property(int, getBarcode, setBarcode, notify=changed)
            
    def getIsoffer(self):
        return self._isOffer
        
    def setIsoffer(self, value):
        if value:
            self._isOffer = value
            self.changed.emit()
            
    isOffer = Property(int, getIsoffer, setIsoffer, notify=changed)
            
    
    def getIsplu(self):
        return self._isPlu
        
    def setIsplu(self, value):
        if value:
            self._isPlu = value
            self.changed.emit()
            
    isPlu = Property(int, getIsplu, setIsplu, notify=changed)
            
    
    def getTax(self):
        return self._tax
        
    def setTax(self, value):
        if value:
            self._tax = value
            self.changed.emit()
            
    tax = Property(int, getTax, setTax, notify=changed)

    
    def getTaxprice(self):
        return self._taxPrice
    
    def setTaxprice(self, value):
        self._taxPrice = value
        self.changed.emit()
        
    texPrice = Property(int, getTaxprice, setTaxprice, notify=changed)           
    
        