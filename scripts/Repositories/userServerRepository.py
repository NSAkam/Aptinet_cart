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
        
    def loginByPhone(self,phone:str):
        query = QSqlQuery()
        query.exec_(
            "select id,loyalityBarcode,name,email,phone,offerPercentage,offerLimitedPercentage,offerMount from ServerUser where phone = '"+phone+"'"
            )
        us = ServerUser()
        while query.next():
            us.id =query.value(0)
            us.loyalityBarcode =query.value(1)
            us.name =query.value(2)
            us.email =query.value(3)
            us.phone =query.value(4)
            us.offerPercentage =query.value(5)
            us.offerLimitedPercentage =query.value(6)
            us.offerMount =query.value(7)
        return us
    
    def loginByloyalityBarcode(self,loginByloyalityBarcode:str):
        query = QSqlQuery()
        query.exec_(
            "select id,loyalityBarcode,name,email,phone,offerPercentage,offerLimitedPercentage,offerMount from ServerUser where loyalityBarcode = '"+loginByloyalityBarcode+"'"
            )
        us = ServerUser()
        while query.next():
            us.id =query.value(0)
            us.loyalityBarcode =query.value(1)
            us.name =query.value(2)
            us.email =query.value(3)
            us.phone =query.value(4)
            us.offerPercentage =query.value(5)
            us.offerLimitedPercentage =query.value(6)
            us.offerMount =query.value(7)
        return us
        


