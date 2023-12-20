from PySide2.QtSql import QSqlQuery

from Services.dal import DAL


class UserFactoreRepository:

    dal: DAL

    def __init__(self, dataAccessLayer: DAL) -> None:
        self.dal = dataAccessLayer
        self.dal.Connect()

    def insertFactor(self, userid: str, Productbarcode: str, Count: str, Weight: str, Price: str, FinalPrice: str, tax: str, saving: str):
        query = QSqlQuery()
        if (query.exec_("insert into userFactor (UserId,Productbarcode,Count,Weight,Price,FinalPrice,tax,saving) VALUES ('"+str(userid)+"','"+Productbarcode+"','"+Count+"','"+Weight+"','"+Price+"','"+FinalPrice+"','"+tax+"','"+saving+"')")):
            return True
        else:
            return False
