from PySide2 import QtCore
from PySide2.QtCore import QObject, Signal, Property
from PySide2.QtSql import QSqlDatabase, QSqlQuery, QSqlRecord, QSqlTableModel
from Models.product import Product


class DAL():

    def __init__(self):
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("/home/kast/KAST.db")
        self.CreateTables()
        super().__init__()

    def Connect(self):
        """
        Connect to local DB
        """
        if (self.db.isOpen() == False):
            if (self.db.open() == False):
                print("Error: connection with database failed")
            else:
                pass
        else:
            print("Database Is Connected")

    def Disconnect(self):
        """
        Disconnect from local DB
        """
        self.db.close()
        print("Database Disconnected")

    def CreateTables(self):
        self.Connect()
        query = QSqlQuery()
        if not query.exec_(
            "Create table IF NOT EXISTS admins ("
            "id	TEXT NOT NULL UNIQUE,"
            "name TEXT,"
            ")"
        ):
            print("Failed to create table admins")
        if not query.exec_(
            "CREATE TABLE IF NOT EXISTS product ("
            "barcode TEXT NOT NULL PRIMARY KEY,"
            "qr TEXT,"
            "name TEXT,"
            "price REAL,"
            "finalPrice REAL,"
            "description TEXT,"
            "rate INTEGER,"
            "commentCount INTEGER,"
            "w1 INTEGER,"
            "w2 INTEGER,"
            "w3 INTEGER,"
            "w4 INTEGER,"
            "w5 INTEGER,"
            "w6 INTEGER,"
            "w7 INTEGER,"
            "w8 INTEGER,"
            "w9 INTEGER,"
            "w10 INTEGER,"
            "meanWeight INTEGER,"
            "tolerance INTEGER,"
            "insertedWeight INTEGER,"
            "isOffer NUMERIC,"
            "isPlu NUMERIC,"
            "tax REAL,"
            "taxPrice INTEGER,"
            ")"
        ):
            print("Failed to create table product")
        if not query.exec_(
            "CREATE TABLE IF NOT EXISTS userFactore ("
            "id INTEGER NOT NULL PRIMARY KEY ,"
            "uid INTEGER,"
            "productBarcode TEXT,"
            "count INTEGER,"
            "price REAL,"
            "finalPrice REAL,"
            "tax REAL,"
            ")"
        ):
            print("Failed to create table userFactore.")
        if not query.exec_(
            "CREATE TABLE IF NOT EXISTS user ("
            "id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,"
            "regTime INTEGER,"
            "rate INTEGER,"
            "usId INTEGER,"
            "email TEXT"
            ")"
        ):
            print("Failed to create table user")
        if not query.exec_(
            "CREATE TABLE IF NOT EXISTS ServerUser ("
            "id INTEGER NOT NULL PRIMARY KEY,"
            "name TEXT,"
            "email TEXT,"
            "phone TEXT,"
            "offer REAL,"
            "code TEXT"
            ")"
        ):
            print("Faild to create table ServerUser")
        if not query.exec_(
            "CREATE TABLE IF NOT EXISTS Config ("
            "id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,"
            "storeId INTEGER,"
            "currency TEXT"
            ")"
        ):
            print("Failed to create TABLE Config")

        if not query.exec_(
            "CREATE TABLE IF NOT EXISTS loggs ("
            "id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,"
            "regTime INTEGER,"
            "action INTEGER,"
            "value TEXT,"
            "userId INTEGER"
            ")"
        ):
            print("Failed to create TABLE loggs.")
            
        if not query.exec_(
            "CREATE TABLE IF NOT EXISTS suggestion ("
            "id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,"
            "pBarcode TEXT,"
            "psBarcode TEXT"
            ")"
        ):
            print("Failed to create TABLE suggestion.")

