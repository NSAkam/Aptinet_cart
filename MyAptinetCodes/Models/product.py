from PySide2.QtCore import QObject
from PySide2.QtCore import QObject, Signal, Property


class Product(QObject):

    _id: int
    _name: str
    _description: str
    _rate: int
    _CommentCount: int
    _price: int
    _finalprice: int
    _meanweight: int
    _tolerance: int
    _insertedweight: int
    _Barcode: str
    _isOffer: bool
    _isPLU: bool
    _tax: float
    _taxPrice: int
    _storeID: int
    _QR: str
    _w1: int
    _w2: int
    _w3: int
    _w4: int
    _w5: int
    _w6: int
    _w7: int
    _w8: int
    _w9: int
    _w10: int

    # Defining a Signal to notify a variable has been changed!
    changed = Signal()

    # Getter, Setter and Property for_id
    def getId(self):
        return self._id

    def setId(self, val):
        self._id = val
        self.changed.emit()

    idProperty = Property(int, getId, setId, notify=changed)

    # Getter, Setter and Property for _name
    def getName(self):
        return self._name

    def setName(self, val):
        self._name = val
        self.changed.emit()

    nameProperty = Property(str, getName, setName, notify=changed)

    # Getter, Setter and Property for _description
    def getDescription(self):
        return self._description

    def setDescription(self, val):
        self._description = val
        self.changed.emit()

    descriptionProperty = Property(str, getDescription, setDescription, notify=changed)

    # Getter, Setter and Property for rate
    def getRate(self):
        return self._rate

    def setRate(self, val):
        self._rate = val
        self.changed.emit()

    rateProperty = Property(int, getRate, setRate, notify=changed)

    # Getter, Setter and Property for CommentCount
    def getCommentCount(self):
        return self._CommentCount

    def setCommentCount(self, val):
        self._CommentCount = val
        self.changed.emit()

    CommentCountProperty = Property(int, getCommentCount, setCommentCount, notify=changed)

    # Getter, Setter and Property for price
    def getPrice(self):
        return self._price

    def setPrice(self, val):
        self._price = val
        self.changed.emit()

    priceProperty = Property(int, getPrice, setPrice, notify=changed)

    # Getter, Setter and Property for finalprice
    def getFinalprice(self):
        return self._finalprice

    def setFinalprice(self, val):
        self._finalprice = val
        self.changed.emit()

    finalpriceProperty = Property(int, getFinalprice, setFinalprice, notify=changed)

    # Getter, Setter and Property for meanweight
    def getMeanweight(self):
        return self._meanweight

    def setMeanweight(self, val):
        self._meanweight = val
        self.changed.emit()

    meanweightProperty = Property(int, getMeanweight, setMeanweight, notify=changed)

    # Getter, Setter and Property for tolerance
    def getTolerance(self):
        return self._tolerance

    def setTolerance(self, val):
        self._tolerance = val
        self.changed.emit()

    toleranceProperty = Property(int, getTolerance, setTolerance, notify=changed)

    # Getter, Setter and Property for insertedweight
    def getInsertedweight(self):
        return self._insertedweight

    def setInsertedweight(self, val):
        self._insertedweight = val
        self.changed.emit()

    insertedweightProperty = Property(int, getInsertedweight, setInsertedweight, notify=changed)

    # Getter, Setter and Property for Barcode
    def getBarcode(self):
        return self._Barcode

    def setBarcode(self, val):
        self._Barcode = val
        self.changed.emit()

    BarcodeProperty = Property(str, getBarcode, setBarcode, notify=changed)

    # Getter, Setter and Property for isOffer
    def getIsOffer(self):
        return self._isOffer

    def setIsOffer(self, val):
        self._isOffer = val
        self.changed.emit()

    isOfferProperty = Property(bool, getIsOffer, setIsOffer, notify=changed)

    # Getter, Setter and Property for isPLU
    def getIsPLU(self):
        return self._isPLU

    def setIsPLU(self, val):
        self._isPLU = val
        self.changed.emit()

    isPLUProperty = Property(bool, getIsPLU, setIsPLU, notify=changed)

    # Getter, Setter and Property for tax
    def getTax(self):
        return self._tax

    def setTax(self, val):
        self._tax = val
        self.changed.emit()

    taxProperty = Property(float, getTax, setTax, notify=changed)

    # Getter, Setter and Property for taxPrice
    def getTaxPrice(self):
        return self._taxPrice

    def setTaxPrice(self, val):
        self._taxPrice = val
        self.changed.emit()

    taxPriceProperty = Property(int, getTaxPrice, setTaxPrice, notify=changed)

    # Getter, Setter and Property for storeID
    def getStoreID(self):
        return self._storeID

    def setStoreID(self, val):
        self._storeID = val
        self.changed.emit()

    storeIDProperty = Property(int, getStoreID, setStoreID, notify=changed)

    # Getter, Setter and Property for QR
    def getQR(self):
        return self._QR

    def setQR(self, val):
        self._QR = val
        self.changed.emit()

    QRProperty = Property(str, getQR, setQR, notify=changed)

    # Getter, Setter and Property for w1
    def getW1(self):
        return self._w1

    def setW1(self, val):
        self._w1 = val
        self.changed.emit()

    w1Property = Property(int, getW1, setW1, notify=changed)

    # Getter, Setter and Property for w2

    def getW2(self):
        return self._w2

    def setW2(self, val):
        self._w2 = val
        self.changed.emit()

    w2Property = Property(int, getW2, setW2, notify=changed)

    # Getter, Setter and Property for w3
    def getW3(self):
        return self._w3

    def setW3(self, val):
        self._w3 = val
        self.changed.emit()

    w3Property = Property(int, getW3, setW3, notify=changed)

    # Getter, Setter and Property for w1
    def getW4(self):
        return self._w4

    def setW4(self, val):
        self._w4 = val
        self.changed.emit()

    w4Property = Property(int, getW4, setW4, notify=changed)

    # Getter, Setter and Property for w5
    def getW5(self):
        return self._w5

    def setW5(self, val):
        self._w5 = val
        self.changed.emit()

    w5Property = Property(int, getW5, setW5, notify=changed)

    # Getter, Setter and Property for w6
    def getW6(self):
        return self._w6

    def setW6(self, val):
        self._w6 = val
        self.changed.emit()

    w6Property = Property(int, getW6, setW6, notify=changed)

    # Getter, Setter and Property for w7
    def getW7(self):
        return self._w7

    def setW7(self, val):
        self._w7 = val
        self.changed.emit()

    w7Property = Property(int, getW7, setW7, notify=changed)

    # Getter, Setter and Property for w8
    def getW8(self):
        return self._w8

    def setW8(self, val):
        self._w8 = val
        self.changed.emit()

    w8Property = Property(int, getW8, setW8, notify=changed)

    # Getter, Setter and Property for w9
    def getW9(self):
        return self._w9

    def setW9(self, val):
        self._w9 = val
        self.changed.emit()

    w9Property = Property(int, getW9, setW9, notify=changed)

    # Getter, Setter and Property for w10
    def getW10(self):
        return self._w10

    def setW10(self, val):
        self._w10 = val
        self.changed.emit()

    w10Property = Property(int, getW10, setW10, notify=changed)









