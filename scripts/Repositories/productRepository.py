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
            p.set_name(query.value(0))
            p.set_price(query.value(1))
            p.set_finalPrice(query.value(2))
            p.set_description(query.value(3))
            p.set_rate(query.value(4))
            p.set_tax(query.value(5))
            p.set_commentCount(query.value(6))
            p.set_meanWeight(query.value(7))
        return p
            
            
        
    def get_isPluProducts(self):
        query = QSqlQuery()
        query.exec_(
            "SELECT barcode, qr, name, price, finalPrice, description, rate, tax, commentCount, meanWeight, tolerance, insertedWeight, isOffer, taxPrice"
            "FROM product"
            "WHERE isPlu = 'true'"
            )
        p = Product()
        while query.next():
            p.set_barcode(query.value(0))
            p.set_QR(query.value(1))
            p.set_name(query.value(2))
            p.set_price(query.value(3))
            p.set_finalPrice(query.value(4))
            p.set_description(query.value(5))
            p.set_rate(query.value(6))
            p.set_tax(query.value(7))
            p.set_commentCount(query.value(8))
            p.set_tolerance(query.value(9))
            p.set_isOffer(query.value(10))
            p.set_isPlu(query.value(11))
        return p
    
        
    def get_offerList(self):
        query = QSqlQuery()
        query.exec_(
            "SELECT barcode, qr, name, price, finalPrice, description, rate, tax, commentCount, meanWeight, tolerance, insertedWeight, isPlu, taxPrice"
            "FROM product"
            "WHERE isOffer = 'true'"
            )
        p = Product()
        while query.next():
            p.set_barcode(query.value(0))
            p.set_QR(query.value(1))
            p.set_name(query.value(2))
            p.set_price(query.value(3))
            p.set_finalPrice(query.value(4))
            p.set_description(query.value(5))
            p.set_rate(query.value(6))
            p.set_tax(query.value(7))
            p.set_commentCount(query.value(8))
            p.set_tolerance(query.value(9))
            p.set_isPlu(query.value(11))
        return p
        
        
    def get_suggestionProduct(self):
        query = QSqlQuery()
        query.exec_(
            "SELECT finalPrice, name"
            "FROM product"
            "JOIN suggestion ON ps_barcode"
            "WHERE suggestion.ps_barcode = product.barcde"
        )
        p = Product()
        while query.next():
            p.set_finalPrice(query.value(0))
            p.set_name(query.value(1))
        return p
               
    
    def get_productList(self, barcode, qr):
        query = QSqlQuery()
        query.exec_(
            "SELECT name, price, finalPrice, description, rate, commentCount, w1, w2, w3, w4 ,w5, w6, w7, w8, w9, w10, meanWeight, tolerance, insertedWeight, isOffer, isPlu, tax, taxPrice"
            "FROM product"
            "WHERE barcode = '"+barcode+"' OR qr = '"+qr+"'"
            )
        p = Product()
        while query.next():
            p.set_name(query.value(2))
            p.set_price(query.value(3))
            p.set_finalPrice(query.value(4))
            p.set_description(query.value(5))
            p.set_rate(query.value(6))
            p.set_commentCount(query.value(7))
            p.set_w1(query.value(8))
            p.set_w2(query.value(9))
            p.set_w3(query.value(10))
            p.set_w4(query.value(11))
            p.set_w5(query.value(12))
            p.set_w6(query.value(13))
            p.set_w7(query.value(14))
            p.set_w8(query.value(15))
            p.set_w9(query.value(16))
            p.set_w10(query.value(17))
            p.set_meanWeight(query.value(18))
            p.set_tolerance(query.value(19))
            p.set_insertedWeight(query.value(20))
            p.setIsoffer(query.value(21))
            p.set_isPlu(query.value(22))
            p.set_tax(query.value(23))
            p.set_taxPrice(query.value(24))
        return p
            
            
            
        
        
    
        
    
        