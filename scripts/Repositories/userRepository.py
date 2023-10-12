from Services.dal import DAL
from PySide2.QtSql import QSqlQuery
from Models.user import User



class UserRepository():
    
    dal:DAL
    def __init__(self,dataAccessLayer:DAL) -> None:
        self.dal = dataAccessLayer
        self.dal.Connect()

    def createUser(self,regdate:str,regtime:str)->int:
        """
        یک یوزر در دیتابیس با تاریخ و ساعت میسازد
        exceprion: if retruen -1 we have error
        return userID if -1 we
        """
        query = QSqlQuery()
        if query.exec_("INSERT into user (Regdate,RegTime) values ('"+regdate+"','"+regtime+"')"):
            insertedUserID = 0
            query.exec_("select max(id) from user")
            while query.next():
                insertedUserID = query.value(0)
            return insertedUserID
        else:
            return -1

    def newChangeWeight(self,regtime:str,chagedweight:int,userID:int):
        """
        زمانی که کاربر وزنی در سبد را کم یا زیاد کرده لاگ گرفته میشود

        return bool
        """
        query = QSqlQuery()
        if query.exec_("insert into userLog (weightchanged,uid,RegTime) VALUES ('"+str(chagedweight)+"','"+str(userID)+"','"+regtime+"')"):
            return True
        else:
            return False

    def newChangeState(self,regtime:str,state:int,userID:int):
        """
        زمانی که وضعیت سبد عوض میشود لاگ گرفته میشود
        
        return bool
        """
        query = QSqlQuery()
        if query.exec_("insert into userLog (state,uid,RegTime) VALUES ('"+str(state)+"','"+str(userID)+"','"+regtime+"')"):
            return True
        else:
            return False

    def newChangeBarcode(self,regtime:str,barcode:str,userID:int):
        """
        زمانی که بارکد محصولی را سبد اسکن میکند لاگ گرفته میشود
        
        return bool
        """
        query = QSqlQuery()
        if query.exec_("insert into userLog (barcode,uid,RegTime) VALUES ('"+barcode+"','"+str(userID)+"','"+str(regtime)+"')"):
            return True
        else:
            return False

    def execLog(self,userID:int):
        """
        Print All Logs

        return bool
        """
        query = QSqlQuery()
        query.exec_("SELECT weightchanged,barcode,state from userLog where uid = '"+str(userID)+"'")
        while query.next():
            print("|" + str(query.value(0)) + "|" + str(query.value(1)) + "|" + str(query.value(2)))

    def clearLog(self):
        """
        اظلاعات جدول لاگ ها خالی میوشد

        return bool
        """
        query = QSqlQuery()
        query.exec_("delete from userLog")
        
    def suspendedFactorCreated(self,userID:int,suspendedFactorID:str):
        """
        زمانی که فاکتور در سرور فروشگاه به صورت موقت ذخیره میشود آن شماره فاکتور جدول فاکتور موقت لاگ گرفته میشود
        return bool
        """
        query = QSqlQuery()
        if query.exec_("update user set suspendFactorID = '"+suspendedFactorID+"' where id = '"+str(userID)+"'"):
            return True
        else:
            return False

    def factorCreated(self,userID:int,factorID:str):
        """
        زمانی که فاکتور به صورت درست پرداخت میشود ای دی فاکتور پرداخت شده که در فروشگاه است به صورت لاگ ذخیره سازی میشود

        return bool
        """
        query = QSqlQuery()
        if query.exec_("update user set factorID = '"+str(factorID)+"' where id = '"+str(userID)+"'"):
            return True
        else:
            return False

    def rate(self,userID:int,rate:int):
        """
        لاگ نظر سنجی از کاربر را ذخیره سازی میشود
        
        return bool
        """
        query = QSqlQuery()
        if query.exec_("update user set Rate = '"+rate+"' where id = '"+str(userID)+"'"):
            return True
        else:
            return False

    def factorListCreate(self,userID:int,count:int,barcode:str,price:int,finalPrice:int):
        """
        اطلاعات محصول در فاکتور به صورت لاگ ذخیره میشود
        
        return bool
        """
        query = QSqlQuery()
        if query.exec_("INSERT into userFactor (uid,Barcode,Counter,Price,FinalPrice) values ('"+str(userID)+"','"+str(barcode)+"','"+str(count)+"','"+str(price)+"','"+str(finalPrice)+"')"):
            return True
        else:
            return False


    def newAdminLog(self,userID:str,adminBarcode:str,regtime:str):
        """
        ادمین ها زمانی که بارکد کارت خود را جلوی بارکد خوان میگیرند به صورت لاگ ذخیره میشود

        return bool
        """
        query = QSqlQuery()
        query.exec_("select count(id) from admins where id = '"+str(adminBarcode)+"'")
        query.next()
        if(int(query.value(0)) > 0):
            query.exec_("insert into userLog (adminBarcode,uid,RegTime) VALUES ('"+adminBarcode+"','"+str(userID)+"','"+str(regtime)+"')")
            return True
        else:
            return False

    def isSuperAdmin(self,userID:str):
        """
        بررسی می کند که آیا یوزی سوپرادمین است یا خیر
        
        return bool
        """
        query = QSqlQuery()
        query.exec_("select count(id) from admins where id = '"+str(userID)+"' and isSA = 1")
        query.next()
        if(int(query.value(0)) > 0):
            return True
        else:
            return False

    def peymentLog(self,userID:str,adminBarcode:str,regtime:str):
        """
        زمانی که یک ادمین برای کاربری به سوپاپ اطمینان مراجعه میکند لاگ ذخیره سازی میشود
        
        return bool
        """
        query = QSqlQuery()
        if query.exec_("insert into userLog (adminBarcode,uid,RegTime) VALUES ('"+adminBarcode+"','"+str(userID)+"','"+str(regtime)+"')"):
            return True
        else:
            return False

