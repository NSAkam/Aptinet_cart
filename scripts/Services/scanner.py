import serial
from PySide2.QtCore import Signal, QThread


class ScannerWorker(QThread):
    _portConnected: bool = True
    _readBytes = None

    def __init__(self):
        self._ser = serial.Serial("/dev/ttyS0", baudrate=9600, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE,
                                  bytesize=serial.EIGHTBITS, timeout=1)
        QThread.__init__(self)

    barcodeValueReadSignal = Signal()

    def get_readBytes(self):
        return self._readBytes

    # def set_readBytes(self, v):
    #     self._readBytes = v

    # def get_portConnected(self):
    #     return self._portConnected

    def set_portConnected(self, v: bool):
        self._portConnected = v

    def run(self):
        while self._portConnected:
            self._readBytes = self.ser.read(32)
            self.barcodeValueReadSignal.emit()

    def __del__(self):
        if self._ser.isOpen():
            self._ser.close()
