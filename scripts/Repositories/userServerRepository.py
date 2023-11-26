from Services.dal import DAL
from PySide2.QtSql import QSqlQuery
from Models.serverUser import ServerUser
import os


class UserServerRepository():

    dal: DAL

    def __init__(self, dataAccessLayer: DAL) -> None:
        self.dal = dataAccessLayer
        self.dal.Connect()

    def insertData(self, id:str,loyalityBarcode:str,name:str,email:str,phone:str,offerPercentage:str,offerLimitedPercentage:str,offerMount:str):
        query = QSqlQuery()
        if (query.exec_("insert into  ServerUser "
                        "(id,loyalityBarcode,name,email,phone,offerPercentage,offerLimitedPercentage,offerMount) "
                        "values "
                        "('"+id+"','"+loyalityBarcode+"','"+name+"','"+email+"','"+phone+"','"+offerPercentage+"','"+offerLimitedPercentage+"','"+offerMount+"')") == False):
            return True
        else:
            return False
        


