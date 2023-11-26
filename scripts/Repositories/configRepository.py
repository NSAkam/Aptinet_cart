from Services.dal import DAL
from PySide2.QtSql import QSqlQuery
import os


class ConfigRepositories():

    dal: DAL

    def __init__(self, dataAccessLayer: DAL) -> None:
        self.dal = dataAccessLayer
        self.dal.Connect()
    
    def get_appVersion():
        query = QSqlQuery()
        appversion = -1
        query.exec_("select appVersion from Config")
        while query.next():
            appversion = query.value(0)
        return appversion
    
    def get_dbVersion():
        query = QSqlQuery()
        appversion = -1
        query.exec_("select dbVersion from Config")
        while query.next():
            appversion = query.value(0)
        return appversion
    
    def get_imagesVersion():
        query = QSqlQuery()
        appversion = -1
        query.exec_("select imagesVersion from Config")
        while query.next():
            appversion = query.value(0)
        return appversion
