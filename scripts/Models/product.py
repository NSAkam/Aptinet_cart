from PySide2.QtCore import QObject, Signal, Property
import os


class Product(QObject):
    _barcode:str = ""
    _name: str = ""
    _Price: int = 0
    _finalprice: int = 0
    _unitCount:int = 0
    _notValid:int=0

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
    _avgWeight: int = 0 # Mean of weights
    _tolerance: int = 0 # Tolerance for every product 
    _insertedWeight: int = 0 # Count of weights in localDB
    _Irancode: str = ""

    _dataModelShow:int = 0

    _countdownTimer: int = 7
    _tedad: int = 0

    def __init__(self):
        super().__init__()

    @Signal
    def changed(self):
        pass

    def getname(self):
        return self._name

    def setname(self, val):
        if (val is None or val == ""):
            self._name = "محصول نام ندارد"
        else:
            self._name = val
        self.changed.emit()

    name = Property(str, getname, setname, notify=changed)

    def getprice(self):
        return self._Price

    def setprice(self, val):
        self._Price = val
        self.changed.emit()

    Price = Property(int, getprice, setprice, notify=changed)

    def getpic(self):
        if (os.path.isfile("/home/kast/pics/" + self.getBarcode() + ".png") == False):
            return "file:///home/kast/pics/DefaultProduct.png"
        else:
            return "file:///home/kast/pics/" + self.getBarcode() + ".png"

    pic = Property(str, getpic, notify=changed)

    def getfinalprice(self):
        return self._finalprice

    def setfinalprice(self, val):
        self._finalprice = val
        self.changed.emit()

    finalprice = Property(int, getfinalprice, setfinalprice, notify=changed)

    def getunitCount(self):
        return self._unitCount

    def setunitCount(self, val):
        self._unitCount = val
        self.changed.emit()

    unitCount = Property(int, getunitCount, setunitCount, notify=changed)

    def getnotValid(self):
        return self._notValid

    def setnotValid(self, val):
        self._notValid = val
        self.changed.emit()

    notValid = Property(int, getnotValid, setnotValid, notify=changed)

    def getBarcode(self):
        return self._barcode

    def setBarcode(self, val: str):
        self._barcode = str(val)
        self.changed.emit()

    Barcode = Property(str, getBarcode, setBarcode, notify=changed)

    def getIrancode(self):
        return self._Irancode

    def setIrancode(self, val: str):
        self._Irancode = val
        self.changed.emit()

    Irancode = Property(str, getIrancode, setIrancode, notify=changed)

    def gettedad(self):
        return self._tedad

    def settedad(self, val):
        self._tedad = val
        self.changed.emit()

    tedad = Property(float, gettedad, settedad, notify=changed)

    def getcountdownTimer(self):
        return self._countdownTimer

    def setcountdownTimer(self, val):
        self._countdownTimer = val
        self.changed.emit()

    countdownTimer = Property(int, getcountdownTimer, setcountdownTimer, notify=changed)

    def getW1(self):
        return self._w1

    def setW1(self, v):
        self._w1 = v if v != "" else 0
        self.changed.emit()

    w1 = Property(int, getW1, setW1, notify=changed)

    def getW2(self):
        return self._w2

    def setW2(self, v):
        self._w2 = v if v != "" else 0
        self.changed.emit()

    w2 = Property(int, getW2, setW2, notify=changed)

    def getW3(self):
        return self._w3

    def setW3(self, v):
        self._w3 = v if v != "" else 0
        self.changed.emit()

    w3 = Property(int, getW3, setW3, notify=changed)

    def getW4(self):
        return self._w4

    def setW4(self, v):
        self._w4 = v if v != "" else 0
        self.changed.emit()

    w4 = Property(int, getW4, setW4, notify=changed)

    def getW5(self):
        return self._w5

    def setW5(self, v):
        self._w5 = v if v != "" else 0
        self.changed.emit()

    w5 = Property(int, getW5, setW5, notify=changed)

    def getW6(self):
        return self._w6

    def setW6(self, v):
        self._w6 = v if v != "" else 0
        self.changed.emit()

    w6 = Property(int, getW6, setW6, notify=changed)

    def getW7(self):
        return self._w7

    def setW7(self, v):
        self._w7 = v if v != "" else 0
        self.changed.emit()

    w7 = Property(int, getW7, setW7, notify=changed)

    def getW8(self):
        return self._w8

    def setW8(self, v):
        self._w8 = v if v != "" else 0
        self.changed.emit()

    w8 = Property(int, getW8, setW8, notify=changed)

    def getW9(self):
        return self._w9

    def setW9(self, v):
        self._w9 = v if v != "" else 0
        self.changed.emit()

    w9 = Property(int, getW9, setW9, notify=changed)

    def getW10(self):
        return self._w10

    def setW10(self, v):
        self._w10 = v if v != "" else 0
        self.changed.emit()

    w10 = Property(int, getW10, setW10, notify=changed)

    def getTolerance(self):
        return self._tolerance

    def setTolerance(self, v):
        self._tolerance = v if v != "" else 0
        self.changed.emit()

    tolerance = Property(int, getTolerance, setTolerance, notify=changed)

    # def outlierRemover(self, data_list, outlier_margin=1.5):
    #     a = array(data_list)
    #     upper_quartile = percentile(a, 75)
    #     lower_quartile = percentile(a, 25)
    #     IQR = max(((upper_quartile - lower_quartile) * outlier_margin),8)
    #     quartileSet = (lower_quartile - IQR, upper_quartile + IQR)
    #     resultList = []
    #     for raw_number in a.tolist():
    #         if quartileSet[0] <= raw_number <= quartileSet[1]:
    #             resultList.append(raw_number)
    #     # print(resultList)
    #     # return int(sum(resultList) / len(resultList)) if len(resultList) > 0 else 0
    #     return resultList
    #
    # def CalcTelorance(self):
    #     self.setTolerance(max((self.getMaxWeight() - self.getAvgWeight()), (self.getAvgWeight() - self.getMinWeight()), (self.getAvgWeight() * 0.1), 8))
    #     print(">>>>>>>>>>>>>>>>>>>>>> Tolerance is :" + str(self.getTolerance()) + "<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    #
    # def CalcAvgWeight(self):
    #     weight_list = []
    #     if self.w1 >= 8:
    #         weight_list.append(self.w1)
    #     if self.w2 >= 8:
    #         weight_list.append(self.w2)
    #     if self.w3 >= 8:
    #         weight_list.append(self.w3)
    #     if self.w4 >= 8:
    #         weight_list.append(self.w4)
    #     if self.w5 >= 8:
    #         weight_list.append(self.w5)
    #     if self.w6 >= 8:
    #         weight_list.append(self.w6)
    #     if self.w7 >= 8:
    #         weight_list.append(self.w7)
    #     if self.w8 >= 8:
    #         weight_list.append(self.w8)
    #     if self.w9 >= 8:
    #         weight_list.append(self.w9)
    #     if self.w10 >= 8:
    #         weight_list.append(self.w10)
    #
    #     valid_weight = self.outlierRemover(weight_list)
    #     self.insertedWeight = len(valid_weight)
    #     if len(valid_weight) != 0:
    #         self.maxWeight = int(max(valid_weight))
    #         self.minWeight = int(min(valid_weight))
    #         self.setAvgWeight(int(sum(valid_weight) / len(valid_weight)))
    #     else:
    #         self.maxWeight = 0
    #         self.minWeight = 0
    #         self.setAvgWeight(int(0))

    def getAvgWeight(self):
        return self._avgWeight

    def setAvgWeight(self, v):
        self._avgWeight = v if v != "" else 0
        self.changed.emit()

    avgWeight = Property(int, getAvgWeight, setAvgWeight, notify=changed)

    # def Calculation(self):
    #     self.CalcAvgWeight()
    #     self.CalcTelorance()

    # def getMinWeight(self):
    #     return self.minWeight

    # def setMinWeight(self, v):
    #     self.minWeight = v if v != "" else 0

    # def getMaxWeight(self):
    #     return self.maxWeight

    # def setMaxWeight(self, v):
    #     self.maxWeight = v if v != "" else 0

    def getInsertedWeight(self):
        return self._insertedWeight

    def setInsertedWeight(self, v):
        self._insertedWeight = v if v != "" else 0
        self.changed.emit()
    
    insertedWeight = Property(int,getInsertedWeight,setInsertedWeight,notify=changed)

    def getDataModelShow(self):
        return self._dataModelShow
    
    def setDataModelShow(self,v):
        self._dataModelShow = v
        self.changed.emit()

    dataModelShow = Property(int,getDataModelShow,setDataModelShow,notify=changed)

    def copy_product(self):
        """
        create copy of product
        return Product
        """
        prod = Product()
        prod.setInsertedWeight(self.getInsertedWeight())
        prod.setTolerance(self.getTolerance())
        prod.setAvgWeight(self.getAvgWeight())
        prod.settedad(self.gettedad())
        prod.setname(self.getname())
        prod.setfinalprice(self.getfinalprice())
        prod.setunitCount(self.getunitCount())
        prod.setnotValid(self.getnotValid())
        prod.setprice(self.getprice())
        prod.setBarcode(self.getBarcode())
        prod.setIrancode(self.getIrancode())
        prod.setW1(self.getW1())
        prod.setW2(self.getW2())
        prod.setW3(self.getW3())
        prod.setW4(self.getW4())
        prod.setW5(self.getW5())
        prod.setW6(self.getW6())
        prod.setW7(self.getW7())
        prod.setW8(self.getW8())
        prod.setW9(self.getW9())
        prod.setW10(self.getW10())
        return prod

    def calNewWeightParameter(self, weight: int):
        """
        یک وزن که به محصول اضافه میشود مقادیر میانگین ، تعداد وزن ها و تلورانس محاسبه میشود
        
        param1: weight
        return: avg, tolerance, insertedWeight
        """
        avg_weight = self.getAvgWeight()
        tolerance = self.getTolerance()
        iw = self.getInsertedWeight()
        new_avg_weight = int((((avg_weight * iw) + weight) / (iw + 1)))
        Min = avg_weight - tolerance
        Max = avg_weight + tolerance
        new_tolerance = int(
            max((abs(new_avg_weight - Min)), (abs(Max - new_avg_weight)), (abs(weight - new_avg_weight)),
                (new_avg_weight * 0.1), 8))
        iw = int(iw + 1)
        return new_avg_weight, new_tolerance, iw
