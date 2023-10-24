from PySide2.QtSql import QSqlQuery


class ProductRepository:
    
    def __init__(self) -> None:
        self.query = QSqlQuery()
    
    def get_products_list(self, barcode):
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
        
    def get_is_plu_products(self):
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
        
    def get_user_by_email(self, email):
        self.query.prepare(
            "SELECT name, email, phone, offer, code FROM ServerUser WHERE email = :email"
        )
        self.query.bindValue(":email", email)
        while self.query.next():
            name = self.query.value("name")
            phone = self.query.value("phone")
            offer = self.query.value("offer")
            code = self.query.value("code")
            return name, phone, offer, code
        
    def get_user_by_phone(self, phone):
        self.query.prepare(
            "SELECT name, email, offer, code FROM ServerUser WHERE phone = :phone"
        )
        self.query.bindValue(":phone", phone)
        while self.query.next():
            name = self.query.value("name")
            email = self.query.value("email")
            offer = self.query.value("offer")
            code = self.query.value("code")
            return name, email, offer, code
        
        
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
            "SELECT p.name, uf.count, uf.price, uf.finalPrice, uf.tax"
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
        
    
    def get_product_list(self, barcode, qr):
        self.query.prepare(
            "SELECT name, price, finalPrice, description, rate, commentCount, w1, w2, w3, w4 ,w5, w6, w7, w8, w9, w10, meanWeight, tolerance, insertedWeight, isOffer, isPlu, tax, taxPrice"
            "FROM product"
            "WHERE barcode = :barcode OR qr = :qr"
            )
        self.query.bindValue(":barcode", barcode)
        self.query.bindValue(":qr", qr)
        while self.query.next():
            name = self.query.value("name")
            price = self.query.value("price")
            finalprice = self.query.value("finalPrice")
            description = self.query.value("description")
            rate = self.query.value("rate")
            commentCount = self.query.value("commentCount")
            w1 = self.query.value("w1")
            w2 = self.query.value("w2")
            w3 = self.query.value("w3")
            w4 = self.query.value("w4")
            w5 = self.query.value("w5")
            w6 = self.query.value("w6")
            w7 = self.query.value("w7")
            w8 = self.query.value("w8")
            w9 = self.query.value("w9")
            w10 = self.query.value("w10")
            meanweight = self.query.value("meanWeight")
            tolerance = self.query.value("tolerance")
            insertedWeight = self.query.value("insertedWeight")
            isOffer = self.query.value("isOffer")
            isPlu = self.query.value("isPlu")
            tax = self.query.value("tax")
            taxPrice = self.query.value("taxPrice")

            return name, price, finalprice, description, rate, commentCount, w1, w2, w3, w4, w5, w6, w7, w8, w9, w10, meanweight, tolerance, insertedWeight, isOffer, isPlu, tax, taxPrice
        
        
    
        
    
        