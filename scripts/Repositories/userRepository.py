from PySide2.QtSql import QSqlQuery

from Services.dal import DAL
from Models.serverUser import ServerUser


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
            