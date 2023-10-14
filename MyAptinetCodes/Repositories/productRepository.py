# TODO: List<Product> / Get_Offer_List() , Product / Get_Product(Barcode), List<Product>/ Get_offer(barcode),
#  void/ Insert_into_factor_list(barcode/quantity)
from MyAptinetCodes.Services.dal import DAL
from MyAptinetCodes.Models.product import Product
from PySide2.QtSql import QSqlQuery
from uuid import uuid1


class ProductRepository:

    def __int__(self):
        self.dal = DAL()
        self.dal.Connect()


    def getProduct(self, barcode):
        """
        This function returns the specifications of a product with a special Barcode.
        :param barcode: Barcode of the product
        :return: an instance of Product()
        """
        try:
            product = Product()
            query = QSqlQuery()
            if query.exec_("SELECT name, description, price, finalprice, rate, CommentCount, meanweight, tolerance,"
            " insertedweights, isOffer, isPLU, tax, QR, storeID, w1, w2, w3, w4, w5, w6, w7, w8, w9, w10 FROM products "
            "WHERE Barcode = '"+barcode+"'"):
                while query.next():
                    product.setName(query.value(0))
                    product.setDescription(query.value(1))
                    product.setPrice(query.value(2))
                    product.setFinalprice(query.value(3))
                    product.setRate(query.value(4))
                    product.setCommentCount(query.value(5))
                    product.setMeanweight(query.value(6))
                    product.setTolerance(query.value(7))
                    product.setInsertedweight(query.value(8))
                return product
            else:
                return None
        except Exception as e:
            print("An exception has been occurred while trying to get data of this product", e)

    def deleteProductsTblRows(self):
        """
        This functions deleted all values in products table
        :return:
        """
        query = QSqlQuery()
        try:
            if query.exec_("DELETE From products"):
                return True
            else
                return False
        except Exception as e:
            print("An exception has been occurred while trying to delete all rows of products table", e)

    def deleteAnSpecificProduct(self, barcode):
        """
        This function checks if there is a row in table with Barcode = barcode
        if yes, it deletes that row
        :param barcode: the barcode of the product
        :return:
        """
        try:
            query = QSqlQuery()
            if query.exec_("SELECT * FROM products WHERE Barcode = '"+barcode+"'"):
                query.exec_("DELETE From products WHERE Barcode = '"+barcode+"'"")
                return True
            else:
                return False
        except Exception as e:
            print(f"An exception has been occurred while trying to delete a product with barcode: {barcode}", e)

    def updateWeightFeatures(self, barcode, meanweight, tolerance, insertedweight):
        """
        This function updates the weight features of the barcode.
        :param barcode:
        :param meanweight:
        :param tolerance:
        :param insertedweight:
        :param w_index:
        :param w:
        :return:
        """
        try:
            query = QSqlQuery()
            # weight_column_name = "w" + str(w_index)
            if query.exec_(
                "INSERT INTO products(barcode, meanweight, tolerance, insertedweight) "
                "VALUES ('"+barcode+"', '"+meanweight+"', '"+tolerance+"', '"+insertedweight+"') "
                "WHERE NOT EXISTS (SELECT 1 FROM products WHERE barcode = '"+barcode+"') "):

                    query.exec_("UPDATE products SET meanweight='" + meanweight + "', tolerance = '" + tolerance + "',"
                                " insertedweight = '" + insertedweight + "' WHERE Barcode='" + barcode + "'")
            else:
                pass
        except Exception as e:
            print("An exception has occurred while trying to get data of this product", e)

    def updateW(self, barcode, w_index, w):
        try:
            query = QSqlQuery()
            weight_column_name = "w" + str(w_index)
            if query.exec_(
                "INSERT INTO products(barcode,'" + weight_column_name + "') VALUES ('"+barcode+"', '"+ w +"') "
                "WHERE NOT EXISTS (SELECT 1 FROM products WHERE barcode = '"+barcode+"') "):

                    query.exec_("UPDATE products SET '" + weight_column_name + "' = '" + w + "' "
                    "WHERE Barcode='" + barcode + "'")
            else:
                pass
        except Exception as e:
            print("An exception has occurred while trying to get data of this product", e)


    def updateProducts(self, barcode, name, price, finalprice, isOffer, isPLU):
        try:
            query = QSqlQuery()
            if query.exec_(
                "INSERT INTO products (barcode, name, price, finalprice, isOffer, isPLU) "
                "VALUES ('"+barcode+"','"+name+"', '"+price+"', '"+finalprice+"', '"+isOffer+"', '"+isPLU+"'"
                " WHERE NOT EXISTS (SELECT 1 FROM products WHERE barcode = '"+barcode+"') "):

                    query.exec_("UPDATE products SET name='" + name + "', price = '" + price + "', finalprice = '" +
                    finalprice + "', isOffer = '" +isOffer+ "', isPLU = '"+isPLU+"' WHERE Barcode='" + barcode + "'")
            else:
                pass
        except Exception as e:
            print("An exception has occurred while trying to get data of this product", e)



    # def updateWeightFeatures(self, barcode, meanweight, tolerance, insertedweight, w_index: int, w):
    #     """
    #     This function update the weight features of the barcode.
    #     :param barcode:
    #     :param meanweight:
    #     :param tolerance:
    #     :param insertedweight:
    #     :return:
    #     """
    #     try:
    #         product = Product()
    #         query = QSqlQuery()
    #         if query.exec_("SELECT meanweight, tolerance, insertedweight FROM products WHERE Barcode = '"+barcode+"'"):
    #             query.exec_("UPDATE products SET meanweight='"+meanweight+"', tolerance = '"+tolerance+"',"
    #                        " insertedweight = '"+insertedweight+"' WHERE Barcode='"+barcode+"'")
    #
    #
    #             while query.next():
    #                 product.setName(query.value(0))
    #                 product.setDescription(query.value(1))
    #                 product.setPrice(query.value(2))
    #                 product.setFinalprice(query.value(3))
    #             return product
    #     except Exception as e:
    #         print("An exception has been occurred while trying to get data of this product", e)



    def getOfferList(self):
        """
        This function finds the products with isOffer=True.
        :return: An instance of product
        """
        try:
            product = Product()
            products_list = []
            query = QSqlQuery("SELECT Barcode, name, description, price, finalprice, meanweight FROM product WHERE isOffer = TRUE ")
            while query.next():
                product.setBarcode(query.value(0))
                product.setName(query.value(1))
                Product.setDescription(query.value(2))
                Product.setPrice(query.value(3))
                Product.setFinalprice(query.value(4))
                Product.setMeanweight(query.value(5))
                products_list.append(product)

            return products_list

        except Exception as e:
            print("An exception has been occurred while trying to get data for Offer lists", e)


    def getSuggestionsOfProduct(self, barcode):
        """
        This function returns the offers related to a special product which is identified by barcode.
        :param barcode: the barcode of the product
        :return: a list of instances of products
        """
        try:
            product = Product()
            products_list=[]
            query = QSqlQuery()
            query.exec_("SELECT name, description, price, finalprice FROM products INNER JOIN Suggestions "
                        "ON products.Barcode = Suggestions.P_Barcode")
            while query.next():
                product.setName(query.value(0))
                product.setDescription(query.value(1))
                product.setPrice(query.value(2))
                product.setFinalprice(query.value(3))
                products_list.append(product)
            return products_list
        except Exception as e:
            print("An exception has been occurred while trying to get data of this product", e)

    def insertIntoFactor(self, barcode, count):
        try:
            query = QSqlQuery()
            query.exec_("SELECT COUNT(*) FROM Factor_list WHERE barcode = '"+barcode+"' ")
            while query.next():
                result = query.value(0)
                if result > 0:
                    # If the barcode exists, update the quantity by adding 1
                    query.prepare("UPDATE Factor_list SET count = '"+count+"' + 1 WHERE barcode = '"+barcode+"'")
                else:
                    # If the barcode doesn't exist, insert a new row with quantity = 1
                    query.prepare("INSERT INTO Factor_list (barcode, count) VALUES (?, 1)")
                    query.addBindValue(barcode)
        except Exception as e:
            print("An exception has been occurred while trying to get data of this product", e)

    # def resetFactorList(self, id):
    #     try:
    #         query = QSqlQuery()
    #         query.exec_("SELECT COUNT(*) FROM Factor_list WHERE id = '"+ id +"' ")
    #         while query.next():
    #             result = query.value(0)
    #             if result > 0:
    #                 # If the barcode exists, update the quantity by adding 1
    #                 query.prepare("UPDATE Factor_list SET quantity = '"+quantity+"' + 1 WHERE barcode = '"+barcode+"'")
    #             else:
    #                 # If the barcode doesn't exist, insert a new row with quantity = 1
    #                 query.prepare("INSERT INTO Factor_list (barcode, quantity) VALUES (?, 1)")
    #                 query.addBindValue(barcode)
    #     except Exception as e:
    #         print("An exception has been occurred while trying to get data of this product", e)

    def getUserbyEmail(self, email):
        try:
            query = QSqlQuery()
            if query.exec_("SELECT FROM user WHERE email= '"+ email +"' "):
                name, phone = query.exec_("SELECT name, phone FROM user WHERE email='"+email+"' ")
                return name, phone
            else:
                query.exec_("INSERT INTO user(guid, name, email, phone) VALUES ")

        except Exception as e:
            print("An exception has been occurred while trying to get data of this product", e)

    def registerUser(self, name, phone, email):
        try:
            query = QSqlQuery()
            if query.exec_("SELECT FROM user WHERE email = '"+ email +"' "):
                print(f"A user with email {email} exists!")
            else:
                query.exec_("INSERT INTO user(guid, name, email, phone) VALUES ('"+ str(uuid1()) +"', '"+ name +"',"
                " '"+ email +"'), '"+ phone +"' ")
                print(f"User {name} with email {email} and phone {phone} ahas been succefully added!")

        except Exception as e:
            print("An exception has been occurred while trying to get data of this product", e)














0


