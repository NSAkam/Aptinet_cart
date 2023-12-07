import os
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
    _price: float = 0
    _finalPrice: float = 0
    _meanWeight: int = 0
    _tolerance: int = 0
    _insertedWeight: int = 0
    _barcode: str = ""
    _isOffer: bool = False
    _isPlu: bool = False
    _tax: bool = False
    _QR: str = ""

    # if (barcode.Length == 13)
    # {
    #     return "normal";
    # }
    # else if (barcode.Length < 13 && isPlu == true)
    # {
    #     return "weighted";
    # }
    # else if (barcode.Length < 13 && isPlu == false)
    # {
    #     return "counted";
    # }

    _productType: str = ""

    _dataModelShow: int = 0  #  0 is normal and counted 1 is PLU
    _productWeightInBasket: int = 0
    _countInBasket: int = 0

    _Qprice: str = ""
    _Qweigh: str = ""
    _quantifier: str = ""
    _taxPercentage: bool = 0

    def __init__(self):
        super().__init__()

    @Signal
    def changedSignal(self):
        pass

    def get_name(self):
        return self._name

    def set_name(self, value):
        self._name = value
        self.changedSignal.emit()

    name = Property(str, get_name, set_name, notify=changedSignal)

    def get_description(self):
        return self._description

    def set_description(self, value):
        self._description = value
        self.changedSignal.emit()

    description = Property(str, get_description,
                           set_description, notify=changedSignal)

    def get_rate(self):
        return self._rate

    def set_rate(self, value):
        self._rate = value
        self.changedSignal.emit()

    rate = Property(int, get_rate, set_rate, notify=changedSignal)

    def get_commentCount(self):
        return self._commentCount

    def set_commentCount(self, value):
        self._commentCount = value
        self.changedSignal.emit()

    commentCount = Property(int, get_commentCount,
                            set_commentCount, notify=changedSignal)

    def getpic(self):
        if (os.path.isfile("/home/aptinet/pics/" + self.get_barcode() + ".png") == False):
            return "file:///home/aptinet/pics/DefaultProduct.png"
        else:
            return "file:///home/aptinet/pics/" + self.get_barcode() + ".png"

    pic = Property(str, getpic, notify=changedSignal)

    def get_w1(self):
        return self._w1

    def set_w1(self, value):
        self._w1 = value
        self.changedSignal.emit()

    w1 = Property(int, get_w1, set_w1, notify=changedSignal)

    def get_w2(self):
        return self._w2

    def set_w2(self, value):
        if value:
            self._w2 = value
            self.changedSignal.emit()

    w2 = Property(int, get_w2, set_w2, notify=changedSignal)

    def get_w3(self):
        return self._w3

    def set_w3(self, value):
        self._w3 = value
        self.changedSignal.emit()

    w3 = Property(int, get_w3, set_w3, notify=changedSignal)

    def get_w4(self):
        return self._w4

    def set_w4(self, value):
        self._w4 = value
        self.changedSignal.emit()

    w4 = Property(int, get_w4, set_w4, notify=changedSignal)

    def get_w5(self):
        return self._w5

    def set_w5(self, value):
        self._w5 = value
        self.changedSignal.emit()

    w5 = Property(int, get_w5, set_w5, notify=changedSignal)

    def get_w6(self):
        return self._w6

    def set_w6(self, value):
        if value:
            self._w6 = value
            self.changedSignal.emit()

    w6 = Property(int, get_w6, set_w6, notify=changedSignal)

    def get_w7(self):
        return self._w7

    def set_w7(self, value):
        self._w7 = value
        self.changedSignal.emit()

    w7 = Property(int, get_w7, set_w7, notify=changedSignal)

    def get_w8(self):
        return self._w8

    def set_w8(self, value):
        self._w8 = value
        self.changedSignal.emit()

    w8 = Property(int, get_w8, set_w8, notify=changedSignal)

    def get_w9(self):
        return self._w9

    def set_w9(self, value):
        self._w9 = value
        self.changedSignal.emit()

    w9 = Property(int, get_w9, set_w9, notify=changedSignal)

    def get_w10(self):
        return self._w10

    def set_w10(self, value):
        self._w10 = value
        self.changedSignal.emit()

    w10 = Property(int, get_w10, set_w10, notify=changedSignal)

    def get_price(self):
        return self._price

    def set_price(self, value):
        if self._tax:
            self._price = value * (1 + self._taxPercentage)
        else:
            self._price = value
        self.changedSignal.emit()

    price = Property(float, get_price, set_price, notify=changedSignal)

    def get_finalPrice(self):
        return self._finalPrice

    def set_finalPrice(self, value):
        if self._tax:
            self._finalPrice = value * (1 + self._taxPercentage)
        else:
            self._finalPrice = value
        self.changedSignal.emit()

    finalPrice = Property(float, get_finalPrice,
                          set_finalPrice, notify=changedSignal)

    def get_meanWeight(self):
        return self._meanWeight

    def set_meanWeight(self, value):
        self._meanWeight = value
        self.changedSignal.emit()

    meanWeight = Property(int, get_meanWeight,
                          set_meanWeight, notify=changedSignal)

    def get_tolerance(self):
        return self._tolerance

    def set_tolerance(self, value):
        self._tolerance = value
        self.changedSignal.emit()

    tolerance = Property(int, get_tolerance,
                         set_tolerance, notify=changedSignal)

    def get_insertedWeight(self):
        return self._insertedWeight

    def set_insertedWeight(self, value):
        self._insertedWeight = value
        self.changedSignal.emit()

    insertedWeight = Property(int, get_insertedWeight,
                              set_insertedWeight, notify=changedSignal)

    def get_barcode(self):
        return self._barcode

    def set_barcode(self, value):
        self._barcode = value
        self.changedSignal.emit()

    barcode = Property(str, get_barcode, set_barcode, notify=changedSignal)

    def get_isOffer(self):
        return self._isOffer

    def set_isOffer(self, value):
        self._isOffer = value
        self.changedSignal.emit()

    isOffer = Property(int, get_isOffer, set_isOffer, notify=changedSignal)

    def get_isPlu(self):
        return self._isPlu

    def set_isPlu(self, value):
        self._isPlu = value
        self.changedSignal.emit()

    isPlu = Property(int, get_isPlu, set_isPlu, notify=changedSignal)

    def get_tax(self):
        return self._tax

    def set_tax(self, value):
        self._tax = value
        self.changedSignal.emit()

    tax = Property(bool, get_tax, set_tax, notify=changedSignal)

    def get_QR(self):
        return self._QR

    def set_QR(self, value):
        self._QR = value
        self.changedSignal.emit()

    QR = Property(str, get_QR, set_QR, notify=changedSignal)

    def get_productType(self):
        return self._productType

    def set_productType(self, value):
        self._productType = value
        self.changedSignal.emit()

    productType = Property(str, get_productType,
                           set_productType, notify=changedSignal)

    def get_productWeightInBasket(self):
        return self._productWeightInBasket

    def set_productWeightInBasket(self, value):
        self._productWeightInBasket = value
        self.changedSignal.emit()

    productWeightInBasket = Property(
        int, get_productWeightInBasket, set_productWeightInBasket, notify=changedSignal)

    def get_dataModelShow(self):
        if (self.productType == "weighted"):
            return 1
        else:
            return 0

    dataModelShow = Property(int, get_dataModelShow, notify=changedSignal)

    def get_countInBasket(self):
        return self._countInBasket

    def set_countInBasket(self, val):
        self._countInBasket = val
        self.changedSignal.emit()

    countInBasket = Property(int, get_countInBasket,
                             set_countInBasket, notify=changedSignal)

    def get_Qprice(self):
        if self._dataModelShow == 1:
            if self.quantifier == "kg":
                return "$ " + str(round(self._finalPrice, 2)) + " /Kg"
            elif self.quantifier == "lb":
                lb = self._productWeightInBasket / 453.59237
                price = self._finalPrice / 1000 * 453.59237
                if lb < 1:
                    return "$ " + str(round((price / 16), 2)) + " /oz"
                elif lb >= 1:
                    return "$ " + str(round(price, 2)) + " /lb"
        else:
            return ""

    Qprice = Property(str, get_Qprice, notify=changedSignal)

    def get_Qweigh(self):
        if self._dataModelShow == 1:
            if self.quantifier == "kg":
                return str(round(self.productWeightInBasket / 1000)) + " Kg"
            elif self.quantifier == "lb":
                lb = self.productWeightInBasket / 453.59237
                if lb > 1:
                    return str(round(lb, 2)) + " lb"
                else:
                    return str(round((lb * 16), 2)) + " oz"
        else:
            return ""

    Qweigh = Property(str, get_Qweigh, notify=changedSignal)

    def get_quantifier(self):
        return self._quantifier

    def set_quantifier(self, val: str):
        self._quantifier = val
        self.changedSignal.emit()

    quantifier = Property(str, get_quantifier, set_quantifier, notify=changedSignal)

    def copy_product(self):
        """
        create copy of product
        return Product
        """
        product = Product()
        product.set_name(self.name)
        product.set_description(self.description)
        product.set_rate(self.rate)
        product.set_commentCount(self.commentCount)
        product.set_w1(self.w1)
        product.set_w2(self.w2)
        product.set_w3(self.w3)
        product.set_w4(self.w4)
        product.set_w5(self.w5)
        product.set_w6(self.w6)
        product.set_w7(self.w7)
        product.set_w8(self.w8)
        product.set_w9(self.w9)
        product.set_w10(self.w10)
        product.set_price(self.price)
        product.set_finalPrice(self.finalPrice)
        product.set_meanWeight(self.meanWeight)
        product.set_tolerance(self.tolerance)
        product.set_insertedWeight(self.insertedWeight)
        product.set_barcode(self.barcode)
        product.set_isOffer(self.isOffer)
        product.set_isPlu(self.isPlu)
        product.set_tax(self.tax)
        product.set_QR(self.QR)
        product.set_productType(self.productType)
        product._taxPercentage = self._taxPercentage
        product.set_quantifier(self._quantifier)
        return product

    def call_newWeightParameter(self, weight: int):
        """
        یک وزن که به محصول اضافه میشود مقادیر میانگین ، تعداد وزن ها و تلورانس محاسبه میشود
        
        param1: weight
        return: avg, tolerance, insertedWeight
        """
        avg_weight = self.get_meanWeight()
        tolerance = self.get_tolerance()
        iw = self.get_insertedWeight()
        new_avg_weight = int((((avg_weight * iw) + weight) / (iw + 1)))
        Min = avg_weight - tolerance
        Max = avg_weight + tolerance
        new_tolerance = int(
            max((abs(new_avg_weight - Min)), (abs(Max - new_avg_weight)), (abs(weight - new_avg_weight)),
                (new_avg_weight * 0.1), 8))
        iw = int(iw + 1)
        return new_avg_weight, new_tolerance, iw
