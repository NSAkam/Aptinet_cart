import os
import sys
import time
from threading import Thread
from PySide2.QtCore import QObject, Signal, Property, Slot
from Models.product import Product
from Models.productModel import ProductModel
from Services.dateTime import DateTime
from Services.weightsensor import WeightSensorWorker
from Services.dal import DAL
from Helpers.scannerHelper import ScannerHelper


class ShopPage(QObject):
    ### Models #######################

    _factorList : ProductModel
    _sugggestedProducts : ProductModel
    _offersProducts : ProductModel
    _newProduct:Product

    _datetime : DateTime
    _scanner:ScannerHelper
    _weightsensor : WeightSensorWorker

    ### Properties ###################
    _countDownTimer:int = -60
    
    def __init__(self,datetime :DateTime , scanner:ScannerHelper):
        super().__init__()
        dal = DAL()
        self._datetime = datetime
        #### Barcode Scanner Sensor ###############################
        self._scanner = scanner
        self._scanner.EAN13_Readed.connect(self.barcodeReaded)
        ### WeightSensot ##########################################
        self._weighsensor = WeightSensorWorker()
        self._weighsensor.basketweight_changed.connect(self.basketWeightChanged)
        self._weighsensor.startWeightchanged.connect(self.startShoppingProcess)
        self._weighsensor.start()
        #### Models ###############################################
        self._factorList = ProductModel(dal)
        self._sugggestedProducts = ProductModel(dal)
        self._offersProducts = ProductModel(dal)

        #### Insert Timer Thread ##################################
        self._canTimerTick = True
        self._timerThread = Thread(target=self.timerSlot)
        self._timerThread.start()


    @Slot()
    def barcodeReaded(self):
        pass

    @Slot()
    def basketWeightChanged(self, val2: int, val1: int):
        pass

    @Slot()
    def startShoppingProcess(self, val):
        self._startProcess = True
    
    @Slot()
    def timerSlot(self):
        pass
