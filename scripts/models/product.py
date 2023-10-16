from PySide2.QtCore import QObject, Signal, Property


class Product(QObject):
    _name: str = ""
    _description: str = ""
    _rate: int = 0
    _commentcount: int = 0
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
    _finalprice: int = 0
    _meanweight: int = 0
    _tolerance: int = 0
    _insertedweight: int = 0
    _barcode: str = ""
    _isoffer: bool = False
    _isplu: bool = False
    _tax: float = 0.0
    _qr: str = ""
    _taxprice: int = 0
    
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
            
    name = Property(str, get_name, set_name, notify=changed)
            
    def get_description(self):
        return self._description
        
    def set_description(self, value):
        if value:
            self._description = value
            self.changed.emit()
            
    description = Property(str, get_description, set_description, notify=changed)
           
    def get_rate(self):
        return self._rate
        
    def set_rate(self, value):
        if value:
            self._rate = value
            self.changed.emit()
            
    rate = Property(int, get_rate, set_rate, notify=changed)
            
    def get_commentcount(self):
        return self._commentcount
        
    def set_commentcount(self, value):
        if value:
            self._commentcount = value
            self.changed.emit()
            
    commentcount = Property(int, get_commentcount, set_commentcount, notify=changed)
            
    def get_w1(self):
        return self._w1
        
    def set_w1(self, value):
        if value:
            self._w1 = value
            self.changed.emit()
            
    w1 = Property(int, get_w1, set_w1, notify=changed)
            
    def get_w2(self):
        return self._w2
        
    def set_w2(self, value):
        if value:
            self._w2 = value
            self.changed.emit()
            
    w2 = Property(int, get_w2, set_w2, notify=changed)
            
    def get_w3(self):
        return self._w3
        
    def set_w3(self, value):
        if value:
            self._w3 = value
            self.changed.emit()
            
    w3 = Property(int, get_w3, set_w3, notify=changed)
            
    def get_w4(self):
        return self._w4
        
    def set_w4(self, value):
        if value:
            self._w4 = value
            self.changed.emit()
            
    w4 = Property(int, get_w4, set_w4, notify=changed)
            
    def get_w5(self):
        return self._w5
        
    def set_w5(self, value):
        if value:
            self._w5 = value
            self.changed.emit()
            
    w5 = Property(int, get_w5, set_w5, notify=changed)
            
    def get_w6(self):
        return self._w6
        
    def set_w6(self, value):
        if value:
            self._w6 = value
            self.changed.emit()
            
    w6 = Property(int, get_w6, set_w6, notify=changed)
            
    def get_w7(self):
        return self._w7
        
    def set_w7(self, value):
        if value:
            self._w7 = value
            self.changed.emit()
            
    w7 = Property(int, get_w7, set_w7, notify=changed)
            
    def get_w8(self):
        return self._w8
        
    def set_w8(self, value):
        if value:
            self._w8 = value
            self.changed.emit()
            
    w8 = Property(int, get_w8, set_w8, notify=changed)
            
    def get_w9(self):
        return self._w9
        
    def set_w9(self, value):
        if value:
            self._w9 = value
            self.changed.emit()
            
    w9 = Property(int, get_w9, set_w9, notify=changed)
            
    def get_w10(self):
        return self._w10
        
    def set_w10(self, value):
        if value:
            self._w10 = value
            self.changed.emit()
            
    w10 = Property(int, get_w10, set_w10, notify=changed)
            
    def get_price(self):
        return self._price
        
    def set_price(self, value):
        if value:
            self._price = value
            self.changed.emit()
            
    price = Property(int, get_price, set_price, notify=changed)
            
    def get_finalprice(self):
        return self._final_price
        
    def set_finalprice(self, value):
        if value:
            self._finalprice = value
            self.changed.emit()
            
    finalprice = Property(int, get_finalprice, set_finalprice, notify=changed)
            
    def get_meanweight(self):
        return self._meanweight
        
    def set_meanweight(self, value):
        if value:
            self._meanweight = value
            self.changed.emit()
            
    meanweight = Property(int, get_meanweight, set_meanweight, notify=changed)
            
    def get_tolerance(self):
        return self._tolerance
        
    def set_tolerance(self, value):
        if value:
            self._tolerance = value
            self.changed.emit()
            
    tolerance = Property(int, get_tolerance, set_tolerance, notify=changed)
            
    def get_insertedweight(self):
        return self._insertedweight
        
    def set_insertedweight(self, value):
        if value:
            self._insertedweight = value
            self.changed.emit()
            
    insertedweight = Property(int, get_insertedweight, set_insertedweight, notify=changed)
            
    def get_barcode(self):
        return self._barcode
        
    def set_barcode(self, value):
        if value:
            self._barcode = value
            self.changed.emit()
            
    barcode = Property(int, get_barcode, set_barcode, notify=changed)
            
    def get_isoffer(self):
        return self._isoffer
        
    def set_isoffer(self, value):
        if value:
            self._isoffer = value
            self.changed.emit()
            
    isoffer = Property(int, get_isoffer, set_isoffer, notify=changed)
            
    def get_isplu(self):
        return self._isplu
        
    def set_isplu(self, value):
        if value:
            self._isplu = value
            self.changed.emit()
            
    plu = Property(int, get_isplu, set_isplu, notify=changed)
            
    def get_tax(self):
        return self._tax
        
    def set_tax(self, value):
        if value:
            self._tax = value
            self.changed.emit()
            
    tax = Property(int, get_tax, set_tax, notify=changed)

    def get_taxprice(self):
        return self._taxprice
    
    def set_taxprice(self, value):
        self._taxprice = value
        self.changed.emit()
        
    texprice = Property(int, get_taxprice, set_taxprice, notify=changed)           
    
        