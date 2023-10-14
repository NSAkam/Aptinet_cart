from PySide2.QtCore import QObject
from PySide2.QtCore import QObject, Signal, Property



class Product(QObject):

    id: int
    name: str
    description: str
    rate: int
    CommentCount: int
    price: int
    finalprice: int
    meanweight: int
    tolerance: int
    insertedweight: int
    Barcode: str
    isOffer: bool
    isPLU: bool
    tax: float
    storeID: int
    QR: str
    w1: int
    w2: int
    w3: int
    w4: int
    w5: int
    w6: int
    w7: int
    w8: int
    w9: int
    w10: int

    # Defining a Signal to notify a variable has been changed!
    changed = Signal()

    # Getter, Setter and Property for id
    def getId(self):
        return self.id

    def setId(self, val):
        self.id = val
        self.changed.emit()

    idProperty = Property(int, getId, setId, notify=changed)

    # Getter, Setter and Property for name
    def getName(self):
        return self.name

    def setName(self, val):
        self.name = val
        self.changed.emit()

    nameProperty = Property(str, getName, setName, notify=changed)

    # Getter, Setter and Property for description
    def getDescription(self):
        return self.description

    def setDescription(self, val):
        self.description = val
        self.changed.emit()

    descriptionProperty = Property(str, getDescription, setDescription, notify=changed)

    # Getter, Setter and Property for rate
    def getRate(self):
        return self.rate

    def setRate(self, val):
        self.rate = val
        self.changed.emit()

    rateProperty = Property(int, getRate, setRate, notify=changed)

    # Getter, Setter and Property for CommentCount
    def getCommentCount(self):
        return self.CommentCount

    def setCommentCount(self, val):
        self.CommentCount = val
        self.changed.emit()

    CommentCountProperty = Property(int, getCommentCount, setCommentCount, notify=changed)

    # Getter, Setter and Property for price
    def getPrice(self):
        return self.price

    def setPrice(self, val):
        self.price = val
        self.changed.emit()

    priceProperty = Property(int, getPrice, setPrice, notify=changed)

    # Getter, Setter and Property for finalprice
    def getFinalprice(self):
        return self.finalprice

    def setFinalprice(self, val):
        self.finalprice = val
        self.changed.emit()

    finalpriceProperty = Property(int, getFinalprice, setFinalprice, notify=changed)

    # Getter, Setter and Property for meanweight
    def getMeanweight(self):
        return self.meanweight

    def setMeanweight(self, val):
        self.meanweight = val
        self.changed.emit()

    meanweightProperty = Property(int, getMeanweight, setMeanweight, notify=changed)

    # Getter, Setter and Property for tolerance
    def getTolerance(self):
        return self.tolerance

    def setTolerance(self, val):
        self.tolerance = val
        self.changed.emit()

    toleranceProperty = Property(int, getTolerance, setTolerance, notify=changed)

    # Getter, Setter and Property for insertedweight
    def getInsertedweight(self):
        return self.insertedweight

    def setInsertedweight(self, val):
        self.insertedweight = val
        self.changed.emit()

    insertedweightProperty = Property(int, getInsertedweight, setInsertedweight, notify=changed)

    # Getter, Setter and Property for Barcode
    def getBarcode(self):
        return self.Barcode

    def setBarcode(self, val):
        self.Barcode = val
        self.changed.emit()

    BarcodeProperty = Property(str, getBarcode, setBarcode, notify=changed)

    # Getter, Setter and Property for isOffer
    def getIsOffer(self):
        return self.isOffer

    def setIsOffer(self, val):
        self.isOffer = val
        self.changed.emit()

    isOfferProperty = Property(bool, getIsOffer, setIsOffer, notify=changed)

    # Getter, Setter and Property for isPLU
    def getIsPLU(self):
        return self.isPLU

    def setIsPLU(self, val):
        self.isPLU = val
        self.changed.emit()

    isPLUProperty = Property(bool, getIsPLU, setIsPLU, notify=changed)

    # Getter, Setter and Property for tax
    def getTax(self):
        return self.tax

    def setTax(self, val):
        self.tax = val
        self.changed.emit()

    taxProperty = Property(float, getTax, setTax, notify=changed)

    # Getter, Setter and Property for storeID
    def getStoreID(self):
        return self.storeID

    def setStoreID(self, val):
        self.storeID = val
        self.changed.emit()

    storeIDProperty = Property(int, getStoreID, setStoreID, notify=changed)

    # Getter, Setter and Property for QR
    def getQR(self):
        return self.QR

    def setQR(self, val):
        self.QR = val
        self.changed.emit()

    QRProperty = Property(str, getQR, setQR, notify=changed)

    # Getter, Setter and Property for w1
    def getW1(self):
        return self.w1

    def setW1(self, val):
        self.w1 = val
        self.changed.emit()

    w1Property = Property(int, getW1, setW1, notify=changed)

    # Getter, Setter and Property for w2

    def getW2(self):
        return self.w2

    def setW2(self, val):
        self.w2 = val
        self.changed.emit()

    w2Property = Property(int, getW2, setW2, notify=changed)

    # Getter, Setter and Property for w3
    def getW3(self):
        return self.w3

    def setW3(self, val):
        self.w3 = val
        self.changed.emit()

    w3Property = Property(int, getW3, setW3, notify=changed)

    # Getter, Setter and Property for w1
    def getW4(self):
        return self.w4

    def setW4(self, val):
        self.w4 = val
        self.changed.emit()

    w4Property = Property(int, getW4, setW4, notify=changed)

    # Getter, Setter and Property for w5
    def getW5(self):
        return self.w5

    def setW5(self, val):
        self.w5 = val
        self.changed.emit()

    w5Property = Property(int, getW5, setW5, notify=changed)

    # Getter, Setter and Property for w6
    def getW6(self):
        return self.w6

    def setW6(self, val):
        self.w6 = val
        self.changed.emit()

    w6Property = Property(int, getW6, setW6, notify=changed)

    # Getter, Setter and Property for w7
    def getW7(self):
        return self.w7

    def setW7(self, val):
        self.w7 = val
        self.changed.emit()

    w7Property = Property(int, getW7, setW7, notify=changed)

    # Getter, Setter and Property for w8
    def getW8(self):
        return self.w8

    def setW8(self, val):
        self.w8 = val
        self.changed.emit()

    w8Property = Property(int, getW8, setW8, notify=changed)

    # Getter, Setter and Property for w9
    def getW9(self):
        return self.w9

    def setW9(self, val):
        self.w9 = val
        self.changed.emit()

    w9Property = Property(int, getW9, setW9, notify=changed)

    # Getter, Setter and Property for w10
    def getW10(self):
        return self.w10

    def setW10(self, val):
        self.w10 = val
        self.changed.emit()

    w10Property = Property(int, getW10, setW10, notify=changed)









