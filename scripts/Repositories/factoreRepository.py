from PySide2.QtSql import QSqlQuery

from Services.dal import DAL
from Models.userFactore import UserFactoreModel
from Models.product import Product


class UserRepository:
    
    dal: DAL
    
    def __init__(self, dataAccessLayer: DAL) -> None:
        self.dal = dataAccessLayer
        self.dal.Connect()
        
    def get_factore_by_phone(self, phone):
        query = QSqlQuery()
        query.exec_(
            "SELECT count, price, finalPrice, tax"
            "FROM userFactor"
            "JOIN ServerUser ON userFactore.uid  = ServerUser.id"
            "WHERE ServerUser.phone = '"+phone+"'"
        )
        
        factore = UserFactoreModel()
        while query.next():
            factore.setCount(query.value(0))
            factore.setPrice(query.value(1))
            factore.setFinalprice(query.value(2))
            factore.setTax(query.value(3))
        return factore
            
        
    def get_factore_by_email(self, email):
        query = QSqlQuery()
        
        query.exec_(
            "SELECT count, price, finalPrice, tax"
            "FROM userFactor"
            "JOIN ServerUser ON userFactore.uid  = ServerUser.id"
            "WHERE ServerUser.email = '"+email+"'"
        )
        factore = UserFactoreModel()
        while query.next():
            factore.setCount(query.value(0))
            factore.setPrice(query.value(1))
            factore.setFinalprice(query.value(2))
            factore.setTax(query.value(3))
        return factore
            
        
    def get_factore_by_id(self, id):
        query = QSqlQuery()
        query.exec_(
            "SELECT p.name, uf.count, uf.price, uf.finalPrice, uf.tax"
            "FROM userFactor as uf"
            "JOIN product AS p ON uf.productBarcode = p.barcode"
            "WHERE uf.id = '"+id+"'"
        )
        p = Product()
        factore = UserFactoreModel()
        while query.next():
            factore.setCount(query.value(0))
            factore.setPrice(query.value(1))
            factore.setFinalprice(query.value(2))
            factore.setTax(query.value(3))
            p.setName(query.value(4))
        return factore, p
            