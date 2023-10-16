from PySide2.QtCore import QObject
from PySide2.QtCore import QObject, Signal, Property


class userFactorModel(QObject):

    _count: int = 0
    _price: int
    _finalPrice: int = 0

    def __int__(self):
        super().__init__()

    changed = Signal()

    def getCount(self):
        return self._count

    def setCount(self, val):
        self._count = val
        self.changed.emit()

    countProperty = Property(int, getCount, setCount, notify=changed)

    def getPrice(self):
        return self._price

    def setPrice(self, val):
        self._price = val
        self.changed.emit()

    priceProperty = Property(int, getPrice, setPrice, notify=changed)

    def getFinalPrice(self):
        return self._finalPrice

    def setFinalPrice(self, val):
        self._finalPrice = val
        self.changed.emit()

    finalPriceProperty = Property(int, getFinalPrice, setFinalPrice, notify=changed)

