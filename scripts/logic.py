from PySide2.QtCore import QObject, Signal, Property,Slot,QUrl
from Services.dateTime import DateTime
from Services.gpio import *
from Services.scanner import ScannerWorker 
import os
import sys


class Logic(QObject): 
    pass