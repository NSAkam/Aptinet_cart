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
    
    def get_lang(self):
        query = QSqlQuery()
        lang = -1  
        query.exec_("select lang from Config LIMIT 1")
        while query.next():
            lang = query.value(0)
        return lang
    
    def set_lang(self,lang:str):
        query = QSqlQuery()
        appversion = -1
        query.exec_("update Config set lang = '"+str(lang)+"'")
        while query.next():
            appversion = query.value(0)
        return appversion
    
    def set_calibrationDate(self,date:str):
        query = QSqlQuery()
        appversion = -1
        query.exec_("update Config set calibrationDate = '"+str(date)+"'")
        while query.next():
            appversion = query.value(0)
        return appversion

    def set_quatifire(self,value:str):
        query = QSqlQuery()
        appversion = -1
        query.exec_("update Config set quatifire = '"+str(value)+"'")
        while query.next():
            appversion = query.value(0)
        return appversion
    
    def set_taxPercentage(self,value:str):
        query = QSqlQuery()
        appversion = -1
        query.exec_("update Config set taxPercentage = '"+str(value)+"'")
        while query.next():
            appversion = query.value(0)
        return appversion
    
    
    def get_Config(self):
        query = QSqlQuery()
        c = Config()
        query.exec_("select storeId,quatifire,currency,appVersion,dbVersion,imagesVersion,basketName,taxPercentage,calibrationDate from Config LIMIT 1")
        while query.next():
            c.storeId = query.value(0)
            c.quatifire = query.value(1)
            c.currency = query.value(2)
            c.appVersion = query.value(3)
            c.dbVersion = query.value(4)
            c.imagesVersion = query.value(5)
            c.basketName = query.value(6)
            c.taxPercentage = query.value(7)
            c.calibrationDate = query.value(8)
        return c
