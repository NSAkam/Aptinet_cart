from ast import Dict
from typing import Any
from PySide2.QtCore import Signal, Property, QAbstractListModel, QModelIndex, Slot
from PySide2.QtCore import QModelIndex, Qt, QByteArray
from Services.dal import DAL
from Models.product import Product
from itertools import chain, combinations
from Services.Utiles import SpecialOfferWorker


class ProductModel(QAbstractListModel):
    NameRole = Qt.UserRole
    DescriptionRole = Qt.UserRole + 2
    RateRole = Qt.UserRole + 3
    CommentCountRole = Qt.UserRole + 4
    PriceRole = Qt.UserRole + 5
    FinalPriceRole = Qt.UserRole + 6
    BarcodeRole = Qt.UserRole + 7
    CountInBasketRole = Qt.UserRole + 8
    WeightRole = Qt.UserRole + 9
    IsPLURole = Qt.UserRole + 10
    TaxRole = Qt.UserRole + 11
    DataModelShowRole = Qt.UserRole + 12
    PicRole = Qt.UserRole + 13
    ProductTypeRole = Qt.UserRole + 14

    m_data = [Product]
    m_validBarcodeSetForDelete = []
    m_removedWeightMin: int = 0
    m_removedWeightMax: int = 0

    _priceToPay: float = 0

    def __init__(self):
        super().__init__()
        self.m_data = []
        self.m_validBarcodeSetForDelete = []

    @Signal
    def changed(self):
        pass

    def get_totalCount(self):
        count: int = 0
        for i in self.m_data:
            if (i.isPlu == True):
                count = count + 1
            else:
                count = count + i.countInBasket
        return count

    totalcount = Property(int, get_totalCount, notify=changed)

    def get_pricenodiscount(self):
        price: float = 0
        for i in self.m_data:
            if i.isPlu:
                price = price + (i.price * i.productWeightInBasket/1000)
            else:
                price = price + (i.price * i.countInBasket)
        return round(price, 2)

    priceNoDiscount = Property(int, get_pricenodiscount, notify=changed)

    def get_finalprice(self):
        finalprice: float = 0
        for i in self.m_data:
            if i.isPlu:
                finalprice = finalprice + (i.finalPrice * i.productWeightInBasket/1000)
            else:
                finalprice = finalprice + (i.finalPrice * i.countInBasket)
        return round(finalprice, 2)

    finalprice = Property(float, get_finalprice, notify=changed)

    def get_priceToPay(self):
        return self._priceToPay

    def set_priceToPay(self, v):
        self._priceToPay = v
        self.changed.emit()

    priceToPay = Property(float, get_priceToPay,
                          set_priceToPay, notify=changed)

    def getProfit(self):
        price: float = 0
        finalprice: float = 0

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

    def rowCount(self, parent) -> int:  # Override
        if (parent.isValid()):
            return 0
        return len(self.m_data)

    def data(self, index, role: int) -> Any:  # Override
        if (not index.isValid()):
            return
        prod = self.m_data[index.row()]
        if (role == self.NameRole):
            return prod.name
        elif (role == self.DescriptionRole):
            return prod.description
        elif (role == self.RateRole):
            return prod.rate
        elif (role == self.CommentCountRole):
            return prod.commentCount
        elif (role == self.PriceRole):
            return prod.price
        elif (role == self.FinalPriceRole):
            return prod.finalPrice
        elif (role == self.BarcodeRole):
            return prod.barcode
        elif (role == self.CountInBasketRole):
            return prod.countInBasket
        elif (role == self.WeightRole):
            return prod.productWeightInBasket
        elif (role == self.IsPLURole):
            return prod.isPlu
        elif (role == self.TaxRole):
            return prod.tax
        elif (role == self.DataModelShowRole):
            return prod.dataModelShow
        elif (role == self.PicRole):
            return prod.pic
        elif (role == self.ProductTypeRole):
            return prod.productType
        else:
            return None

    def roleNames(self) -> Dict:  # Override
        default = super().roleNames()
        default[self.NameRole] = QByteArray(b"name")
        default[self.DescriptionRole] = QByteArray(b"description")
        default[self.RateRole] = QByteArray(b"rate")
        default[self.CommentCountRole] = QByteArray(b"commentCount")
        default[self.PriceRole] = QByteArray(b"price")
        default[self.FinalPriceRole] = QByteArray(b"finalPrice")
        default[self.BarcodeRole] = QByteArray(b"barcode")
        default[self.CountInBasketRole] = QByteArray(b"countInBasket")
        default[self.WeightRole] = QByteArray(b"weight")
        default[self.IsPLURole] = QByteArray(b"isPLURole")
        default[self.TaxRole] = QByteArray(b"tax")
        default[self.DataModelShowRole] = QByteArray(b"dataModelShow")
        default[self.ProductTypeRole] = QByteArray(b"productType")
        default[self.PicRole] = QByteArray(b"pic")
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

    def count(self) -> int:
        return len(self.m_data)

    def insertProduct(self, prod: Product, count: int):
        temp = False
        for index, value in enumerate(self.m_data):
            if (value.barcode == prod.barcode):
                ix = self.index(index, 0)
                self.m_data[index].set_countInBasket(
                    self.m_data[index].countInBasket + count)
                self.dataChanged.emit(ix, ix, self.roleNames())
                temp = True
        if temp == False:
            prod.set_countInBasket(count)
            self.beginInsertRows(QModelIndex(), 0, 0)
            self.m_data.insert(0, prod)
            self.endInsertRows()
        self.changed.emit()

    def insert_productList(self, prods: [Product]):
        self.beginResetModel()
        for p in prods:
            if p.get_countInBasket() > 0:
                self.m_data.append(p)
        self.endResetModel()


    def removeProducts(self, prods: [Product]):
        for prod in prods:
            for factor in self.m_data:
                if prod.barcode == factor.barcode:
                    idx = self.m_data.index(factor)
                    # ix = self.index(self.m_data.index(factor), 0)
                    if (factor.countInBasket - prod.countInBasket) == 0:
                        self.beginRemoveRows(QModelIndex(), idx, idx)
                        del self.m_data[idx]
                        self.endRemoveRows()
                    else:
                        ix = self.index(self.m_data.index(factor), 0)
                        self.m_data[idx].set_countInBasket(
                            factor.countInBasket - prod.countInBasket)
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
                if prod.barcode == factor.barcode:
                    ix = self.index(self.m_data.index(factor), 0)
                    factor.set_countInBasket(
                        factor.countInBasket - prod.countInBasket)
                    self.dataChanged.emit(ix, ix, self.roleNames())
        self.changed.emit()

    @Slot(result=bool)
    def reset(self):
        self.beginResetModel()
        self.resetInternalData()  # should work without calling it ?
        self.endResetModel()
        return True

    def validBarcodeSetForRemove(self, data: [Product], RemovedWight):
        lst_1 = []
        for item in data:
            if item.meanWeight <= RemovedWight + item.tolerance + 8:
                for i in range(item.countInBasket):
                    lst_1.append(item.barcode)
        self.setValidBarcodeSetForDelete(lst_1)
        self.m_removedWeightMax = RemovedWight
        self.m_removedWeightMin = RemovedWight

    def updateValidBarcodeSetForRemove(self, product: Product):
        removeAllProduct = False
        acceptableBarcode = False
        removeSuccessfullyBefor = False
        avgWeight = product.meanWeight
        tolerance = product.tolerance
        if product.barcode in self.m_validBarcodeSetForDelete:
            if (self.m_removedWeightMax - avgWeight + (tolerance + 8)) >= 0:
                acceptableBarcode = True
                self.m_validBarcodeSetForDelete.remove(product.barcode)
                self.beginResetModel()
                self.insertProduct(product, 1)
                self.endResetModel()
                self.changed.emit()
                self.m_removedWeightMin = self.m_removedWeightMin - \
                                          avgWeight - (tolerance + 8)
                self.m_removedWeightMax = self.m_removedWeightMax - \
                                          avgWeight + (tolerance + 8)
        if not acceptableBarcode:
            for prod in self.m_data:
                if product.barcode == prod.barcode:
                    removeSuccessfullyBefor = True
        if self.m_removedWeightMin <= 0 and self.m_removedWeightMax >= 0:
            removeAllProduct = True
        # print(self.m_removedWeightMax)
        # print(self.m_removedWeightMin)
        return acceptableBarcode, removeAllProduct, removeSuccessfullyBefor

    @Slot(int)
    def increaseClicked(self, index: int):
        ix = self.index(index, 0)

        # self.beginResetModel()
        self.m_data[index].set_countInBasket(self.m_data[index].get_countInBasket() + 1)
        # self.endResetModel()
        self.dataChanged.emit(ix, ix, self.roleNames())

    @Slot(int)
    def decreaseClicked(self, index: int):
        ix = self.index(index, 0)
        # self.m_data[index].settedad(self.m_data[index].gettedad() + 1)
        # self.beginResetModel()
        if self.m_data[index].get_countInBasket() > 0:
            self.m_data[index].set_countInBasket(self.m_data[index].get_countInBasket() - 1)
        # self.endResetModel()
        self.dataChanged.emit(ix, ix, self.roleNames())

    # @Slot()
    # def checkForProductsChange(self,lst:[Product]):
    #     changed = False
    #     for index, prod in enumerate(lst):
    #         if(prod.getunitCount() < self.m_data[index].getunitCount()):
    #             ix = self.index(index, 0)
    #             self.m_data[index].setDataModelShow(1)
    #             self.dataChanged.emit(ix, ix, self.roleNames())
    #             changed = True
    #         if(prod.getnotValid() > 0):
    #             ix = self.index(index, 0)
    #             self.m_data[index].setDataModelShow(1)
    #             self.dataChanged.emit(ix, ix, self.roleNames())
    #             changed = True
    #     return changed
