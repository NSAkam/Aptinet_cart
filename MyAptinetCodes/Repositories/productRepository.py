# TODO: List<Product> / Get_Offer_List() , Product / Get_Product(Barcode), List<Product>/ Get_offer(barcode),
#  void/ Insert_into_factor_list(barcode/quantity)
from Services.dal import DAL
from Models.product import Product
from Models.suggestion import Suggestion
from PySide2.QtSql import QSqlQuery
from uuid import uuid1


class ProductRepository():

    def __init__(self, dal: DAL):
        self.dal = dal
        self.dal.Connect()
        # print("Connection to database has been successful")

    def InsertNewRow(self, barcode , name, price, finalprice, description):
        query = QSqlQuery()
        # query.exec_("INSERT INTO product(barcode, name, price, final_price, description) "
        #             "VALUES ('"+ barcode +"','"+ name +"', '"+ price +"','"+ finalprice +"', '"+ description +"')")
        query.prepare("INSERT INTO product(barcode, name, price, finalprice, description) "
                    "VALUES (?,?,?,?,?)")
        query.bindValue(0, barcode)
        query.bindValue(1, name)
        query.bindValue(2, price)
        query.bindValue(3, finalprice)
        query.bindValue(4, description)
        query.exec_()
        print("A new row has been inserted")


    def getProduct(self, barcode):
        """
        This function returns the specifications of a product with a special Barcode.
        :param barcode: Barcode of the product
        :return: an instance of Product()
        """
        try:
            query = QSqlQuery()

            if query.exec_("SELECT qr, name, price, finalprice, description, rate, commentcount, w1, w2, w3,"
                           " w4, w5, w6, w7, w8, w9, w10, meanweight, tolerance, isoffer, isplu,"
                           " tax, taxPrice, insertedweight FROM product WHERE barcode = '"+barcode+"'"):
                while query.next():
                    product = Product()
                    product.setQR(query.value(0))
                    product.setName(query.value(1))
                    product.setPrice(query.value(2))
                    product.setFinalprice(query.value(3))
                    product.setDescription(query.value(4))
                    product.setRate(query.value(5))
                    product.setCommentCount(query.value(6))
                    product.setW1(query.value(7))
                    product.setW2(query.value(8))
                    product.setW3(query.value(9))
                    product.setW4(query.value(10))
                    product.setW5(query.value(11))
                    product.setW6(query.value(12))
                    product.setW7(query.value(13))
                    product.setW8(query.value(14))
                    product.setW9(query.value(15))
                    product.setW10(query.value(16))
                    product.setMeanweight(query.value(17))
                    product.setTolerance(query.value(18))
                    product.setIsOffer(query.value(19))
                    product.setIsPLU(query.value(20))
                    product.setTax(query.value(21))
                    product.setTaxPrice(query.value(22))
                    product.setInsertedweight(query.value(23))
                return product
            else:
                print("SQL Error", query.lastError().text())
        except Exception as e:
            print("An exception has been occurred while trying to get data of this product", e)


    def testSelect(self, barcode="124"):
        query = QSqlQuery()
        if query.exec_("SELECT insertedweight FROM product WHERE barcode = '" + barcode + "'"):
            while query.next():
                print("select inserted weights...")
                print(query.value(0))
        else:
            print("Error for inserted weight!\n")
            print(query.lastError().text())

    def deleteProductTblRows(self):
        """
        This functions deleted all values in products table
        :return:
        """
        query = QSqlQuery()
        try:
            if query.exec_("DELETE From product"):
                return True
            else:
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
            if query.exec_("SELECT * FROM product WHERE barcode = '"+barcode+"'"):
                query.exec_("DELETE From product WHERE barcode = '"+barcode+"'")
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

            # Check if the product already exists in the table
            if query.exec_("SELECT barcode FROM product WHERE barcode = '" + barcode + "'"):
                if query.next():
                    # Barcode already exists, update the existing record
                    if query.exec_("UPDATE product SET meanweight = '" + str(meanweight) + "', tolerance = '"
                                    + str(tolerance) + "', insertedweight = '" + str(insertedweight)
                                    + "' WHERE barcode = '" + barcode + "'"):
                        print("The weight features have been updated successfully!")
                        return True
                    else:
                        print(query.lastError().text())
                        return False
                else:
                    # Barcode does not exist, insert a new record
                    if query.exec_("INSERT INTO product (barcode, meanweight, tolerance, insertedweight) VALUES ('" +
                                   barcode + "', '" + str(meanweight) + "', '" + str(tolerance) + "', '" +
                                   str(insertedweight) + "')"):
                        print("The weight features have been inserted successfully!")
                        return True
                    else:
                        print(query.lastError().text())
                        return False
            else:
                print(query.lastError().text())
                return False

        except Exception as e:
            print(str(e))
            return False
    #     try:
    #         query = QSqlQuery()
    #         if query.exec_(
    #             "INSERT INTO product (mean_weight, tolerance, inserted_weight) "
    #             "VALUES ('"+str(meanweight)+"', '"+ str(tolerance) +"', '"+ str(insertedweight) +"') "
    #             "WHERE (SELECT 1 FROM product WHERE barcode = '"+ barcode +"') "):
    #             query.exec_("UPDATE product SET mean_weight='" + str(meanweight) + "', tolerance = '" + str(tolerance) + "',"
    #                             " inserted_weight = '" + str(insertedweight) + "' WHERE barcode='" + str(barcode) + "'")
    #             print("The weight features have been updated successfully!")
    #             return True
    #         else:
    #             print(query.lastError().text())
    #             return False
    #     except Exception as e:
    #         print("An exception has occurred while trying to update weight features. The error is:\n", e)
    #
    # def updateW(self, barcode, w_index, w):
    #     try:
    #         query = QSqlQuery()
    #         weight_column_name = "w" + str(w_index)
    #         if query.exec_(
    #             "INSERT INTO product (barcode,'" + weight_column_name + "') VALUES ('"+barcode+"', '"+ w +"') "
    #             "WHERE (SELECT 1 FROM products WHERE barcode = '"+barcode+"') "):
    #
    #             query.exec_("UPDATE products SET '" + weight_column_name + "' = '" + w + "' "
    #                 "WHERE barcode='" + barcode + "'")
    #             return True
    #         else:
    #             return False
    #     except Exception as e:
    #         print("An exception has occurred while trying to get data of this product", e)

    def updateProduct(self, barcode, name, price, finalprice, isOffer, isPLU):
        try:
            query = QSqlQuery()

            # Check if the row already exists
            select_query = "SELECT 1 FROM product WHERE barcode = '" + barcode + "'"
            if query.exec_(select_query) and query.next():
                # Row exists, perform an UPDATE
                update_query = "UPDATE product SET name='" + str(name) + "', price = '" + str(
                    price) + "', finalprice = '" + str(finalprice) + "', isoffer = '" + str(
                    isOffer) + "', isplu = '" + str(isPLU) + "' WHERE barcode='" + barcode + "'"
                if query.exec_(update_query):
                    return True
            else:
                # Row does not exist, perform an INSERT
                insert_query = "INSERT INTO product (barcode, name, price, finalprice, isoffer, isplu) VALUES ('" + str(
                    barcode) + "','" + str(name) + "', '" + str(price) + "', '" + str(finalprice) + "', '" + str(
                    isOffer) + "', '" + isPLU + "')"
                if query.exec_(insert_query):
                    return True

            print(query.lastError().text())
            return False
        except Exception as e:
            print("SQL error:", query.lastError().text())
            print("An exception has occurred while trying to update data of this product. The error is \n", e)

    # def updateProduct(self, barcode, name, price, finalprice, isOffer, isPLU):
    #     try:
    #         query = QSqlQuery()
    #         if query.exec_(
    #             "INSERT INTO product (barcode, name, price, final_price, is_offer, is_plu) "
    #             "VALUES ('"+ str(barcode) +"','"+ str(name) +"', '"+ str(price) +"', '"
    #              + str(finalprice)+"', '"+ str(isOffer)+"', '"+isPLU+"' "
    #              "WHERE (SELECT 1 FROM product WHERE barcode = '"+barcode+"') "):
    #
    #             query.exec_("UPDATE product SET name='" + str(name) + "', price = '" + str(price) + "', final_price = '" +
    #                 str(finalprice) + "', is_offer = '" + str(isOffer) + "', is_plu = '"+ str(isPLU)
    #                 +"' WHERE barcode='" + barcode + "'")
    #             return True
    #         else:
    #             print(query.lastError().text())
    #             return False
    #     except Exception as e:
    #         print("SQL error:", query.lastError().text())
    #         print("An exception has occurred while trying to update data of this product. The error is \n", e)

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
            products_list = []
            query = QSqlQuery()
            if query.exec_("SELECT barcode, name, description, price, finalprice, meanweight FROM "
                           "product WHERE isoffer = 'TRUE' "):
                while query.next():
                    product = Product()
                    product.setBarcode(query.value(0))
                    product.setName(query.value(1))
                    product.setDescription(query.value(2))
                    product.setPrice(query.value(3))
                    product.setFinalprice(query.value(4))
                    product.setMeanweight(query.value(5))
                    products_list.append(product)
                return products_list
            else:
                print("Error in Get Offer List", query.lastError().text())
                return False
        except Exception as e:
            print("Error in Get Offer List", query.lastError().text())
            print("An exception has been occurred while trying to get data for Offer lists", e)

    def getSuggestionsOfProduct(self, barcode):
        """
        This function returns the offers related to a special product which is identified by barcode.
        :param barcode: the barcode of the product
        :return: a list of instances of products
        """
        try:
            products_list = []
            suggestions_list = []
            query = QSqlQuery()
            if query.exec_("SELECT DISTINCT s.ps_barcode, p.barcode, p.qr, p.name, p.description, p.price, "
                           "p.finalprice, p.tax, p.taxPrice FROM product as p INNER JOIN suggestion as s ON "
                           "s.ps_barcode = p.barcode WHERE s.p_barcode =  '"+ barcode +"'"):
                while query.next():
                    suggestion = Suggestion()
                    product = Product()
                    suggestion.setPsBarcode(query.value(0))
                    product.setBarcode(query.value(1))
                    product.setQR(query.value(2))
                    product.setName(query.value(3))
                    product.setDescription(query.value(4))
                    product.setPrice(query.value(5))
                    product.setFinalprice(query.value(6))
                    product.setTax(query.value(7))
                    product.setTaxPrice(query.value(8))
                    suggestion.setPBarcode(barcode)
                    products_list.append(product)
                    suggestions_list.append(suggestion)
                return products_list, suggestions_list
            else:
                print("SQL Error:", query.lastError().text())
                return False
        except Exception as e:
            print("An exception has been occurred while trying to get data of this product", e)

    # def getSuggestionsOfProduct(self, barcode):
    #     """
    #     This function returns the offers related to a special product which is identified by barcode.
    #     :param barcode: the barcode of the product
    #     :return: a list of instances of products
    #     """
    #     try:
    #         product = Product()
    #         products_list=[]
    #         query = QSqlQuery()
    #         if query.exec_("SELECT name, description, price, final_price FROM product INNER JOIN suggestions "
    #                     "ON product.barcode = Suggestions.p_barcode"):
    #             while query.next():
    #                 product.setName(query.value(0))
    #                 product.setDescription(query.value(1))
    #                 product.setPrice(query.value(2))
    #                 product.setFinalprice(query.value(3))
    #                 products_list.append(product)
    #             return products_list
    #         else:
    #             return False
    #     except Exception as e:
    #         print("An exception has been occurred while trying to get data of this product", e)

    def insertIntoFactor(self, barcode):
        try:
            query = QSqlQuery()
            query.exec_("SELECT COUNT(count) FROM userFactor WHERE productbarcode = '"+barcode+"' ")
            # query.exec_("SELECT COUNT(count) FROM userFactor")
            while query.next():
                result = query.value(0)
                if result > 0:
                    # If the barcode exists, update the quantity by adding 1
                    query.prepare("UPDATE userFactor SET count = count + 1 WHERE productbarcode = '"+ barcode +"' ")
                    if query.exec_():
                        print("One point is added to the quantity of product with barcode: ", barcode)
                    else:
                        print("Error occurred during the update:", query.lastError().text())
                else:
                    # If the barcode doesn't exist, insert a new row with quantity = 1
                    query.prepare("INSERT INTO userFactor (productbarcode, count) VALUES (?, ?)")
                    query.bindValue(0, barcode)
                    query.bindValue(1, str(1))
                    if query.exec_():
                        print(f"A new product with barcode {barcode} has been added with quantity 1")
                    else:
                        print("Error occurred during adding the product:", query.lastError().text())

        except Exception as e:
            print("An exception has been occurred while trying to insert a product to factor", e)


    # def resetFactorList(self, id):
    #     try:
    #         query = QSqlQuery()
    #         if query.exec_("SELECT * FROM userFactor WHERE id = '"+ id +"' "):
    #             if query.exec_("DELETE FROM userFactor WHERE id = '"+ id +"' "):
    #                 return True
    #             else:
    #                 print("An error occured while trying to delete factor", query.lastError().text())
    #                 return False
    #         else:
    #             print("There is no factor with id: ", id)
    #
    #     except Exception as e:
    #         print("An exception has been occurred while trying to get data of this product", e)

    def getUserbyEmail(self, email):
        try:
            query = QSqlQuery()
            if query.exec_("SELECT FROM user WHERE email= '"+ email +"' "):
                name, phone = query.exec_("SELECT name, phone FROM user WHERE email='"+email+"' ")
                return name, phone
            else:
                return False
        except Exception as e:
            print("An exception has been occurred while trying to get data of this product", e)

    def registerUser(self, name, phone, email):
        try:
            query = QSqlQuery()
            if query.exec_("SELECT FROM user WHERE email = '" + email +"' "):
                print(f"A user with email {email} exists!")
            else:
                query.exec_("INSERT INTO user(guid, name, email, phone) VALUES "
                            "('"+ str(uuid1()) +"', '"+ name +"', '"+ email +"'), '"+ phone +"' ")
                print(f"User {name} with email {email} and phone {phone} ahas been succefully added!")

        except Exception as e:
            print("An exception has been occurred while trying to get data of this product", e)


# dal = DAL()
# pr = ProductRepository()
# print(pr.getProduct('123'))








0


