from PySide2.QtCore import QUrl, QObject, Signal, Property, Slot, QByteArray, QJsonDocument, QJsonArray, QJsonValue, QEventLoop, QThread, QRunnable
from Services.dal import DAL
from Repositories.productRepository import ProductRepository
import uuid
import json


class Apihandler(QObject):
    def __init__(self, dataAccessLayer: DAL):
        super().__init__()
        self.dal = dataAccessLayer
        self._productRepository = ProductRepository(self.dal)