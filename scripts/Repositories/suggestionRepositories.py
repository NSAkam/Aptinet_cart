from Services.dal import DAL
from PySide2.QtSql import QSqlQuery
from Models.suggestion import Suggestion
import os


class SuggestionRepositories():

    dal: DAL

    def __init__(self, dataAccessLayer: DAL) -> None:
        self.dal = dataAccessLayer
        self.dal.Connect()
        
    def deleteAll(self):
        query = QSqlQuery()
        query.exec_("delete from suggestion")

    def insertALLData(self, suglist: [Suggestion]):
        res = True
        query = QSqlQuery()
        for sug in suglist:
            if (query.exec_("insert into suggestion (Productid,Productidsuggested) values ('"+sug.Productid+"','"+sug.Productidsuggested+"')") == False):
                res = False
        return res
    
    def insertData(self, Productid:str,Productidsuggested:str):
        query = QSqlQuery()
        if (query.exec_("insert into suggestion (Productid,Productidsuggested) values ('"+Productid+"','"+Productidsuggested+"')") == False):
            return True
        else:
            return False
