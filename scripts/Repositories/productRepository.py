from Services.dal import DAL
from PySide2.QtSql import QSqlQuery
from models.product import Product


class ProductRepository:
    
    def __init__(self) -> None:
        self.dal = DAL()
        self.dal.Connect()
        self.query = QSqlQuery()
        
    def get_user_by_email(self, email):
        self.query.prepare("SELECT * FROM user WHERE email = :email")
        self.query.bindValue(":email", email)
        self.query.exec()
        
    def get_user_by_phone(self, phone):
        self.query.prepare("SELECT * FROM user WHERE phone = :phone")
        self.query.bindValue(":phone", phone)
        self.query.exec()
        
    def get_user_by_code(self, code):
        self.query.prepare("SELECT * FROM user WHERE code = :code")
        self.query.bindValue(":code", code)
        self.query.exec()
        
    def get_product_barcode(self, barcode):
        self.query.prepare("SELECT * FROM product WHERE barcode = :barcode")
        self.query.bindVaue(":barcode", barcode)
        self.query.exec()
        
    def get_product_offer_list(self):
        self.query.exec_(
            "SELECT * FROM product WHERE is_offer = True"
        )
        
    def get_factore_by_id(self, id):
        self.query.prepare("SELECT * FROM factor WHERE id = :id")
        self.query.bindValue(":id", id)
        self.query.exec()
        
    def get_suggestion_barcode(self, barcode):
        self.query.exec_(
            "SELECT * FROM product INNER JOIN suggestion ON product.barcode = suggestion.barcode"
            )
    
    def get_one_product(self, id):
        self.query.prepare("SELECT * FROM product WHERE id = :id LIMIT 1")
        self.query.bindValue(":id", id)
        self.query.exec()
        
    def insert_into_factorlist(self):
        self.query.exec_("SELECT barcode FROM product")
        while self.query.next():
            barcode = self.query.value(0)
            self.query.prepare(
                "UPDATE factorlist SET count = count + 1 WHERE barcode = :barcode"
            )
            self.query.bindValue(":barcode", barcode)
            self.query.exec()
            
        
        
        