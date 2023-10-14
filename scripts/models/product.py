from PySide2.QtCore import QObject, Signal, Property


class Product(QObject):
    _name: str = ""
    _description: str = ""
    _rate: int = 0
    _comment_count: int = 0
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
    _final_price: int = 0
    _mean_weight: int = 0
    _tolerance: int = 0
    _inserted_weight: int = 0
    _barcode: str = ""
    _is_offer: bool = False
    _is_plu: bool = False
    _tax: float = 0.0
    _qr: str = ""
    
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
            
    read_name = Property(str, get_name, set_name, notify=changed)
            
    def get_description(self):
        return self._description
        
    def set_description(self, value):
        if value:
            self._description = value
            self.changed.emit()
            
    read_description = Property(str, get_description, set_description, notify=changed)
            
    def get_rate(self):
        return self._rate
        
    def set_rate(self, value):
        if value:
            self._rate = value
            self.changed.emit()
            
    read_rate = Property(int, get_rate, set_rate, notify=changed)
            
    def get_comment_count(self):
        return self._comment_count
        
    def set_comment_count(self, value):
        if value:
            self._comment_count = value
            self.changed.emit()
            
    read_comment_count = Property(int, get_comment_count, set_comment_count, notify=changed)
            
    def get_w1(self):
        return self._w1
        
    def set_w1(self, value):
        if value:
            self._w1 = value
            self.changed.emit()
            
    read_w1 = Property(int, get_w1, set_w1, notify=changed)
            
    def get_w2(self):
        return self._w2
        
    def set_w2(self, value):
        if value:
            self._w2 = value
            self.changed.emit()
            
    read_w2 = Property(int, get_w2, set_w2, notify=changed)
            
    def get_w3(self):
        return self._w3
        
    def set_w3(self, value):
        if value:
            self._w3 = value
            self.changed.emit()
            
    read_w3 = Property(int, get_w3, set_w3, notify=changed)
            
    def get_w4(self):
        return self._w4
        
    def set_w4(self, value):
        if value:
            self._w4 = value
            self.changed.emit()
            
    read_w4 = Property(int, get_w4, set_w4, notify=changed)
            
    def get_w5(self):
        return self._w5
        
    def set_w5(self, value):
        if value:
            self._w5 = value
            self.changed.emit()
            
    read_w5 = Property(int, get_w5, set_w5, notify=changed)
            
    def get_w6(self):
        return self._w6
        
    def set_w6(self, value):
        if value:
            self._w6 = value
            self.changed.emit()
            
    read_w6 = Property(int, get_w6, set_w6, notify=changed)
            
    def get_w7(self):
        return self._w7
        
    def set_w7(self, value):
        if value:
            self._w7 = value
            self.changed.emit()
            
    read_w7 = Property(int, get_w7, set_w7, notify=changed)
            
    def get_w8(self):
        return self._w8
        
    def set_w8(self, value):
        if value:
            self._w8 = value
            self.changed.emit()
            
    read_w8 = Property(int, get_w8, set_w8, notify=changed)
            
    def get_w9(self):
        return self._w9
        
    def set_w9(self, value):
        if value:
            self._w9 = value
            self.changed.emit()
            
    read_w9 = Property(int, get_w9, set_w9, notify=changed)
            
    def get_w10(self):
        return self._w10
        
    def set_w10(self, value):
        if value:
            self._w10 = value
            self.changed.emit()
            
    read_w10 = Property(int, get_w10, set_w10, notify=changed)
            
    def get_price(self):
        return self._price
        
    def set_price(self, value):
        if value:
            self._price = value
            self.changed.emit()
            
    read_price = Property(int, get_price, set_price, notify=changed)
            
    def get_final_price(self):
        return self._final_price
        
    def set_final_price(self, value):
        if value:
            self._final_price = value
            self.changed.emit()
            
    read_final_price = Property(int, get_final_price, set_final_price, notify=changed)
            
    def get_mean_weight(self):
        return self._mean_weight
        
    def set_mean_weight(self, value):
        if value:
            self._mean_weight = value
            self.changed.emit()
            
    read_mean_weight = Property(int, get_mean_weight, set_mean_weight, notify=changed)
            
    def get_tolerance(self):
        return self._tolerance
        
    def set_tolerance(self, value):
        if value:
            self._tolerance = value
            self.changed.emit()
            
    read_tolerance = Property(int, get_tolerance, set_tolerance, notify=changed)
            
    def get_inserted_weight(self):
        return self._inserted_weight
        
    def set_inserted_weight(self, value):
        if value:
            self._inserted_weight = value
            self.changed.emit()
            
    read_inserted_weight = Property(int, get_inserted_weight, set_inserted_weight, notify=changed)
            
    def get_barcode(self):
        return self._barcode
        
    def set_barcode(self, value):
        if value:
            self._barcode = value
            self.changed.emit()
            
    read_barcode = Property(int, get_barcode, set_barcode, notify=changed)
            
    def get_is_offer(self):
        return self._is_offer
        
    def set_is_offer(self, value):
        if value:
            self._is_offer = value
            self.changed.emit()
            
    read_is_offer = Property(int, get_is_offer, set_is_offer, notify=changed)
            
    def get_is_plu(self):
        return self._is_plu
        
    def set_is_plu(self, value):
        if value:
            self._is_plu = value
            self.changed.emit()
            
    read_plu = Property(int, get_is_plu, set_is_plu, notify=changed)
            
    def get_tax(self):
        return self._tax
        
    def set_tax(self, value):
        if value:
            self._tax = value
            self.changed.emit()
            
    read_tax = Property(int, get_tax, set_tax, notify=changed)
            
    
        