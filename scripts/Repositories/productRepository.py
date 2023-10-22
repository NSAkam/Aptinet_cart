from PySide2.QtSql import QSqlQuery


class ProductRepository:
    
    def __init__(self) -> None:
        self.query = QSqlQuery()
    
    def get_products(self, barcode):
        self.query.prepare(
            "SELECT name, price, finalPrice, description, rate, tax, commentCount, meanWeight"
            "FROM product"
            "WHERE barcode = :barcode"
            )
        self.query.bindValue(":barcode", barcode)
        while self.query.next():
            name = self.query.value("name")
            price = self.query.value("price")
            finalPrice = self.query.value("finalPrice")
            description = self.query.value("description")
            rate = self.query.value("rate")
            tax = self.query.value("tax")
            commentCount = self.query.value("commentCount")
            meanWeight = self.query.value("meanweight")
            return name , price, finalPrice, description, rate, tax, commentCount, meanWeight
        
    def get_is_plu_product(self):
        self.query.prepare(
            "SELECT name, price, finalPrice, description, rate, tax, commentCount, meanWeight"
            "FROM product"
            "WHERE isPlu = 'true'"
            )
        while self.query.next():
            name = self.query.value("name")
            price = self.query.value("price")
            finalPrice = self.query.value("finalPrice")
            description = self.query.value("description")
            rate = self.query.value("rate")
            tax = self.query.value("tax")
            commentCount = self.query.value("commentCount")
            meanWeight = self.query.value("meanweight")
            return name , price, finalPrice, description, rate, tax, commentCount, meanWeight
        
    def get_offer_list(self):
        self.query.prepare(
            "SELECT name, price, finalPrice, description, rate, tax, commentCount, meanWeight"
            "FROM product"
            "WHERE isOffer = 'true'"
            )
        while self.query.next():
            name = self.query.value("name")
            price = self.query.value("price")
            finalPrice = self.query.value("finalPrice")
            description = self.query.value("description")
            rate = self.query.value("rate")
            tax = self.query.value("tax")
            commentCount = self.query.value("commentCount")
            meanWeight = self.query.value("meanweight")
            return name , price, finalPrice, description, rate, tax, commentCount, meanWeight
        
    def get_email_by_name(self, name):
        self.query.prepare(
            "SELECT email FROM ServerUser WHERE name = :name"
        )
        self.query.bindValue(":name", name)
        while self.query.next():
            email = self.query.value("email")
            return email
        
    def get_factore_by_phone(self, phone):
        self.query.prepare(
            "SELECT count, price, finalPrice"
            "FROM userFactor"
            "JOIN ServerUser ON userFactore.uid  = ServerUser.id"
            "WHERE ServerUser.phone = :phone"
        )
        self.query.bindValue(":phone", phone)
        while self.query.next():
            count = self.query.value("count")
            price = self.query.value("price")
            finalPrice = self.query.value("finalPrice")
            return count, price, finalPrice
        
    def get_factore_by_email(self, email):
        self.query.prepare(
            "SELECT count, price, finalPrice"
            "FROM userFactor"
            "JOIN ServerUser ON userFactore.uid  = ServerUser.id"
            "WHERE ServerUser.email = :email"
        )
        self.query.bindValue(":email", email)
        while self.query.next():
            count = self.query.value("count")
            price = self.query.value("price")
            finalPrice = self.query.value("finalPrice")
            return count, price, finalPrice
        
    def get_factore_by_id(self, id):
        self.query.prepare(
            "SELECT p.name, uf.count, uf.price, uf.finalPrice"
            "FROM userFactor as uf"
            "JOIN product AS p ON uf.productBarcode = p.barcode"
            "WHERE uf.id = :id"
        )
        self.query.bindValue(":id", id)
        while self.query.next():
            name = self.query.value("name")
            count = self.query.value("count")
            price = self.query.value("price")
            finalPrice = self.query.value("finalPrice")
            return name, count, price, finalPrice
        
    def get_suggestion_product(self):
        self.query.prepare(
            "SELECT finalPrice, name"
            "FROM product"
            "JOIN suggestion ON ps_barcode"
            "WHERE suggestion.ps_barcode = product.barcode"
        )
        while self.query.next():
            name = self.query.value("name")
            finalPrice = self.query.value("finalPrice")
            return finalPrice, name
        
        
        
    
        
    
        