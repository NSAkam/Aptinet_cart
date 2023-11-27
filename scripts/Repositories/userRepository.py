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
        now = datetime.datetime.now()
        TotalSeconds = (now - datetime.datetime(1970,1,1)).timestamp()
        query = QSqlQuery()
        if query.exec_("insert into User (regtime) values ('"+TotalSeconds+"')"):
            query.exec_("SELECT MAX(id) FROM User")
            while query.next():
                userid = query.value(0)
            return userid
        else:
            return -1


    def get_userByEmail(self, email):
        query = QSqlQuery()
        query.exec_(
            "SELECT name, email, phone, offer, code FROM ServerUser WHERE email = '"+email+"'"
        )
        user = ServerUser()
        while query.next():
            user.set_name(query.value(0))
            user.set_email(query.value(1))
            user.set_phone(query.value(2))
            user.set_offer(query.value(3))
            user.set_code(query.value(4))
        return user
            
        
    def get_userByPhone(self, phone):
        query = QSqlQuery()
        query.exec_(
            "SELECT name, email, offer, code FROM ServerUser WHERE phone = '"+phone+"'"
        )
        user = ServerUser()
        while query.next():
            user.set_name(query.value(0))
            user.set_email(query.value(1))
            user.set_offer(query.value(2))
            user.set_code(query.value((3)))
        return user
    
    
                
                    
