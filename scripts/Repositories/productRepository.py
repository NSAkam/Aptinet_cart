from Services.dal import DAL
from PySide2.QtSql import QSqlQuery
from models.product import Product


class ProductRepository:
    
    def __init__(self) -> None:
        self.dal = DAL()
        self.dal.Connect()
        self.query = QSqlQuery()
        
    def get_user_by_email(self, email):
        self.query.prepare("SELECT * FROM ServerUser WHERE email = :email")
        self.query.bindValue(":email", email)
        if self.query.exec_():
            while self.query.next():
                name = self.query.value("name")
                phone = self.query.value("phone")
                offer = self.query.value("offer")
                code = self.query.value("code")
            return name, phone, offer, code
        
    def get_user_by_phone(self, phone):
        self.query.prepare("SELECT * FROM ServerUser WHERE phone = :phone")
        self.query.bindValue(":phone", phone)
        if self.query.exec_():
            while self.query.next():
                name = self.query.value("name")
                email = self.query.value("email")
                offer = self.query.value("offer")
                code = self.query.value("code")
            return name, email, offer, code
        
    def get_user_by_code(self, code):
        self.query.prepare("SELECT * FROM ServerUser WHERE code = :code")
        self.query.bindValue(":code", code)
        if self.query.exec_():
            while self.query.next():
                name = self.query.value("name")
                email = self.query.value("email")
                offer = self.query.value("offer")
                phone = self.query.value("phone")
            return name, email, offer, phone
        
    def get_product_barcode(self, barcode):
        self.query.prepare("SELECT * FROM product WHERE barcode = :barcode")
        self.query.bindValue(":barcode", barcode)
        if self.query.exec_():
            while self.query.next():
                name = self.query.value("name")
                price = self.query.value("price")
                final_price = self.query.value("final_price")
                description = self.query.value("description")
            return name, price, final_price, description
        
    def get_product_offer_list(self):
        self.query.exec_(
            "SELECT * FROM product WHERE is_offer = True"
        )
        while self.query.next():
                name = self.query.value("name")
                price = self.query.value("price")
                final_price = self.query.value("final_price")
                description = self.query.value("description")
        return name, price, final_price, description
        
    def get_factore_by_id(self, id):
        self.query.prepare("SELECT * FROM userFactor WHERE id = :id")
        self.query.bindValue(":id", id)
        if self.query.exec_():
            while self.query.next():
                count = self.query.value("count")
                price = self.query.value("price")
                final_price = self.query.value("final_price")
                tax = self.query.value("tax")
            return count, price, final_price, tax
        
    def get_suggestion_barcode(self, barcode):
        self.query.exec_(
            "SELECT * FROM product INNER JOIN suggestion ON product.barcode = suggestion.barcode"
            )
        if self.query.exec_():
            while self.query.next():
                qr = self.query.value("qr")
                name = self.query.value("name")
                final_price = self.query.value("final_price")
                tax = self.query.value("tax")
            return qr, name, final_price, tax
    
    def get_one_product(self, id):
        self.query.prepare("SELECT * FROM product WHERE id = :id LIMIT 1")
        self.query.bindValue(":id", id)
        while self.query.next():
            product_name = self.query.value(1)
        
        
    def insert_into_userfactor(self):
        self.query.exec_("SELECT barcode FROM product")
        while self.query.next():
            barcode = self.query.value(0)
            self.query.prepare(
                "UPDATE userFactor SET count = count + 1 WHERE barcode = :barcode"
            )
            self.query.bindValue(":barcode", barcode)
            self.query.exec()
            
    def get_product_list(self):
       if self.query.exec_("SELECT * FROM product"):
        while self.query.next():
            product_name = self.query.value(1)
            product_description = self.query.value(2)
            product_rate = self.query.value(3) 
            product_comment_count = self.query.value(4)
            product_w1 = self.query.value(5)
              