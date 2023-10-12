from Services.dal import DAL
from PySide2.QtSql import QSqlQuery
from Models.product import Product
import os


class ProductRepository():

    dal: DAL

    def __init__(self, dataAccessLayer: DAL) -> None:
        self.dal = dataAccessLayer
        self.dal.Connect()

    ### functions ####################################################

    def GetProducts(self, barcode):
        """
        اطلاعات یک محصول بخصوص را با استفاده از بارکد برمیگرداند

        :param p1: One Barcode Of Products
        :return: Informations OF Barcode From Local DB
        """
        query = QSqlQuery()

        query.exec_("select p.*,pf.w1,pf.w2,pf.w3,pf.w4,pf.w5,pf.w6,pf.w7,pf.w8,pf.w9,pf.w10,pf.mean,pf.tolerance,pf.InsertedWeight,pf.IranCode from Products as p LEFT join ProductsFeatures as pf on p.barcode = pf.barcode where p.barcode = '"+barcode+"'")
        p = Product()
        while query.next():
            p.setBarcode(query.value(0))
            p.setname(query.value(1))
            p.setprice(query.value(2))
            p.setfinalprice(query.value(3))
            p.setunitCount(query.value(4))
            p.setnotValid(query.value(5))
            p.setW1(query.value(6))
            p.setW2(query.value(7))
            p.setW3(query.value(8))
            p.setW4(query.value(9))
            p.setW5(query.value(10))
            p.setW6(query.value(11))
            p.setW7(query.value(12))
            p.setW8(query.value(13))
            p.setW9(query.value(14))
            p.setW10(query.value(15))
            p.setAvgWeight(query.value(16))
            p.setTolerance(query.value(17))
            p.setInsertedWeight(query.value(18))
            p.setIrancode(query.value(19))
        return p

    def GetProductBarcode(self, irancode) -> str:
        """
        بارکد محصول را از روی ایران کد پیدا کرده و برمیگرداند

        param1: irancode Of Product
        return: barcode Of Product
        """

        query = QSqlQuery()
        query.exec_(
            "select barcode from ProductsFeatures where IranCode = '" + irancode + "'")
        barcode: str = ""
        while query.next():
            barcode = query.value(0)
        return barcode

    def deleteAllProducts(self):
        """
        جدول محصولات را خالی میکند
        توجه شود که این جدول به جدول ویژگی های محصولات متصل است

        return: bool
        """
        query = QSqlQuery()
        if query.exec_("delete from Products"):
            return True

    def deleteAllProductsFeature(self):
        """
        جدول ویژگی های محصولات را خالی میکند 

        return: bool
        """
        query = QSqlQuery()
        if query.exec_("delete from ProductsFeatures"):
            return True

    def updateProductFeature(self, barcode: str, irancode: str, mean: int, tolerance: int, InsertedWeight: int) -> bool:
        """
        جدول ویژگی های محصول را بروز رسانی میکند

        return: bool
        """
        query = QSqlQuery()
        if query.exec_(
            "INSERT into ProductsFeatures (barcode,mean,tolerance,InsertedWeight) "
            "select '"+barcode+"','" +
                str(mean) + "','" + str(tolerance) +
            "','" + str(InsertedWeight) + "' "
                "WHERE NOT EXISTS(SELECT 1 FROM ProductsFeatures WHERE barcode = '"+barcode+"')"):
            if query.exec_("UPDATE ProductsFeatures set irancode ='"+str(irancode)+"',mean ='"+str(mean)+"',tolerance ='"+str(tolerance)+"',InsertedWeight ='"+str(InsertedWeight)+"' "
                           "where barcode = '"+barcode+"'"):
                return True
            else:
                return False
        else:
            return False

    def updatePrice(self, name: str, barcode: str, price: int, finalprice: int):
        """
        قیمت محصول را بروز رسانی میکند

        return: bool
        """
        query = QSqlQuery()
        if query.exec_(
            "INSERT into Products (name,barcode,Price,FinalPrice) "
            "select '"+name+"','" + barcode + "','" +
                str(price) + "','" + str(finalprice) + "' "
                "WHERE NOT EXISTS(SELECT 1 FROM Products WHERE barcode = '" + barcode + "')"):
            if query.exec_("UPDATE Products set name='"+name+"', Price ='"+str(price)+"', FinalPrice='"+str(finalprice)+"' "
                           "where barcode = '"+barcode+"'"):
                return True
            else:
                return False
        else:
            return False

    def updateProduductW1(self, barcode: str, w: int, avg: int, tol: int, iw: int):
        """
        وزن اول محصول را بروز رسانی میکند

        return: bool
        """
        query = QSqlQuery()
        if query.exec_(
            "INSERT into ProductsFeatures (barcode,w1,mean,tolerance,InsertedWeight) "
            "select '"+barcode+"','" +
                str(w)+"','" + str(avg) + "','" +
            str(tol) + "','" + str(iw) + "' "
                "WHERE NOT EXISTS(SELECT 1 FROM ProductsFeatures WHERE barcode = '"+barcode+"')"):
            if query.exec_("update ProductsFeatures set w1='" + str(w) + "', mean = '" + str(avg) + "', tolerance = '" + str(tol) + "', InsertedWeight = '" + str(iw) + "' where barcode ='" + barcode + "'"):
                return True
            else:
                return False
        else:
            return False

    def updateProduductW2(self, barcode: str, w: int, avg: int, tol: int, iw: int):
        """
        وزن دوم محصول را بروز رسانی میکند

        return: bool
        """
        query = QSqlQuery()
        if query.exec_(
            "INSERT into ProductsFeatures (barcode,w2,mean,tolerance,InsertedWeight) "
            "select '"+barcode+"','" +
                str(w)+"','" + str(avg) + "','" +
            str(tol) + "','" + str(iw) + "' "
                "WHERE NOT EXISTS(SELECT 1 FROM ProductsFeatures WHERE barcode = '"+barcode+"')"):
            if query.exec_("update ProductsFeatures set w2='" + str(w) + "', mean = '" + str(avg) + "', tolerance = '" + str(tol) + "', InsertedWeight = '" + str(iw) + "' where barcode ='" + barcode + "'"):
                return True
            else:
                return False
        else:
            return False

    def updateProduductW3(self, barcode: str, w: int, avg: int, tol: int, iw: int):
        """
        وزن سوم محصول را بروز رسانی میکند

        return: bool
        """
        query = QSqlQuery()
        if query.exec_(
            "INSERT into ProductsFeatures (barcode,w3,mean,tolerance,InsertedWeight) "
            "select '"+barcode+"','" +
                str(w)+"','" + str(avg) + "','" +
            str(tol) + "','" + str(iw) + "' "
                "WHERE NOT EXISTS(SELECT 1 FROM ProductsFeatures WHERE barcode = '"+barcode+"')"):
            if query.exec_("update ProductsFeatures set w3='" + str(w) + "', mean = '" + str(avg) + "', tolerance = '" + str(tol) + "', InsertedWeight = '" + str(iw) + "' where barcode ='" + barcode + "'"):
                return True
            else:
                return False
        else:
            return False

    def updateProduductW4(self, barcode: str, w: int, avg: int, tol: int, iw: int):
        """
        وزن چهارم محصول را بروز رسانی میکند

        return: bool
        """
        query = QSqlQuery()
        if query.exec_(
            "INSERT into ProductsFeatures (barcode,w4,mean,tolerance,InsertedWeight) "
            "select '"+barcode+"','" +
                str(w)+"','" + str(avg) + "','" +
            str(tol) + "','" + str(iw) + "' "
                "WHERE NOT EXISTS(SELECT 1 FROM ProductsFeatures WHERE barcode = '"+barcode+"')"):
            if query.exec_("update ProductsFeatures set w4='" + str(w) + "', mean = '" + str(avg) + "', tolerance = '" + str(tol) + "', InsertedWeight = '" + str(iw) + "' where barcode ='" + barcode + "'"):
                return True
            else:
                return False
        else:
            return False

    def updateProduductW5(self, barcode: str, w: int, avg: int, tol: int, iw: int):
        """
        وزن پنجم محصول را بروز رسانی میکند

        return: bool
        """
        query = QSqlQuery()
        if query.exec_(
            "INSERT into ProductsFeatures (barcode,w5,mean,tolerance,InsertedWeight) "
            "select '"+barcode+"','" +
                str(w)+"','" + str(avg) + "','" +
            str(tol) + "','" + str(iw) + "' "
                "WHERE NOT EXISTS(SELECT 1 FROM ProductsFeatures WHERE barcode = '"+barcode+"')"):
            if query.exec_("update ProductsFeatures set w5='" + str(w) + "', mean = '" + str(avg) + "', tolerance = '" + str(tol) + "', InsertedWeight = '" + str(iw) + "' where barcode ='" + barcode + "'"):
                return True
            else:
                return False
        else:
            return False

    def updateProduductW6(self, barcode: str, w: int, avg: int, tol: int, iw: int):
        """
        وزن ششم محصول را بروز رسانی میکند

        return: bool
        """
        query = QSqlQuery()
        if query.exec_(
            "INSERT into ProductsFeatures (barcode,w6,mean,tolerance,InsertedWeight) "
            "select '"+barcode+"','" +
                str(w)+"','" + str(avg) + "','" +
            str(tol) + "','" + str(iw) + "' "
                "WHERE NOT EXISTS(SELECT 1 FROM ProductsFeatures WHERE barcode = '"+barcode+"')"):
            if query.exec_("update ProductsFeatures set w6='" + str(w) + "', mean = '" + str(avg) + "', tolerance = '" + str(tol) + "', InsertedWeight = '" + str(iw) + "' where barcode ='" + barcode + "'"):
                return True
            else:
                return False
        else:
            return False

    def updateProduductW7(self, barcode: str, w: int, avg: int, tol: int, iw: int):
        """
        وزن هفتم محصول را بروز رسانی میکند

        return: bool
        """
        query = QSqlQuery()
        if query.exec_(
            "INSERT into ProductsFeatures (barcode,w7,mean,tolerance,InsertedWeight) "
            "select '"+barcode+"','" +
                str(w)+"','" + str(avg) + "','" +
            str(tol) + "','" + str(iw) + "' "
                "WHERE NOT EXISTS(SELECT 1 FROM ProductsFeatures WHERE barcode = '"+barcode+"')"):
            if query.exec_("update ProductsFeatures set w7='" + str(w) + "', mean = '" + str(avg) + "', tolerance = '" + str(tol) + "', InsertedWeight = '" + str(iw) + "' where barcode ='" + barcode + "'"):
                return True
            else:
                return False
        else:
            return False

    def updateProduductW8(self, barcode: str, w: int, avg: int, tol: int, iw: int):
        """
        وزن هشتم محصول را بروز رسانی میکند

        return: bool
        """
        query = QSqlQuery()
        if query.exec_(
            "INSERT into ProductsFeatures (barcode,w8,mean,tolerance,InsertedWeight) "
            "select '"+barcode+"','" +
                str(w)+"','" + str(avg) + "','" +
            str(tol) + "','" + str(iw) + "' "
                "WHERE NOT EXISTS(SELECT 1 FROM ProductsFeatures WHERE barcode = '"+barcode+"')"):
            if query.exec_("update ProductsFeatures set w8='" + str(w) + "', mean = '" + str(avg) + "', tolerance = '" + str(tol) + "', InsertedWeight = '" + str(iw) + "' where barcode ='" + barcode + "'"):
                return True
            else:
                return False
        else:
            return False

    def updateProduductW9(self, barcode: str, w: int, avg: int, tol: int, iw: int):
        """
        وزن نهم محصول را بروز رسانی میکند

        return: bool
        """
        query = QSqlQuery()
        if query.exec_(
            "INSERT into ProductsFeatures (barcode,w9,mean,tolerance,InsertedWeight) "
            "select '"+barcode+"','" +
                str(w)+"','" + str(avg) + "','" +
            str(tol) + "','" + str(iw) + "' "
                "WHERE NOT EXISTS(SELECT 1 FROM ProductsFeatures WHERE barcode = '"+barcode+"')"):
            if query.exec_("update ProductsFeatures set w9='" + str(w) + "', mean = '" + str(avg) + "', tolerance = '" + str(tol) + "', InsertedWeight = '" + str(iw) + "' where barcode ='" + barcode + "'"):
                return True
            else:
                return False
        else:
            return False

    def updateProduductW10(self, barcode: str, w: int, avg: int, tol: int, iw: int):
        """
        وزن دهم محصول را بروز رسانی میکند

        return: bool
        """
        query = QSqlQuery()
        if query.exec_(
            "INSERT into ProductsFeatures (barcode,w10,mean,tolerance,InsertedWeight) "
            "select '"+barcode+"','" +
                str(w)+"','" + str(avg) + "','" +
            str(tol) + "','" + str(iw) + "' "
                "WHERE NOT EXISTS(SELECT 1 FROM ProductsFeatures WHERE barcode = '"+barcode+"')"):
            if query.exec_("update ProductsFeatures set w10='" + str(w) + "', mean = '" + str(avg) + "', tolerance = '" + str(tol) + "', InsertedWeight = '" + str(iw) + "' where barcode ='" + barcode + "'"):
                return True
            else:
                return False
        else:
            return False

    def updateProductIranBarcode(self, barcode: str, v: str):
        """
        ایران بارکد محصول را بروز رسانی میکند

        param1: barcode of Product
        param2: irancode of Product
        return: bool
        """
        query = QSqlQuery()
        if query.exec_(
            "INSERT into ProductsFeatures (barcode,IranCode)"
            "select '"+barcode+"','"+v+"' "
                "WHERE NOT EXISTS(SELECT 1 FROM ProductsFeatures WHERE barcode = '"+barcode+"')"):
            if query.exec_("update ProductsFeatures set IranCode='"+v+"' where barcode ='" + barcode + "'"):
                return True
            else:
                return False
        else:
            return False

    def GetSpecialOffer(self):
        """
        محصولات دارای تخفیف ویژه را برمیگرداند

        return: [Product]
        """
        self.dal.Connect()
        query = QSqlQuery()
        query.exec_("select *,cast(FinalPrice as Real)/ cast(Price as real) from Products where barcode in ('6260403687541','6262032506736') and cast(FinalPrice as Real)/ cast(Price as real) != 1 order by cast(FinalPrice as Real)/ cast(Price as real) asc ")
        res: [Product] = []
        while query.next():
            p = Product()
            p.setBarcode(query.value(0))
            p.setname(query.value(1))
            p.setprice(query.value(2))
            p.setfinalprice(query.value(3))
            if (os.path.isfile("/home/kast/pics/" + str(query.value(0)) + ".png") == True):
                res.append(p)
                if (len(res) >= 12):
                    break
        return res

    def insertAllProductsAsJson(self, s: str):
        """
        یک جیسون را گرفته و در جدول محصولات ذخیره میکند
        به این صورت که اگر محصولی در دیتابیس بود آن را دست نمیزند
        
        return: bool
        """
        query = QSqlQuery()
        res = query.exec_("insert or IGNORE into Products"
                          "(name,barcode,Price,FinalPrice,UnitCount,NotValid)"
                          "select json_extract(value,'$.Name'),"
                          "cast(json_extract(value,'$.Barcode') as int),"
                          "cast(json_extract(value,'$.ConsumerPrice') as int),"
                          "cast(json_extract(value,'$.SalePrice') as int),"
                          "cast(json_extract(value,'$.UnitCount') as int),"
                          "cast(json_extract(value,'$.NotValid') as int) from json_each('"+s+"') where json_extract(value,'$.Barcode') !=''")
        if (res == False):
            print(query.lastError())
        return res

    def insertAllProductsFeaturesAsJson(self, s: str):
        """
        یک جیسون را گرفته و در جدول ویژگی محصولات ذخیره میکند
        به این صورت که اگر محصولی در دیتابیس بود آن را آپدیت میکند دست نمیزند
        
        return: bool
        """
        query = QSqlQuery()
        return query.exec_("insert or REPLACE into ProductsFeatures"
                           "(barcode,mean,tolerance,InsertedWeight,IranCode)"
                           "select cast(json_extract(value,'$.Barcode')as int),"
                           "json_extract(value,'$.mean'),"
                           "json_extract(value,'$.tolerance'),"
                           "json_extract(value,'$.InsertedWeight'),"
                           "json_extract(value,'$.Irancode') from json_each('"+s+"')")

    def deleteWeights(self):
        """
        تمام وزن های جدول ویژگی ها را خالی میکند

        return: bool
        """
        query = QSqlQuery()
        return query.exec_("update ProductsFeatures set w1='0',w2='0',w3='0',w4='0',w5='0',w6='0',w7='0',w8='0',w9='0',w10='0'")
