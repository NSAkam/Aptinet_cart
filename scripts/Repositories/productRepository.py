from PySide2.QtSql import QSqlQuery

from Services.dal import DAL
from Models.product import Product


class ProductRepository:
    
    dal: DAL
    
    def __init__(self, dataAccessLayer: DAL) -> None:
        self.dal = dataAccessLayer
        self.dal.Connect()

    def insertALLData(self, productList: [Product]):
        res = True
        query = QSqlQuery()
        for prod in productList:
            if (query.exec_("insert into product " 
                            "(name,description,rate,commentCount,w1,w2,w3,w4,w5,w6,w7,w8,w9,w10,price,finalprice,meanWeight,tolerance,insertedWeight,barcode,isOffer,isPlu,tax,qrCode,productType) "
					        "values "
                            "('"+prod.name+"','"+prod.description+"','"+prod.rate+"','"+prod.commentCount+"','"+prod.w1+"','"+prod.w2+"','"+prod.w3+"','"+prod.w4+"','"+prod.w5+"','"+prod.w6+"','"+prod.w7+"','"+prod.w8+"','"+prod.w9+"','"+prod.w10+"','"+prod.price+"','"+prod.finalprice+"','"+prod.meanWeight+"','"+prod.tolerance+"','"+prod.insertedWeight+"','"+prod.barcode+"','"+prod.isOffer+"','"+prod.isPlu+"','"+prod.tax+"','"+prod.qrCode+"','"+prod.productType+"')") == False):
                res = False
        return res
    
    def insertData(self, name:str,description:str,rate:int,commentCount:int,w1:int,w2:int,w3:int,w4:int,w5:int,w6:int,w7:int,w8:int,w9:int,w10:int,price:float,finalprice:float,meanWeight:int,tolerance:int,insertedWeight:int,barcode:str,isOffer:int,isPlu:int,tax:int,qrCode:str,productType:str):
        query = QSqlQuery()
        if (query.exec_("insert into product " 
                        "(name,description,rate,commentCount,w1,w2,w3,w4,w5,w6,w7,w8,w9,w10,price,finalprice,meanWeight,tolerance,insertedWeight,barcode,isOffer,isPlu,tax,qrCode,productType) "
		                "values "
                        "('"+name+"','"+description+"','"+rate+"','"+commentCount+"','"+w1+"','"+w2+"','"+w3+"','"+w4+"','"+w5+"','"+w6+"','"+w7+"','"+w8+"','"+w9+"','"+w10+"','"+price+"','"+finalprice+"','"+meanWeight+"','"+tolerance+"','"+insertedWeight+"','"+barcode+"','"+isOffer+"','"+isPlu+"','"+tax+"','"+qrCode+"','"+productType+"')") == False):
            return True
        else:
            return False
    
    def get_product(self, barcode):
        query = QSqlQuery()
        query.exec_(
            "SELECT name,description,rate,commentCount,w1,w2,w3,w4,w5,w6,w7,w8,w9,w10,price,finalprice,meanWeight,tolerance,insertedWeight,barcode,isOffer,isPlu,tax,qrCode,productType"
            "FROM product"
            "WHERE barcode = '"+barcode+"'"
            )
        p = Product()
        while query.next():
            p.name = query.value(0)
            p.description = query.value(1)
            p.rate = query.value(2)
            p.commentCount = query.value(3)
            p.w1 = query.value(4)
            p.w2 = query.value(5)
            p.w3 = query.value(6)
            p.w4 = query.value(7)
            p.w5 = query.value(8)
            p.w6 = query.value(9)
            p.w7 = query.value(10)
            p.w8 = query.value(11)
            p.w9 = query.value(12)
            p.w10 = query.value(13)
            p.price = query.value(14)
            p.finalPrice = query.value(15)
            p.meanWeight = query.value(16)
            p.tolerance = query.value(17)
            p.insertedWeight = query.value(18)
            p.barcode = query.value(19)
            p.isOffer = query.value(20)
            p.isPlu = query.value(21)
            p.tax = query.value(22)
            p.QR = query.value(23)
            p.productType = query.value(24)
        return p
    
    def get_topOfferProducts(self):
        res:[Product] = [] 
        query = QSqlQuery()
        query.exec_(
            "SELECT name,description,rate,commentCount,w1,w2,w3,w4,w5,w6,w7,w8,w9,w10,price,finalprice,meanWeight,tolerance,insertedWeight,barcode,isOffer,isPlu,tax,qrCode,productType"
            "FROM product"
            "WHERE isOffer = '1' limit 10"
            )
        while query.next():
            p = Product()
            p.name = query.value(0)
            p.description = query.value(1)
            p.rate = query.value(2)
            p.commentCount = query.value(3)
            p.w1 = query.value(4)
            p.w2 = query.value(5)
            p.w3 = query.value(6)
            p.w4 = query.value(7)
            p.w5 = query.value(8)
            p.w6 = query.value(9)
            p.w7 = query.value(10)
            p.w8 = query.value(11)
            p.w9 = query.value(12)
            p.w10 = query.value(13)
            p.price = query.value(14)
            p.finalPrice = query.value(15)
            p.meanWeight = query.value(16)
            p.tolerance = query.value(17)
            p.insertedWeight = query.value(18)
            p.barcode = query.value(19)
            p.isOffer = query.value(20)
            p.isPlu = query.value(21)
            p.tax = query.value(22)
            p.QR = query.value(23)
            p.productType = query.value(24)
            res.append(p)
        return res
    
    def get_offerProducts(self):
        res:[Product] = [] 
        query = QSqlQuery()
        query.exec_(
            "SELECT name,description,rate,commentCount,w1,w2,w3,w4,w5,w6,w7,w8,w9,w10,price,finalprice,meanWeight,tolerance,insertedWeight,barcode,isOffer,isPlu,tax,qrCode,productType"
            "FROM product"
            "WHERE isOffer = '1'"
            )
        while query.next():
            p = Product()
            p.name = query.value(0)
            p.description = query.value(1)
            p.rate = query.value(2)
            p.commentCount = query.value(3)
            p.w1 = query.value(4)
            p.w2 = query.value(5)
            p.w3 = query.value(6)
            p.w4 = query.value(7)
            p.w5 = query.value(8)
            p.w6 = query.value(9)
            p.w7 = query.value(10)
            p.w8 = query.value(11)
            p.w9 = query.value(12)
            p.w10 = query.value(13)
            p.price = query.value(14)
            p.finalPrice = query.value(15)
            p.meanWeight = query.value(16)
            p.tolerance = query.value(17)
            p.insertedWeight = query.value(18)
            p.barcode = query.value(19)
            p.isOffer = query.value(20)
            p.isPlu = query.value(21)
            p.tax = query.value(22)
            p.QR = query.value(23)
            p.productType = query.value(24)
            res.append(p)
        return res
    
            
    def get_suggesstionProducts(self,productBarcode:str):
        res:[Product] = [] 
        query = QSqlQuery()
        query.exec_(
                "select "
                "name,description,rate,commentCount,w1,w2,w3,w4,w5,w6,w7,w8,w9,w10,price,finalprice,meanWeight,tolerance,insertedWeight,barcode,isOffer,isPlu,tax,qrCode,productType "
                "from suggestion inner join product on suggestion.Productidsuggested = product.barcode where suggestion.Productid = '"+productBarcode+"'"
            )
        while query.next():
            p = Product()
            p.name = query.value(0)
            p.description = query.value(1)
            p.rate = query.value(2)
            p.commentCount = query.value(3)
            p.w1 = query.value(4)
            p.w2 = query.value(5)
            p.w3 = query.value(6)
            p.w4 = query.value(7)
            p.w5 = query.value(8)
            p.w6 = query.value(9)
            p.w7 = query.value(10)
            p.w8 = query.value(11)
            p.w9 = query.value(12)
            p.w10 = query.value(13)
            p.price = query.value(14)
            p.finalPrice = query.value(15)
            p.meanWeight = query.value(16)
            p.tolerance = query.value(17)
            p.insertedWeight = query.value(18)
            p.barcode = query.value(19)
            p.isOffer = query.value(20)
            p.isPlu = query.value(21)
            p.tax = query.value(22)
            p.QR = query.value(23)
            p.productType = query.value(24)
            res.append(p)
        return res


    def get_pluProducts(self):
        res:[Product] = [] 
        query = QSqlQuery()
        query.exec_(
            "SELECT name,description,rate,commentCount,w1,w2,w3,w4,w5,w6,w7,w8,w9,w10,price,finalprice,meanWeight,tolerance,insertedWeight,barcode,isOffer,isPlu,tax,qrCode,productType"
            "FROM product"
            "WHERE productType='weighted' or productType = 'counted' "
            )
        while query.next():
            p = Product()
            p.name = query.value(0)
            p.description = query.value(1)
            p.rate = query.value(2)
            p.commentCount = query.value(3)
            p.w1 = query.value(4)
            p.w2 = query.value(5)
            p.w3 = query.value(6)
            p.w4 = query.value(7)
            p.w5 = query.value(8)
            p.w6 = query.value(9)
            p.w7 = query.value(10)
            p.w8 = query.value(11)
            p.w9 = query.value(12)
            p.w10 = query.value(13)
            p.price = query.value(14)
            p.finalPrice = query.value(15)
            p.meanWeight = query.value(16)
            p.tolerance = query.value(17)
            p.insertedWeight = query.value(18)
            p.barcode = query.value(19)
            p.isOffer = query.value(20)
            p.isPlu = query.value(21)
            p.tax = query.value(22)
            p.QR = query.value(23)
            p.productType = query.value(24)
            res.append(p)
        return res











