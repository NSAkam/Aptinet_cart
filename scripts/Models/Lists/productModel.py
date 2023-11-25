from ast import Dict
from typing import Any
from PySide2.QtCore import Signal, Property, QAbstractListModel, QModelIndex, Slot
from PySide2.QtCore import QModelIndex, Qt, QByteArray
from Services.dal import DAL
from Models.product import Product
from itertools import chain, combinations
from Repositories.productRepository import ProductRepository
from Services.Utiles import SpecialOfferWorker



class ProductModel(QAbstractListModel):
    repository: ProductRepository

    NameRole = Qt.UserRole
    DescriptionRole = Qt.UserRole + 2
    RateRole = Qt.UserRole + 3
    CommentCount = Qt.UserRole + 4
    PriceRole = Qt.UserRole + 5
    FinalPriceRole = Qt.UserRole + 6
    BarcodeRole = Qt.UserRole + 7
    CountInBasketRole = Qt.UserRole + 8
    WeightRole = Qt.UserRole + 9
    IsPLURole = Qt.UserRole + 11
    TaxRole = Qt.UserRole + 12
    DataModelShow = Qt.UserRole + 13
    PicRole = Qt.UserRole + 14


    m_data = [Product]
    m_validBarcodeSetForDelete = []
    m_removedWeightMin: int = 0
    m_removedWeightMax: int = 0
    priceToPay:float = 0

    def __init__(self, dataAccessLayer: DAL):
        super().__init__()
        self.repository = ProductRepository(dataAccessLayer)
        self.m_data = []
        self.m_validBarcodeSetForDelete = []

    @Signal
    def changed(self):
        pass

    def get_totalCount(self):
        count: int = 0
        for i in self.m_data:
            if(i.isPlu == True):
                count = count + 1
            else:
                count = count + i.countInBasket
        return count

    totalcount = Property(int, get_totalCount, notify=changed)

    def getPricenodiscount(self):
        price: int = 0
        for i in self.m_data:
            price = price + (i.price * i.countInBasket)
        return price

    pricenodiscount = Property(int, getPricenodiscount, notify=changed)

    def getFinalprice(self):
        finalprice: int = 0
        for i in self.m_data:
            finalprice = finalprice + (i.finalPrice * i.countInBasket)
        return finalprice

    finalprice = Property(float, getFinalprice, notify=changed)

    def getPriceToPay(self):
        return self.priceToPay; 

    def setPriceToPay(self,v):
        self.priceToPay = v
        self.changed.emit()

    priceToPay = Property(float ,getPriceToPay,setPriceToPay,notify=changed)

    def getProfit(self):
        price: int = 0
        finalprice: int = 0

        for i in self.m_data:
            price = price + (i.price * i.countInBasket)
            finalprice = finalprice + (i.finalPrice * i.countInBasket)
        return price - finalprice

    profit = Property(int, getProfit, notify=changed)
    

    def getValidBarcodeSetForDelete(self):
        return self.m_validBarcodeSetForDelete

    def setValidBarcodeSetForDelete(self, v):
        self.m_validBarcodeSetForDelete = v

    # Function #################################################################

    def rowCount(self, parent) -> int:  ###Override
        if (parent.isValid()):
            return 0
        return len(self.m_data)

    def data(self, index, role: int) -> Any:  ###Override
        if (not index.isValid()):
            return
        prod = self.m_data[index.row()]
        if (role == self.NameRole):
            return prod.getName()
        elif(role == self.DescriptionRole):
            return prod.description
        elif(role == self.RateRole):
            return prod.rate
        elif(role == self.CommentCount):
            return prod.commentCount
        elif(role == self.PriceRole):
            return prod.price
        elif(role == self.finalprice):
            return prod.finalPrice
        elif(role == self.BarcodeRole):
            return prod.barcode
        elif(role == self.CountInBasketRole):
            return prod.countInBasket
        elif(role == self.WeightRole):
            return prod.productWeightInBasket
        elif(role == self.IsOfferRole):
            return prod.isOffer
        elif(role == self.IsPLURole):
            return prod.isPlu
        elif(role == self.TaxRole):
            return prod.tax
        elif(role ==self.DataModelShow):
            return prod.dataModelShow
        elif(role == self.PicRole):
            return prod.pic
        else:
            return None

    def roleNames(self) -> Dict:  ###Override
        default = super().roleNames()
        default[self.NameRole] = QByteArray(b"name")
        default[self.DescriptionRole] = QByteArray(b"description")
        default[self.RateRole] = QByteArray(b"rate")
        default[self.CommentCount] = QByteArray(b"commentCount")
        default[self.PriceRole] = QByteArray(b"price")
        default[self.FinalPriceRole] = QByteArray(b"finalPrice")
        default[self.BarcodeRole] = QByteArray(b"barcode")
        default[self.CountInBasketRole] = QByteArray(b"countInBasket")
        default[self.WeightRole] = QByteArray(b"weight")
        default[self.IsOfferRole] = QByteArray(b"isOffer")
        default[self.IsPLURole] = QByteArray(b"isPLURole")
        default[self.TaxRole] = QByteArray(b"tax")
        default[self.DataModelShow] = QByteArray(b"dataModelShow")
        return default

    # def data(self):
    #     return self.m_data
    # def setdata(self,val):
    #     self.beginResetModel()
    #     self.m_data = val
    #     self.endResetModel()

    def clearData(self):
        self.beginResetModel()
        self.m_data.clear()
        self.changed.emit()
        self.endResetModel()

    def get_productByBarcode(self, barcode: str):
        return self.repository.get_product(barcode)

    def insertNewProduct(self, barcode):
        return self.repository.GetProducts(barcode)

    def getProductQrByirancode(self, irancode):
        return str(self.repository.GetProductBarcode(irancode))

    def count(self) -> int:
        return len(self.m_data)

    def insertProduct(self, prod: Product, tedad: int):
        temp = False
        for index, value in enumerate(self.m_data):
            if (value.getBarcode() == prod.getBarcode()):
                ix = self.index(index, 0)
                self.m_data[index].settedad(self.m_data[index].gettedad() + tedad)
                self.dataChanged.emit(ix, ix, self.roleNames())
                temp = True
        if (temp == False):
            prod.settedad(tedad)
            self.beginInsertRows(QModelIndex(), 0, 0)
            self.m_data.insert(0, prod)
            self.endInsertRows()
        self.changed.emit()

    def removeProducts(self, prods: [Product]):
        for prod in prods:
            for factor in self.m_data:
                if prod.getBarcode() == factor.getBarcode():
                    idx = self.m_data.index(factor)
                    # ix = self.index(self.m_data.index(factor), 0)
                    if (factor.gettedad() - prod.gettedad()) == 0:
                        self.beginRemoveRows(QModelIndex(), idx, idx)
                        del self.m_data[idx]
                        self.endRemoveRows()
                    else:
                        ix = self.index(self.m_data.index(factor), 0)
                        self.m_data[idx].settedad(factor.gettedad() - prod.gettedad())
                        self.dataChanged.emit(ix, ix, self.roleNames())
                    # self.beginResetModel()
                    # self.m_data[self.m_data.index(factor)].settedad(factor.gettedad() - prod.gettedad())
                    # self.endResetModel()
                    # if factor.gettedad() == 0:
                    #     self.beginResetModel()
                    #     del self.m_data[self.m_data.index(factor)]
                    #     self.endResetModel()
        self.changed.emit()

    def removeProductsUpdateBypass(self, prods: [Product]):
        for prod in prods:
            for factor in self.m_data:
                if prod.getBarcode() == factor.getBarcode():
                    ix = self.index(self.m_data.index(factor), 0)
                    factor.settedad(factor.gettedad() - prod.gettedad())
                    self.dataChanged.emit(ix, ix, self.roleNames())
        self.changed.emit()

    @Slot(result=bool)
    def reset(self):
        self.beginResetModel()
        self.resetInternalData()  # should work without calling it ?
        self.endResetModel()
        return True

    # def getSpecialOffer(self):
    #     self.beginResetModel()
    #     self.m_data = self.repository.GetSpecialOffer()
    #     self.endResetModel()
    #     # self.spworker = SpecialOfferWorker(self.repository)
    #     # self.spworker.get.connect(self.onGetSpecialOffer)
    #     # self.spworker.start()
        

    @Slot(list)
    def onGetSpecialOffer(self,v):
        self.beginResetModel()
        self.m_data = v
        self.endResetModel()

    
    # def powerset(self, iterable):
    #     return chain.from_iterable(combinations(iterable, r) for r in range(len(iterable) + 1))

    def validBarcodeSetForRemove(self, data, RemovedWight):
        lst_1 = []
        for item in data:
            if item.getAvgWeight() <= RemovedWight + item.getTolerance() + 8:
                for i in range(item.gettedad()):
                    lst_1.append(item.getBarcode())
        self.setValidBarcodeSetForDelete(lst_1)
        self.m_removedWeightMax = RemovedWight
        self.m_removedWeightMin = RemovedWight

    # def validBarcodeSetForRemove(self, data, RemovedWight):
    #     lst_1 = []
    #     for item in data:
    #         if item.getAvgWeight() <= RemovedWight + item.getTolerance() + 8:
    #             for i in range(item.gettedad()):
    #                 temp = Product()
    #                 temp.settedad(1)
    #                 temp.setQRCode(item.getBarcode())
    #                 temp.setW1(item.getW1())
    #                 temp.setW2(item.getW2())
    #                 temp.setW3(item.getW3())
    #                 temp.setW4(item.getW4())
    #                 temp.setW5(item.getW5())
    #                 temp.setW6(item.getW6())
    #                 temp.setW7(item.getW7())
    #                 temp.setW8(item.getW8())
    #                 temp.setW9(item.getW9())
    #                 temp.setW10(item.getW10())
    #                 temp.CalcTelorance()
    #                 lst_1.append(temp)
    #     res = list(self.powerset(lst_1))[1:]
    #     ValidSet = []
    #     for ValidSetNomination in res:
    #         AccumulativeWeight = 0
    #         AccumulativeTolerance = 0
    #         for i in range(len(ValidSetNomination)):
    #             AccumulativeWeight += ValidSetNomination[i].getAvgWeight()
    #             AccumulativeTolerance += ValidSetNomination[i].getTolerance()
    #         if AccumulativeWeight - AccumulativeTolerance <= RemovedWight <= AccumulativeWeight + AccumulativeTolerance:
    #             tempList = []
    #             for i in range(len(ValidSetNomination)):
    #                 tempList.append(ValidSetNomination[i].getBarcode())
    #             if tempList not in ValidSet:
    #                 ValidSet.append(tempList)
    #     self.setValidBarcodeSetForDelete(ValidSet)

    def updateValidBarcodeSetForRemove(self, barcode):
        removeAllProduct = False
        acceptableBarcode = False
        removeSuccessfullyBefor = False
        avgWeight = self.repository.GetProducts(barcode).getAvgWeight()
        tolerance = self.repository.GetProducts(barcode).getTolerance()
        if barcode in self.m_validBarcodeSetForDelete:
            if (self.m_removedWeightMax - avgWeight + (tolerance + 8)) >= 0:
                acceptableBarcode = True
                self.m_validBarcodeSetForDelete.remove(barcode)
                self.beginResetModel()
                self.insertProduct(self.repository.GetProducts(barcode), 1)
                self.endResetModel()
                self.changed.emit()
                self.m_removedWeightMin = self.m_removedWeightMin - avgWeight - (tolerance + 8)
                self.m_removedWeightMax = self.m_removedWeightMax - avgWeight + (tolerance + 8)
        if not acceptableBarcode:
            for prod in self.m_data:
                if barcode == prod.getBarcode():
                    removeSuccessfullyBefor = True
        if self.m_removedWeightMin <= 0 and self.m_removedWeightMax >= 0:
            removeAllProduct = True
        # print(self.m_removedWeightMax)
        # print(self.m_removedWeightMin)
        return acceptableBarcode, removeAllProduct, removeSuccessfullyBefor

    # def updateValidBarcodeSetForRemove(self, barcode):
    #     removeAllProduct = False
    #     acceptableBarcode = False
    #     for i in range(len(self.m_validBarcodeSetForDelete)):
    #         if barcode in self.m_validBarcodeSetForDelete[i]:
    #             acceptableBarcode = True
    #             break
    #     if acceptableBarcode:
    #         self.insertProduct(self.repository.GetProducts(barcode), 1)
    #         print("Product Added >>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<" + str(len(self.m_data)))
    #         for i in range(len(self.m_validBarcodeSetForDelete)-1, -1, -1):
    #             if barcode not in self.m_validBarcodeSetForDelete[i]:
    #                 del self.m_validBarcodeSetForDelete[i]
    #         for i in range(len(self.m_validBarcodeSetForDelete)):
    #             self.m_validBarcodeSetForDelete[i].remove(barcode)
    #             if len(self.m_validBarcodeSetForDelete[i]) == 0:
    #                 removeAllProduct = True
    #     return (acceptableBarcode, removeAllProduct)

    # def calNewWeightParameter(self, prod: Product, weight: int): ### to be deleted
    #     avg_weight = prod.getAvgWeight()
    #     tolerance = prod.getTolerance()
    #     inserted_weight = prod.getInsertedWeight()
    #     new_avg_weight = int((((avg_weight * inserted_weight) + weight) / (inserted_weight + 1)))
    #     Min = avg_weight - tolerance
    #     Max = avg_weight + tolerance
    #     new_tolerance = int(
    #         max((abs(new_avg_weight - Min)), (abs(Max - new_avg_weight)), (abs(weight - new_avg_weight)),
    #             (new_avg_weight * 0.1), 8))
    #     new_inserted_weight = int(inserted_weight + 1)
    #     return (new_avg_weight, new_tolerance, new_inserted_weight)

    def updateWeight(self, prod: Product, weight: int):
        if prod.getInsertedWeight() == 0:
            prod.setW1(weight)
            prod.setAvgWeight(weight)
            prod.setTolerance(int(max(8, int(weight * 0.1))))
            prod.setInsertedWeight(1)
            self.repository.updateProduductW1(prod.getBarcode(), weight, prod.getAvgWeight(), prod.getTolerance(),
                                              prod.getInsertedWeight())
        else:
            if prod.getW1() == 0:
                new_avg_weight, new_tolerance, new_inserted_weight = prod.calNewWeightParameter(weight)
                prod.setW1(weight)
                prod.setAvgWeight(new_avg_weight)
                prod.setTolerance(new_tolerance)
                prod.setInsertedWeight(new_inserted_weight)
                self.repository.updateProduductW1(prod.getBarcode(), weight, new_avg_weight, new_tolerance,
                                                  new_inserted_weight)
            elif prod.getW2() == 0:
                new_avg_weight, new_tolerance, new_inserted_weight = prod.calNewWeightParameter(weight)
                prod.setW2(weight)
                prod.setAvgWeight(new_avg_weight)
                prod.setTolerance(new_tolerance)
                prod.setInsertedWeight(new_inserted_weight)
                self.repository.updateProduductW2(prod.getBarcode(), weight, new_avg_weight, new_tolerance,
                                                  new_inserted_weight)
            elif prod.getW3() == 0:
                new_avg_weight, new_tolerance, new_inserted_weight = prod.calNewWeightParameter(weight)
                prod.setW3(weight)
                prod.setAvgWeight(new_avg_weight)
                prod.setTolerance(new_tolerance)
                prod.setInsertedWeight(new_inserted_weight)
                self.repository.updateProduductW3(prod.getBarcode(), weight, new_avg_weight, new_tolerance,
                                                  new_inserted_weight)
            elif prod.getW4() == 0:
                new_avg_weight, new_tolerance, new_inserted_weight = prod.calNewWeightParameter(weight)
                prod.setW4(weight)
                prod.setAvgWeight(new_avg_weight)
                prod.setTolerance(new_tolerance)
                prod.setInsertedWeight(new_inserted_weight)
                self.repository.updateProduductW4(prod.getBarcode(), weight, new_avg_weight, new_tolerance,
                                                  new_inserted_weight)
            elif prod.getW5() == 0:
                new_avg_weight, new_tolerance, new_inserted_weight = prod.calNewWeightParameter(weight)
                prod.setW5(weight)
                prod.setAvgWeight(new_avg_weight)
                prod.setTolerance(new_tolerance)
                prod.setInsertedWeight(new_inserted_weight)
                self.repository.updateProduductW5(prod.getBarcode(), weight, new_avg_weight, new_tolerance,
                                                  new_inserted_weight)
            elif prod.getW6() == 0:
                new_avg_weight, new_tolerance, new_inserted_weight = prod.calNewWeightParameter(weight)
                prod.setW6(weight)
                prod.setAvgWeight(new_avg_weight)
                prod.setTolerance(new_tolerance)
                prod.setInsertedWeight(new_inserted_weight)
                self.repository.updateProduductW6(prod.getBarcode(), weight, new_avg_weight, new_tolerance,
                                                  new_inserted_weight)
            elif prod.getW7() == 0:
                new_avg_weight, new_tolerance, new_inserted_weight = prod.calNewWeightParameter(weight)
                prod.setW7(weight)
                prod.setAvgWeight(new_avg_weight)
                prod.setTolerance(new_tolerance)
                prod.setInsertedWeight(new_inserted_weight)
                self.repository.updateProduductW7(prod.getBarcode(), weight, new_avg_weight, new_tolerance,
                                                  new_inserted_weight)
            elif prod.getW8() == 0:
                new_avg_weight, new_tolerance, new_inserted_weight = prod.calNewWeightParameter(weight)
                prod.setW8(weight)
                prod.setAvgWeight(new_avg_weight)
                prod.setTolerance(new_tolerance)
                prod.setInsertedWeight(new_inserted_weight)
                self.repository.updateProduductW8(prod.getBarcode(), weight, new_avg_weight, new_tolerance,
                                                  new_inserted_weight)
            elif prod.getW9() == 0:
                new_avg_weight, new_tolerance, new_inserted_weight = prod.calNewWeightParameter(weight)
                prod.setW9(weight)
                prod.setAvgWeight(new_avg_weight)
                prod.setTolerance(new_tolerance)
                prod.setInsertedWeight(new_inserted_weight)
                self.repository.updateProduductW9(prod.getBarcode(), weight, new_avg_weight, new_tolerance,
                                                  new_inserted_weight)
            elif prod.getW10() == 0:
                new_avg_weight, new_tolerance, new_inserted_weight = prod.calNewWeightParameter(weight)
                prod.setW10(weight)
                prod.setAvgWeight(new_avg_weight)
                prod.setTolerance(new_tolerance)
                prod.setInsertedWeight(new_inserted_weight)
                self.repository.updateProduductW10(prod.getBarcode(), weight, new_avg_weight, new_tolerance,
                                                   new_inserted_weight)
        # if prod.insertedWeight == 10:
        #     if weight >= prod.getMaxWeight():
        #         if prod.getW1() == prod.getMaxWeight():
        #             prod.setW1(weight)
        #             self.repository.updateProduductW1(prod.getBarcode(), weight)
        #         elif prod.getW2() == prod.getMaxWeight():
        #             prod.setW2(weight)
        #             self.repository.updateProduductW2(prod.getBarcode(), weight)
        #         elif prod.getW3() == prod.getMaxWeight():
        #             prod.setW3(weight)
        #             self.repository.updateProduductW3(prod.getBarcode(), weight)
        #         elif prod.getW4() == prod.getMaxWeight():
        #             prod.setW4(weight)
        #             self.repository.updateProduductW4(prod.getBarcode(), weight)
        #         elif prod.getW5() == prod.getMaxWeight():
        #             prod.setW5(weight)
        #             self.repository.updateProduductW5(prod.getBarcode(), weight)
        #         elif prod.getW6() == prod.getMaxWeight():
        #             prod.setW6(weight)
        #             self.repository.updateProduductW6(prod.getBarcode(), weight)
        #         elif prod.getW7() == prod.getMaxWeight():
        #             prod.setW7(weight)
        #             self.repository.updateProduductW7(prod.getBarcode(), weight)
        #         elif prod.getW8() == prod.getMaxWeight():
        #             prod.setW8(weight)
        #             self.repository.updateProduductW8(prod.getBarcode(), weight)
        #         elif prod.getW9() == prod.getMaxWeight():
        #             prod.setW9(weight)
        #             self.repository.updateProduductW9(prod.getBarcode(), weight)
        #         elif prod.getW10() == prod.getMaxWeight():
        #             prod.setW10(weight)
        #             self.repository.updateProduductW10(prod.getBarcode(), weight)
        #     elif weight <= prod.getMinWeight():
        #         if prod.getW1() == prod.getMinWeight():
        #             prod.setW1(weight)
        #             self.repository.updateProduductW1(prod.getBarcode(), weight)
        #         elif prod.getW2() == prod.getMinWeight():
        #             prod.setW2(weight)
        #             self.repository.updateProduductW2(prod.getBarcode(), weight)
        #         elif prod.getW3() == prod.getMinWeight():
        #             prod.setW3(weight)
        #             self.repository.updateProduductW3(prod.getBarcode(), weight)
        #         elif prod.getW4() == prod.getMinWeight():
        #             prod.setW4(weight)
        #             self.repository.updateProduductW4(prod.getBarcode(), weight)
        #         elif prod.getW5() == prod.getMinWeight():
        #             prod.setW5(weight)
        #             self.repository.updateProduductW5(prod.getBarcode(), weight)
        #         elif prod.getW6() == prod.getMinWeight():
        #             prod.setW6(weight)
        #             self.repository.updateProduductW6(prod.getBarcode(), weight)
        #         elif prod.getW7() == prod.getMinWeight():
        #             prod.setW7(weight)
        #             self.repository.updateProduductW7(prod.getBarcode(), weight)
        #         elif prod.getW8() == prod.getMinWeight():
        #             prod.setW8(weight)
        #             self.repository.updateProduductW8(prod.getBarcode(), weight)
        #         elif prod.getW9() == prod.getMinWeight():
        #             prod.setW9(weight)
        #             self.repository.updateProduductW9(prod.getBarcode(), weight)
        #         elif prod.getW10() == prod.getMinWeight():
        #             prod.setW10(weight)
        #             self.repository.updateProduductW10(prod.getBarcode(), weight)
        #
        # else:
        #     if prod.getW1() <= 8:
        #         prod.setW1(weight)
        #         self.repository.updateProduductW1(prod.getBarcode(), weight)
        #     elif prod.getW2() <= 8:
        #         prod.setW2(weight)
        #         self.repository.updateProduductW2(prod.getBarcode(), weight)
        #     elif prod.getW3() <= 8:
        #         prod.setW3(weight)
        #         self.repository.updateProduductW3(prod.getBarcode(), weight)
        #     elif prod.getW4() <= 8:
        #         prod.setW4(weight)
        #         self.repository.updateProduductW4(prod.getBarcode(), weight)
        #     elif prod.getW5() <= 8:
        #         prod.setW5(weight)
        #         self.repository.updateProduductW5(prod.getBarcode(), weight)
        #     elif prod.getW6() <= 8:
        #         prod.setW6(weight)
        #         self.repository.updateProduductW6(prod.getBarcode(), weight)
        #     elif prod.getW7() <= 8:
        #         prod.setW7(weight)
        #         self.repository.updateProduductW7(prod.getBarcode(), weight)
        #     elif prod.getW8() <= 8:
        #         prod.setW8(weight)
        #         self.repository.updateProduductW8(prod.getBarcode(), weight)
        #     elif prod.getW9() <= 8:
        #         prod.setW9(weight)
        #         self.repository.updateProduductW9(prod.getBarcode(), weight)
        #     elif prod.getW10() <= 8:
        #         prod.setW10(weight)
        #         self.repository.updateProduductW10(prod.getBarcode(), weight)
        # prod.Calculation()
        # self.repository.newWeightInserted(prod.getBarcode(), 1)

    @Slot(int)
    def increaseClicked(self, index: int):
        ix = self.index(index, 0)

        # self.beginResetModel()
        self.m_data[index].settedad(self.m_data[index].gettedad() + 1)
        # self.endResetModel()
        self.dataChanged.emit(ix, ix, self.roleNames())

    @Slot(int)
    def decreaseClicked(self, index: int):
        ix = self.index(index, 0)
        # self.m_data[index].settedad(self.m_data[index].gettedad() + 1)
        # self.beginResetModel()
        if self.m_data[index].gettedad() > 0:
            self.m_data[index].settedad(self.m_data[index].gettedad() - 1)
        # self.endResetModel()
        self.dataChanged.emit(ix, ix, self.roleNames())

    @Slot()
    def checkForProductsChange(self,lst:[Product]):
        changed = False
        for index, prod in enumerate(lst):
            if(prod.getunitCount() < self.m_data[index].getunitCount()):
                ix = self.index(index, 0)
                self.m_data[index].setDataModelShow(1)            
                self.dataChanged.emit(ix, ix, self.roleNames())
                changed = True
            if(prod.getnotValid() > 0):
                ix = self.index(index, 0)
                self.m_data[index].setDataModelShow(1)
                self.dataChanged.emit(ix, ix, self.roleNames())
                changed = True
        return changed
                

    def removeObject(self):
        print(
            ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ProductModel Deleted <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
        self.repository.Disconnect()
        del self.repository
