from PySide2.QtCore import QObject, Signal, Property,Slot,QUrl
from Services.dateTime import DateTime
from Services.scanner import ScannerWorker 
import os
import sys


class Logic(QObject): 
    _datetime : DateTime

    def __init__(self)->None:
        super().__init__()
        try:
            self._datetime = DateTime()
        except:
            print("\n can not Get dataTime")
        