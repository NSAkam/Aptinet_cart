from PySide2.QtCore import QObject, Signal, Slot
from Services.scanner import ScannerWorker


class ScannerHelper(QObject):
    _scannerWorker: ScannerWorker
    _barcode: str
    _IDBarcode: str

    def __init__(self):
        super().__init__()

        self._scannerWorker = ScannerWorker()
        self._scannerWorker.barcodeValueReadSignal.connect(self.barcode_read)

    EAN13ReadSignal = Signal()
    QRReadSignal = Signal()
    IDBarcodeReadSignal = Signal()

    def get_barcode(self):
        return self._barcode

    def set_barcode(self, v: str):
        self._barcode = v

    @Slot()
    def barcode_read(self):
        if len(self._scannerWorker.get_readBytes()) == 15:
            self.barcode = self._scannerWorker.get_readBytes()[1:-1].decode('latin1')
            self.EAN13ReadSignal.emit()
        elif len(self._scannerWorker.get_readBytes()) == 22 or len(self._scannerWorker.get_readBytes()) == 12:
            self.ID_barcode = self._scannerWorker.get_readBytes()[1:-1].decode('latin1')
            self.IDBarcodeReadSignal.emit()
        # elif len(self._scannerWorker.readed_bytes) > 3:
        #     self.iranbarcode = self._scannerWorker.readed_bytes[1:-1].decode('latin1')
        #     self.Qr_Readed.emit()

    @Slot()
    def start(self):
        self._scannerWorker.start()
