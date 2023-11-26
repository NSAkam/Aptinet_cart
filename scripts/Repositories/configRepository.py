from Services.dal import DAL
from PySide2.QtSql import QSqlQuery
from Models.config import Config
import os


class ConfigRepositories():

    dal: DAL

    def __init__(self, dataAccessLayer: DAL) -> None:
        self.dal = dataAccessLayer
        self.dal.Connect()
    
    def get_appVersion(self):
        query = QSqlQuery()
        appversion = -1
        query.exec_("select appVersion from Config")
        while query.next():
            appversion = query.value(0)
        return appversion
    
    def get_dbVersion(self):
        query = QSqlQuery()
        appversion = -1
        query.exec_("select dbVersion from Config")
        while query.next():
            appversion = query.value(0)
        return appversion
    
    def get_imagesVersion(self):
        query = QSqlQuery()
        appversion = -1
        query.exec_("select imagesVersion from Config")
        while query.next():
            appversion = query.value(0)
        return appversion
    
    def get_Config(self):
        query = QSqlQuery()
        query.exec_("select storeId,is_kg,currency,appVersion,dbVersion,imagesVersion,basketName from Config LIMIT 1")
        c = Config()
        while query.next():
            print("sdiashodkasdjuiasjdopas")
            c.storeId = query.value(0)
            c.isKg = query.value(1)
            c.currency = query.value(2)
            c.appVersion = query.value(3)
            print(query.value(3))
            c.dbVersion = query.value(4)
            c.imagesVersion = query.value(5)
            c.basketName = query.value(6)
        return c
