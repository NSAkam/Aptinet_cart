import sqlite3
from PySide2.QtSql import QSqlQuery

from Services.dal import DAL
from Models.serverUser import ServerUser
from Models.user import User


class UserRepository:
    
    dal: DAL
    
    def __init__(self, dataAccessLayer: DAL) -> None:
        self.dal = dataAccessLayer
        self.dal.Connect()
        
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
    
    def create_user(self, email:str,regTime:int):
        query = QSqlQuery()
        serveruser_id = 0
        query.exec_("SELECT id FROM ServerUser as us WHERE email = '"+email+"'")
        while query.next():
            serveruser_id = query.value(0)
        if serveruser_id > 0 :
            userid = 0
            if query.exec_("INSERT INTO User (USID,email,regTime) VALUES('"+serveruser_id+"','"+email+"','"+regTime+"')"):
                query.exec_("SELECT MAX(id) FROM User")
                while query.next():
                    userid = query.value(0)
                return userid
            else:
                return -1
        else:
            userid = 0
            if query.exec_("INSERT INTO User (email,regTime) VALUES(email,regTime) VALUES('"+email+"','"+regTime+"')"):
                query.exec_("SELECT MAX(id) FROM User")
                while query.next():
                    id = query.value(0)
                return id
            else:
                return -1
        return -1
                
                    