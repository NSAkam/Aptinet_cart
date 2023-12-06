from PySide2.QtSql import QSqlQuery

from Services.dal import DAL
from Models.product import Product


class ProductRepository:

    dal: DAL

    def __init__(self, dataAccessLayer: DAL) -> None:
        self.dal = dataAccessLayer
        self.dal.Connect()

    def deleteAll(self):
        query = QSqlQuery()
        query.exec_("delete from product")

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

    def insertData(self, name: str, description: str, rate: int, commentCount: int, w1: int, w2: int, w3: int, w4: int, w5: int, w6: int, w7: int, w8: int, w9: int, w10: int, price: float, finalprice: float, meanWeight: int, tolerance: int, insertedWeight: int, barcode: str, isOffer: int, isPlu: int, tax: int, qrCode: str, productType: str):
        query = QSqlQuery()
        if (query.exec_("insert into product "
                        "(name,description,rate,commentCount,w1,w2,w3,w4,w5,w6,w7,w8,w9,w10,price,finalprice,meanWeight,tolerance,insertedWeight,barcode,isOffer,isPlu,tax,qrCode,productType) "
                        "values "
                        "('"+str(name)+"','"+str(description)+"','"+str(rate)+"','"+str(commentCount)+"','"+str(w1)+"','"+str(w2)+"','"+str(w3)+"','"+str(w4)+"','"+str(w5)+"','"+str(w6)+"','"+str(w7)+"','"+str(w8)+"','"+str(w9)+"','"+str(w10)+"','"+str(price)+"','"+str(finalprice)+"','"+str(meanWeight)+"','"+str(tolerance)+"','"+str(insertedWeight)+"','"+str(barcode)+"','"+str(isOffer)+"','"+str(isPlu)+"','"+str(tax)+"','"+str(qrCode)+"','"+str(productType)+"')")):
            return True
        else:
            return False

    def get_product(self, barcode):
        query = QSqlQuery()
        taxPercentage = 0
        quantifire = ""
        query.exec_("select quatifire,taxPercentage from Config LIMIT 1")
        while query.next:
            quantifire = query.value(0)
            taxPercentage =query.value(1)
        query.exec_(
            "SELECT name,description,rate,commentCount,w1,w2,w3,w4,w5,w6,w7,w8,w9,w10,price,finalprice,meanWeight,tolerance,insertedWeight,barcode,isOffer,isPlu,tax,qrCode,productType "
            "FROM product "
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
        res: [Product] = []
        query = QSqlQuery()
        query.exec_(
            "SELECT name,description,rate,commentCount,w1,w2,w3,w4,w5,w6,w7,w8,w9,w10,price,finalprice,meanWeight,tolerance,insertedWeight,barcode,isOffer,isPlu,tax,qrCode,productType "
            "FROM product "
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
        res: [Product] = []
        query = QSqlQuery()
        query.exec_(
            "SELECT name,description,rate,commentCount,w1,w2,w3,w4,w5,w6,w7,w8,w9,w10,price,finalprice,meanWeight,tolerance,insertedWeight,barcode,isOffer,isPlu,tax,qrCode,productType "
            "FROM product "
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

    def get_suggesstionProducts(self, productBarcode: str):
        res: [Product] = []
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
        res: [Product] = []
        query = QSqlQuery()
        query.exec_(
            "SELECT name,description,rate,commentCount,w1,w2,w3,w4,w5,w6,w7,w8,w9,w10,price,finalprice,meanWeight,tolerance,insertedWeight,barcode,isOffer,isPlu,tax,qrCode,productType "
            "FROM product "
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

    def updateWeight(self,w: int, barcode: str, weight: int, avg: int, tol: int, iw: int):
        query = QSqlQuery()
        if (query.exec_("update product set w"+str(w)+" = '"+str(weight)+"' ,insertedWeight= '"+str(iw)+"' , tolerance = '"+str(tol)+"' , meanWeight = '"+str(avg)+"' where barcode = '"+str(barcode)+"'")):
            return True
        else:
            return False

    def updateProduductWeight(self, prod: Product, weight: int):
        if prod.insertedWeight == 0:
            prod.set_w1(weight)
            prod.set_meanWeight(weight)
            prod.set_tolerance(int(max(8, int(weight * 0.1))))
            prod.set_insertedWeight(1)
            self.updateWeight(1, prod.barcode, weight, prod.meanWeight, prod.tolerance,
                                              prod.insertedWeight)
        else:
            if prod.get_w1() == 0:
                new_avg_weight, new_tolerance, new_inserted_weight = prod.call_newWeightParameter(
                    weight)
                prod.set_w1(weight)
                prod.set_meanWeight(new_avg_weight)
                prod.set_tolerance(new_tolerance)
                prod.set_insertedWeight(new_inserted_weight)
                self.updateWeight(1, prod.barcode, weight, prod.meanWeight, prod.tolerance,
                                              prod.insertedWeight)
            elif prod.get_w2() == 0:
                new_avg_weight, new_tolerance, new_inserted_weight = prod.call_newWeightParameter(
                    weight)
                prod.set_w2(weight)
                prod.set_meanWeight(new_avg_weight)
                prod.set_tolerance(new_tolerance)
                prod.set_insertedWeight(new_inserted_weight)
                self.updateWeight(2, prod.barcode, weight, prod.meanWeight, prod.tolerance,
                                              prod.insertedWeight)
            elif prod.get_w3() == 0:
                new_avg_weight, new_tolerance, new_inserted_weight = prod.call_newWeightParameter(
                    weight)
                prod.set_w3(weight)
                prod.set_meanWeight(new_avg_weight)
                prod.set_tolerance(new_tolerance)
                prod.set_insertedWeight(new_inserted_weight)
                self.updateWeight(3, prod.barcode, weight, prod.meanWeight, prod.tolerance,
                                              prod.insertedWeight)
            elif prod.get_w4() == 0:
                new_avg_weight, new_tolerance, new_inserted_weight = prod.call_newWeightParameter(
                    weight)
                prod.set_w4(weight)
                prod.set_meanWeight(new_avg_weight)
                prod.set_tolerance(new_tolerance)
                prod.set_insertedWeight(new_inserted_weight)
                self.updateWeight(4, prod.barcode, weight, prod.meanWeight, prod.tolerance,
                                              prod.insertedWeight)
            elif prod.get_w5() == 0:
                new_avg_weight, new_tolerance, new_inserted_weight = prod.call_newWeightParameter(
                    weight)
                prod.set_w5(weight)
                prod.set_meanWeight(new_avg_weight)
                prod.set_tolerance(new_tolerance)
                prod.set_insertedWeight(new_inserted_weight)
                self.updateWeight(5, prod.barcode, weight, prod.meanWeight, prod.tolerance,
                                              prod.insertedWeight)
            elif prod.get_w6() == 0:
                new_avg_weight, new_tolerance, new_inserted_weight = prod.call_newWeightParameter(
                    weight)
                prod.set_w6(weight)
                prod.set_meanWeight(new_avg_weight)
                prod.set_tolerance(new_tolerance)
                prod.set_insertedWeight(new_inserted_weight)
                self.updateWeight(6, prod.barcode, weight, prod.meanWeight, prod.tolerance,
                                              prod.insertedWeight)
            elif prod.get_w7() == 0:
                new_avg_weight, new_tolerance, new_inserted_weight = prod.call_newWeightParameter(
                    weight)
                prod.set_w7(weight)
                prod.set_meanWeight(new_avg_weight)
                prod.set_tolerance(new_tolerance)
                prod.set_insertedWeight(new_inserted_weight)
                self.updateWeight(7, prod.barcode, weight, prod.meanWeight, prod.tolerance,
                                              prod.insertedWeight)
            elif prod.get_w8() == 0:
                new_avg_weight, new_tolerance, new_inserted_weight = prod.call_newWeightParameter(
                    weight)
                prod.set_w8(weight)
                prod.set_meanWeight(new_avg_weight)
                prod.set_tolerance(new_tolerance)
                prod.set_insertedWeight(new_inserted_weight)
                self.updateWeight(8, prod.barcode, weight, prod.meanWeight, prod.tolerance,
                                              prod.insertedWeight)
            elif prod.get_w9() == 0:
                new_avg_weight, new_tolerance, new_inserted_weight = prod.call_newWeightParameter(
                    weight)
                prod.set_w9(weight)
                prod.set_meanWeight(new_avg_weight)
                prod.set_tolerance(new_tolerance)
                prod.set_insertedWeight(new_inserted_weight)
                self.updateWeight(9, prod.barcode, weight, prod.meanWeight, prod.tolerance,
                                              prod.insertedWeight)
            elif prod.get_w10() == 0:
                new_avg_weight, new_tolerance, new_inserted_weight = prod.call_newWeightParameter(
                    weight)
                prod.set_w10(weight)
                prod.set_meanWeight(new_avg_weight)
                prod.set_tolerance(new_tolerance)
                prod.set_insertedWeight(new_inserted_weight)
                self.updateWeight(10, prod.barcode, weight, prod.meanWeight, prod.tolerance,
                                              prod.insertedWeight)
