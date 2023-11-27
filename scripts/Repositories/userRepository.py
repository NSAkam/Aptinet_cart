import sqlite3
from PySide2.QtSql import QSqlQuery

from Services.dal import DAL
from Models.serverUser import ServerUser
from Models.user import User
import datetime


class UserRepository:

    dal: DAL

    def __init__(self, dataAccessLayer: DAL) -> None:
        self.dal = dataAccessLayer
        self.dal.Connect()

    def create_user(self):
        TotalSeconds = datetime.datetime.now().timestamp()
        u = User()
        u.id = -1
        query = QSqlQuery()
        if query.exec_("insert into User (regtime) values ('"+TotalSeconds+"')"):
            query.exec_("SELECT MAX(id) FROM User")
            while query.next():
                u.id = query.value(0)
            return u
        else:
            return -1

    def updateUserServerID(self, userid: int, usid: str):
        query = QSqlQuery()
        if (query.exec_("update User set USID = '"+usid+"' where id = '"+str(userid)+"'")):
            return True
        else:
            return False
