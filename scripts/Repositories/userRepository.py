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
        
    def get_user_by_email(self, email):
        query = QSqlQuery()
        
        query.exec_(
            "SELECT name, email, phone, offer, code FROM ServerUser WHERE email = '"+email+"'"
        )
        user = ServerUser()
        while query.next():
            user.setName(query.value(0))
            user.setEmail(query.value(1))
            user.setPhone(query.value(2))
            user.setOffer(query.value(3))
            user.setCode(query.value(4))
        return user
            
        
    def get_user_by_phone(self, phone):
        query = QSqlQuery()
        query.exec_(
            "SELECT name, email, offer, code FROM ServerUser WHERE phone = '"+phone+"'"
        )
        user = ServerUser()
        while query.next():
            user.setName(query.value(0))
            user.setEmail(query.value(1))
            user.setOffer(query.value(2))
            user.setCode(query.value((3)))
        return user
    
    def create_user(self, email):
        query = QSqlQuery()
        serveruser_id = 0
        query.exec_("SELECT id FROM ServerUser as us WHERE email = '"+email+"'")
        while query.next():
            serveruser_id = query.value(0)
        if serveruser_id > 0 :
            try:
                if query.exec_("INSERT INTO User(usId) VALUES(serveruser_id)"):
                    query.exec_("SELECT MAX(id) FROM User")
                    while query.next():
                        id = query.value(0)
                        return id
            except sqlite3.Error as e:
                print(f"Error: {e}")
        return None
                
                    
