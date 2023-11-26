from Services.dal import DAL
from PySide2.QtSql import QSqlQuery
from Models.product import Product
from Models.admin import Admin
import os


class AdminRepository():

    dal: DAL

    def __init__(self, dataAccessLayer: DAL) -> None:
        self.dal = dataAccessLayer
        self.dal.Connect()

    def insertALLData(self, adminsList: [Admin]):
        res = True
        query = QSqlQuery()
        for admin in adminsList:
            if (query.exec_("insert into admins (barcode,name) VALUES ('"+admin.barcode+"','"+admin.name+"')") == False):
                res = False
        return res
    
    def insertData(self, barcode:str,name:str):
        query = QSqlQuery()
        if (query.exec_("insert into admins (barcode,name) VALUES ('"+barcode+"','"+name+"')") == False):
            return True
        else:
            return False
    
    
    def Login(self, adminBarcode: str):
        res = False
        query = QSqlQuery()
        query.exec_("select name from admins where barcode = '" +
                    adminBarcode+"'")
        while query.next():
            if (len(query.value(0)) > 0):
                res = True
        return res