# def updateWeight(self, prod: Product, weight: int):
#         if prod.getInsertedWeight() == 0:
#             prod.setW1(weight)
#             prod.setAvgWeight(weight)
#             prod.setTolerance(int(max(8, int(weight * 0.1))))
#             prod.setInsertedWeight(1)
#             self.repository.updateProduductW1(prod.getBarcode(), weight, prod.getAvgWeight(), prod.getTolerance(),
#                                               prod.getInsertedWeight())
#         else:
#             if prod.getW1() == 0:
#                 new_avg_weight, new_tolerance, new_inserted_weight = prod.calNewWeightParameter(weight)
#                 prod.setW1(weight)
#                 prod.setAvgWeight(new_avg_weight)
#                 prod.setTolerance(new_tolerance)
#                 prod.setInsertedWeight(new_inserted_weight)
#                 self.repository.updateProduductW1(prod.getBarcode(), weight, new_avg_weight, new_tolerance,
#                                                   new_inserted_weight)
#             elif prod.getW2() == 0:
#                 new_avg_weight, new_tolerance, new_inserted_weight = prod.calNewWeightParameter(weight)
#                 prod.setW2(weight)
#                 prod.setAvgWeight(new_avg_weight)
#                 prod.setTolerance(new_tolerance)
#                 prod.setInsertedWeight(new_inserted_weight)
#                 self.repository.updateProduductW2(prod.getBarcode(), weight, new_avg_weight, new_tolerance,
#                                                   new_inserted_weight)
#             elif prod.getW3() == 0:
#                 new_avg_weight, new_tolerance, new_inserted_weight = prod.calNewWeightParameter(weight)
#                 prod.setW3(weight)
#                 prod.setAvgWeight(new_avg_weight)
#                 prod.setTolerance(new_tolerance)
#                 prod.setInsertedWeight(new_inserted_weight)
#                 self.repository.updateProduductW3(prod.getBarcode(), weight, new_avg_weight, new_tolerance,
#                                                   new_inserted_weight)
#             elif prod.getW4() == 0:
#                 new_avg_weight, new_tolerance, new_inserted_weight = prod.calNewWeightParameter(weight)
#                 prod.setW4(weight)
#                 prod.setAvgWeight(new_avg_weight)
#                 prod.setTolerance(new_tolerance)
#                 prod.setInsertedWeight(new_inserted_weight)
#                 self.repository.updateProduductW4(prod.getBarcode(), weight, new_avg_weight, new_tolerance,
#                                                   new_inserted_weight)
#             elif prod.getW5() == 0:
#                 new_avg_weight, new_tolerance, new_inserted_weight = prod.calNewWeightParameter(weight)
#                 prod.setW5(weight)
#                 prod.setAvgWeight(new_avg_weight)
#                 prod.setTolerance(new_tolerance)
#                 prod.setInsertedWeight(new_inserted_weight)
#                 self.repository.updateProduductW5(prod.getBarcode(), weight, new_avg_weight, new_tolerance,
#                                                   new_inserted_weight)
#             elif prod.getW6() == 0:
#                 new_avg_weight, new_tolerance, new_inserted_weight = prod.calNewWeightParameter(weight)
#                 prod.setW6(weight)
#                 prod.setAvgWeight(new_avg_weight)
#                 prod.setTolerance(new_tolerance)
#                 prod.setInsertedWeight(new_inserted_weight)
#                 self.repository.updateProduductW6(prod.getBarcode(), weight, new_avg_weight, new_tolerance,
#                                                   new_inserted_weight)
#             elif prod.getW7() == 0:
#                 new_avg_weight, new_tolerance, new_inserted_weight = prod.calNewWeightParameter(weight)
#                 prod.setW7(weight)
#                 prod.setAvgWeight(new_avg_weight)
#                 prod.setTolerance(new_tolerance)
#                 prod.setInsertedWeight(new_inserted_weight)
#                 self.repository.updateProduductW7(prod.getBarcode(), weight, new_avg_weight, new_tolerance,
#                                                   new_inserted_weight)
#             elif prod.getW8() == 0:
#                 new_avg_weight, new_tolerance, new_inserted_weight = prod.calNewWeightParameter(weight)
#                 prod.setW8(weight)
#                 prod.setAvgWeight(new_avg_weight)
#                 prod.setTolerance(new_tolerance)
#                 prod.setInsertedWeight(new_inserted_weight)
#                 self.repository.updateProduductW8(prod.getBarcode(), weight, new_avg_weight, new_tolerance,
#                                                   new_inserted_weight)
#             elif prod.getW9() == 0:
#                 new_avg_weight, new_tolerance, new_inserted_weight = prod.calNewWeightParameter(weight)
#                 prod.setW9(weight)
#                 prod.setAvgWeight(new_avg_weight)
#                 prod.setTolerance(new_tolerance)
#                 prod.setInsertedWeight(new_inserted_weight)
#                 self.repository.updateProduductW9(prod.getBarcode(), weight, new_avg_weight, new_tolerance,
#                                                   new_inserted_weight)
#             elif prod.getW10() == 0:
#                 new_avg_weight, new_tolerance, new_inserted_weight = prod.calNewWeightParameter(weight)
#                 prod.setW10(weight)
#                 prod.setAvgWeight(new_avg_weight)
#                 prod.setTolerance(new_tolerance)
#                 prod.setInsertedWeight(new_inserted_weight)
#                 self.repository.updateProduductW10(prod.getBarcode(), weight, new_avg_weight, new_tolerance,
#                                                    new_inserted_weight)
