from Services.dal import DAL
from PySide2.QtSql import QSqlQuery
from Models.product import Product
import os


class AdminUserRepository():

    dal: DAL

    def __init__(self, dataAccessLayer: DAL) -> None:
        self.dal = dataAccessLayer
        self.dal.Connect()

    def Login(self, adminBarcode: str):
        res = False
        query = QSqlQuery()
        query.exec_("select name from admins where barcode = '"+adminBarcode+"'")
        while query.next():
            if(len(query.value(0))>0):
                res = True
        return res
