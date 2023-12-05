import serial
from PySide2.QtCore import Signal, QThread


class ScannerWorker(QThread):
    _portConnected: bool = True
    _readBytes = None
    _canReadBarcode: bool
    _extraCharacter: int = 2

    def __init__(self):
        QThread.__init__(self)
        self._ser = serial.Serial("/dev/ttyS0", baudrate=9600, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE,
                                  bytesize=serial.EIGHTBITS, timeout=1)
        self._canReadBarcode = True

    barcodeValueReadSignal = Signal()

    def get_readBytes(self):
        return self._readBytes

    def get_extraCharacter(self):
        return self._extraCharacter

    def run(self):
        while self._canReadBarcode:
            self._readBytes = self._ser.read(32)
            # self.barcodeValueReadSignal.emit()

    def stop(self):
        self._canReadBarcode = False

    def __del__(self):
        if self._ser.isOpen():
            self._ser.close()
