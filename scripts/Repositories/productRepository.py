from PySide2.QtSql import QSqlQuery

from Services.dal import DAL
from Models.product import Product


class ProductRepository:
    
    dal: DAL
    
    def __init__(self, dataAccessLayer: DAL) -> None:
        self.dal = dataAccessLayer
        self.dal.Connect()
    
    def get_product(self, barcode):
        query = QSqlQuery()
        
        query.exec_(
            "SELECT name, price, finalPrice, description, rate, tax, commentCount, meanWeight"
            "FROM product"
            "WHERE barcode = '"+barcode+"'"
            )
        p = Product()
        while query.next():
            p.setName(query.value(0))
            p.setPrice(query.value(1))
            p.setFinalprice(query.value(2))
            p.setDescription(query.value(3))
            p.setRate(query.value(4))
            p.setTax(query.value(5))
            p.setCommentcount(query.value(6))
            p.setMeanweight(query.value(7))
        return p
            
            
        
    def get_is_plu_products(self):
        query = QSqlQuery()
        query.exec_(
            "SELECT barcode, qr, name, price, finalPrice, description, rate, tax, commentCount, meanWeight, tolerance, insertedWeight, isOffer, taxPrice"
            "FROM product"
            "WHERE isPlu = 'true'"
            )
        p = Product()
        while query.next():
            p.setBarcode(query.value(0))
            p.setQr(query.value(1))
            p.setName(query.value(2))
            p.setPrice(query.value(3))
            p.setFinalprice(query.value(4))
            p.setDescription(query.value(5))
            p.setRate(query.value(6))
            p.setTax(query.value(7))
            p.setCommentcount(query.value(8))
            p.setTolerance(query.value(9))
            p.setIsoffer(query.value(10))
            p.setIsplu(query.value(11))
        return p
    
        
    def get_offer_list(self):
        query = QSqlQuery()
        query.exec_(
            "SELECT barcode, qr, name, price, finalPrice, description, rate, tax, commentCount, meanWeight, tolerance, insertedWeight, isPlu, taxPrice"
            "FROM product"
            "WHERE isOffer = 'true'"
            )
        p = Product()
        while query.next():
            p.setBarcode(query.value(0))
            p.setQr(query.value(1))
            p.setName(query.value(2))
            p.setPrice(query.value(3))
            p.setFinalprice(query.value(4))
            p.setDescription(query.value(5))
            p.setRate(query.value(6))
            p.setTax(query.value(7))
            p.setCommentcount(query.value(8))
            p.setTolerance(query.value(9))
            p.setIsplu(query.value(11))
        return p
        
        
    def get_suggestion_product(self):
        query = QSqlQuery()
        query.exec_(
            "SELECT finalPrice, name"
            "FROM product"
            "JOIN suggestion ON ps_barcode"
            "WHERE suggestion.ps_barcode = product.barcde"
        )
        p = Product()
        while query.next():
            p.setFinalprice(query.value(0))
            p.setName(query.value(1))
        return p
               
    
    def get_product_list(self, barcode, qr):
        query = QSqlQuery()
        self.query.prepare(
            "SELECT name, price, finalPrice, description, rate, commentCount, w1, w2, w3, w4 ,w5, w6, w7, w8, w9, w10, meanWeight, tolerance, insertedWeight, isOffer, isPlu, tax, taxPrice"
            "FROM product"
            "WHERE barcode = '"+barcode+"' OR qr = '"+qr+"'"
            )
        p = Product()
        while query.next():
            p.setName(query.value(2))
            p.setPrice(query.value(3))
            p.setFinalprice(query.value(4))
            p.setDescription(query.value(5))
            p.setRate(query.value(6))
            p.setCommentcount(query.value(7))
            p.setW1(query.value(8))
            p.setW2(query.value(9))
            p.setW3(query.value(10))
            p.setW4(query.value(11))
            p.setW5(query.value(12))
            p.setW6(query.value(13))
            p.setW7(query.value(14))
            p.setW8(query.value(15))
            p.setW9(query.value(16))
            p.setW10(query.value(17))
            p.setMeanweight(query.value(18))
            p.setTolerance(query.value(19))
            p.setInsertedweight(query.value(20))
            p.setIsoffer(query.value(21))
            p.setIsplu(query.value(22))
            p.setTax(query.value(23))
            p.setTaxprice(query.value(24))
        return p
            
            
            
        
        
    
        
    
        