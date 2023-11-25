from ast import Dict
from typing import Any
from PySide2.QtCore import Signal, Property, QAbstractListModel, QModelIndex, Slot
from PySide2.QtCore import QModelIndex, Qt, QByteArray
from Services.dal import DAL
from Models.product import Product
from itertools import chain, combinations
from Repositories.productRepository import ProductRepository
from Services.Utiles import SpecialOfferWorker
from Models.productModel import ProductModel
from Services.dal import DAL

class ProductBypassModel(ProductModel):
    def __init__(self,dataaccesslayer : DAL):
        super().__init__(dataaccesslayer)

    @Slot(int)
    def increaseClicked(self, index: int):
        ix = self.index(index, 0)
        # self.beginResetModel()
        self.m_data[index].setCountInBasket(self.m_data[index].getCountInBasket() + 1)
        # self.endResetModel()
        self.dataChanged.emit(ix, ix, self.roleNames())

    @Slot(int)
    def decreaseClicked(self, index: int):
        ix = self.index(index, 0)
        # self.m_data[index].settedad(self.m_data[index].gettedad() + 1)
        # self.beginResetModel()
        if self.m_data[index].getCountInBasket() > 0:
            self.m_data[index].setCountInBasket(self.m_data[index].setCountInBasket() - 1)
        # self.endResetModel()
        self.dataChanged.emit(ix, ix, self.roleNames())

    def removeObject(self):
        print(
            ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ProductModel Deleted <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
        self.repository.Disconnect()
        del self.repository


