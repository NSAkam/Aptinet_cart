import serial
from threading import Thread
from PySide2.QtCore import QObject, Signal, Property, QThread


class ScannerWorker(QThread):
    portConnected: bool = True

    def disconnect(self):
        self.portConnected = False
        self.ser.close()

    def __init__(self):
        self.ser = serial.Serial("/dev/ttyS0", baudrate=9600, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE,
                                 bytesize=serial.EIGHTBITS, timeout=1)
        QThread.__init__(self)

    @Signal
    def barcodeValueReaded(self):
        pass

    def run(self):
        while self.portConnected:
            self.readed_bytes = self.ser.read(32)
            self.barcodeValueReaded.emit()
        

    def disconnectSignals(self):
        self.IDbarcodeReaded.disconnect(self)
    
    def __del__(self):
        if (self.ser.isOpen()):
            self.ser.close()
