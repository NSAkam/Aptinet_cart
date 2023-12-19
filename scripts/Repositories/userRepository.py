import sqlite3
from PySide2.QtSql import QSqlQuery

from Services.dal import DAL
from Models.serverUser import ServerUser
from Models.user import User
import datetime
import uuid


class UserRepository:

    dal: DAL

    def __init__(self, dataAccessLayer: DAL) -> None:
        self.dal = dataAccessLayer
        self.dal.Connect()

    def create_user(self):
        TotalSeconds = datetime.datetime.now().timestamp()
        u = User()
        u.id = "-1"
        newUserID = str(uuid.uuid4())
        query = QSqlQuery()
        if query.exec_("insert into User (id,regtime) values ('"+newUserID+"','"+str(TotalSeconds)+"')"):
            u.id = newUserID
            return u
        else:
            return -1

    def updateUserServerID(self, userid: str, usid: str):
        query = QSqlQuery()
        if (query.exec_("update User set USID = '"+usid+"' where id = '"+str(userid)+"'")):
            return True
        else:
            return False

    def updateRate(self, userid: str, rate: str):
        query = QSqlQuery()
        if (query.exec_("update User set Rate = '"+rate+"' where id = '"+str(userid)+"'")):
            return True
        else:
            return False

    def updateEmail(self, userid: str, email: str):
        query = QSqlQuery()
        if (query.exec_("update User set email = '"+email+"' where id = '"+str(userid)+"'")):
            return True
        else:
            return False

    def updateFactorprices(self, userid: str, factorPrice: str, finalFactorPrice: str, OfferCode: str):
        query = QSqlQuery()
        if (query.exec_("update User set factorPrice= '"+factorPrice+"',finalFactorPrice='"+finalFactorPrice+"',OfferCode='"+OfferCode+"' where id = '"+str(userid)+"'")):
            return True
        else:
            return False
