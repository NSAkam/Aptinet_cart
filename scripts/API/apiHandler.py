from PySide2.QtCore import QUrl, QObject, Signal, Property, Slot, QByteArray, QJsonDocument, QJsonArray, QJsonValue, QEventLoop, QThread, QRunnable
from Services.dal import DAL
from Repositories.productRepository import ProductRepository
from Repositories.suggestionRepositories import SuggestionRepositories
from Repositories.userServerRepository import UserServerRepository
from Repositories.adminRepository import AdminRepository
from PySide2 import QtGui
import Services.restapi as restapi

import uuid
import json


class Apihandler(QObject):

    _tedadToDownload: int = 0
    _tedadDownloaded: int = 0

    _productRepository: ProductRepository
    _suggestionRepository: SuggestionRepositories
    _userServerRepository: UserServerRepository
    _adminRepository: AdminRepository

    url = "https://app.aptinet.com/"

    def __init__(self, dataAccessLayer: DAL):
        super().__init__()
        self.dal = dataAccessLayer
        self._productRepository = ProductRepository(self.dal)
        self._suggestionRepository = SuggestionRepositories(self.dal)
        self._userServerRepository = UserServerRepository(self.dal)
        self._adminRepository = AdminRepository(self.dal)

    appVersionRecievedSignal = Signal(str)
    dbVersionRecievedSignal = Signal(str)
    imagesVersionRecievedSignal = Signal(str)

    changedSignal = Signal()
    updateDownloadedFromServerValue = Signal(int)

    def get_tedadToDownload(self):
        return self._tedadToDownload

    def set_tedadToDownload(self, v: int):
        if (v == 0):
            self._tedadToDownload = 0
        else:
            self._tedadToDownload = self._tedadToDownload + v
        self.changedSignal.emit()

    tedadToDownload = Property(
        int, get_tedadToDownload, set_tedadToDownload, notify=changedSignal)

    def get_tedadDownloaded(self):
        return self._tedadDownloaded

    def set_tedadDownloaded(self, v: int):
        self._tedadDownloaded = v
        self.changedSignal.emit()
        self.updateDownloadedFromServerValue.emit(self._tedadDownloaded + 1)

    tedadDownloaded = Property(
        int, get_tedadDownloaded, set_tedadDownloaded, notify=changedSignal)

    @Slot()
    def startDownloadFromServer(self):
        self.set_tedadToDownload(0)
        self.set_tedadToDownload(0)

        self._productRepository.deleteAll()
        self.download_products()
        self._suggestionRepository.deleteAll()
        self.download_suggesstions()
        self._adminRepository.deleteAll()
        self.download_admins()
        self._userServerRepository.deleteAll()
        self.download_userServer()

    @Slot()
    def download_products(self):
        api = restapi.restAPI()
        api.recived.connect(self.all_productsRecived)
        api.Get(self.url + "api/products/GetProducs")

    @Slot(str)
    def all_productsRecived(self, v: str):
        print("all_productsRecived")
        lst = json.loads(v)
        self.set_tedadToDownload(len(lst))
        QtGui.QGuiApplication.processEvents()

        for i, x in enumerate(lst):
            name: str = lst[i]["name"]
            description: str = lst[i]["description"]
            rate: int = lst[i]["rate"]
            commentCount: int = lst[i]["commentCount"]
            w1: int = lst[i]["w1"]
            w2: int = lst[i]["w2"]
            w3: int = lst[i]["w3"]
            w4: int = lst[i]["w4"]
            w5: int = lst[i]["w5"]
            w6: int = lst[i]["w6"]
            w7: int = lst[i]["w7"]
            w8: int = lst[i]["w8"]
            w9: int = lst[i]["w9"]
            w10: int = lst[i]["w10"]
            price: float = lst[i]["price"]
            finalprice: float = lst[i]["finalprice"]
            meanWeight: int = lst[i]["meanWeight"]
            tolerance: int = lst[i]["tolerance"]
            insertedWeight: int = lst[i]["insertedWeighted"]
            barcode: str = lst[i]["barcode"]
            isOffer: int = lst[i]["isOffer"]
            isPlu: int = lst[i]["isPlu"]
            tax: int = lst[i]["tax"]
            qrCode: str = lst[i]["qrCode"]
            productType: str = lst[i]["productType"]

            res = self._productRepository.insertData(name, description, rate, commentCount, w1, w2, w3, w4, w5, w6, w7, w8, w9, w10,price, finalprice, meanWeight, tolerance, insertedWeight, barcode, isOffer, isPlu, tax, qrCode, productType)

        self.set_tedadDownloaded(self.get_tedadDownloaded() + 1)
        QtGui.QGuiApplication.processEvents()

    @Slot()
    def download_suggesstions(self):
        api = restapi.restAPI()
        api.recived.connect(self.all_suggesstionsRecived)
        api.Get(self.url + "api/products/GetSuggesstions")

    @Slot(str)
    def all_suggesstionsRecived(self, v: str):
        print("all_suggesstionsRecived")
        lst = json.loads(v)
        self.set_tedadToDownload(len(lst))
        QtGui.QGuiApplication.processEvents()

        for i, x in enumerate(lst):
            productBarcode: str = lst[i]["productBarcode"]
            sugProductBarcode: str = lst[i]["sugProductBarcode"]

            res = self._suggestionRepository.insertData(
                productBarcode, sugProductBarcode)
        self.set_tedadDownloaded(self.get_tedadDownloaded() + 1)
        QtGui.QGuiApplication.processEvents()

    @Slot()
    def download_admins(self):
        api = restapi.restAPI()
        api.recived.connect(self.all_adminsRecived)
        api.Get(self.url + "api/user/GetAdmins")

    @Slot(str)
    def all_adminsRecived(self, v: str):
        print("all_adminsRecived")
        lst = json.loads(v)
        self.set_tedadToDownload(len(lst))
        QtGui.QGuiApplication.processEvents()

        for i, x in enumerate(lst):
            productBarcode: str = lst[i]["barcode"]
            sugProductBarcode: str = lst[i]["name"]

            res = self._adminRepository.insertData(
                productBarcode, sugProductBarcode)
        self.set_tedadDownloaded(self.get_tedadDownloaded() + 1)
        QtGui.QGuiApplication.processEvents()

    @Slot()
    def download_userServer(self):
        api = restapi.restAPI()
        api.recived.connect(self.all_userServerRecived)
        api.Get(self.url + "api/user/GetUsers")

    @Slot(str)
    def all_userServerRecived(self, v: str):
        print("all_userServerRecived")

        lst = json.loads(v)
        self.set_tedadToDownload(len(lst))
        QtGui.QGuiApplication.processEvents()

        for i, x in enumerate(lst):
            res = self._userServerRepository.insertData(lst[i]["id"], lst[i]["loyalityBarcode"], lst[i]["name"], lst[i]
                                                        ["email"], lst[i]["phone"], lst[i]["offerPercentage"], lst[i]["offerLimitedPercentage"], lst[i]["offerMount"])
        self.set_tedadDownloaded(self.get_tedadDownloaded() + 1)
        QtGui.QGuiApplication.processEvents()

    @Slot()
    def get_appVersion(self):
        api = restapi.restAPI()
        api.recived.connect(self.appVersion_Recived)
        api.Get(self.url + "api/APP/GetAppVersion")

    @Slot(str)
    def appVersion_Recived(self, v: str):
        print("appVersion_Recived" + v)
        self.appVersionRecievedSignal.emit(v)

    @Slot()
    def get_dbVersion(self):
        api = restapi.restAPI()
        api.recived.connect(self.dbVersion_Recived)
        api.Get(self.url + "api/APP/GetDbVersion")

    @Slot(str)
    def dbVersion_Recived(self, v: str):
        self.dbVersionRecievedSignal.emit(v)

    @Slot()
    def get_imagesVersion(self):
        api = restapi.restAPI()
        api.recived.connect(self.imagesVersion_Recived)
        api.Get(self.url + "api/APP/GetImagesVersion")

    @Slot(str)
    def imagesVersion_Recived(self, v: str):
        self.imagesVersionRecievedSignal.emit(v)
