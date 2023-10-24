from PySide2.QtCore import QObject, Signal, Property, QThread,Slot
from Services.scanner import ScannerWorker

class ScannerHelper(QObject):
    _scannerWorker:ScannerWorker
    barcode:str

    def __init__(self):
        super().__init__()

        self._scannerWorker = ScannerWorker()
        self._scannerWorker.barcodeValueReaded.connect(self.barcodeReaded)

    @Signal
    def EAN13_Readed(self):
        pass
    
    @Signal
    def Qr_Readed(self):
        pass

    @Signal
    def IDbarcode_Readed(self):
        pass

    @Slot()
    def barcodeReaded(self):
        if len(self._scannerWorker.readed_bytes) == 15:
            self.barcode = self._scannerWorker.readed_bytes[1:-1].decode('latin1')
            self.EAN13_Readed.emit()
        # elif len(self._scannerWorker.readed_bytes) == 22 or len(self._scannerWorker.readed_bytes) == 12:
        #     self.IDbarcode = self._scannerWorker.readed_bytes[1:-1].decode('latin1')
        #     self.IDbarcodeReaded.emit()
        # elif len(self._scannerWorker.readed_bytes) > 3:
        #     self.iranbarcode = self._scannerWorker.readed_bytes[1:-1].decode('latin1')
        #     self.Qr_Readed.emit()

    @Slot()
    def start(self):
        self._scannerWorker.start()