from PySide2.QtCore import QObject, Signal, Slot
from Services.scanner import ScannerWorker


class ScannerHelper(QObject):
    _scannerWorker: ScannerWorker
    _barcode: str
    _IDBarcode: str
    _loyaltyCardBarcode: str

    _outOfLogic: bool = False

    ### Setting ###################
    _productBarcodeLength: int = 13
    _IDBarcodeLength: int = 20
    _LoyaltyCardBarcodeLength: int = 16

    def __init__(self):
        super().__init__()
        self._scannerWorker = ScannerWorker()
        self._scannerWorker.barcodeValueReadSignal.connect(self.barcode_read)
        self.start()
        self._barcode = ""


    EAN13ReadSignal = Signal()
    QRReadSignal = Signal()
    IDBarcodeReadSignal = Signal()
    loyaltyCardBarcodeReadSignal = Signal()
    goToSettingSignal = Signal()

    def get_barcode(self):
        return self._barcode

    def set_barcode(self, v: str):
        self._barcode = v

    def get_IDBarcode(self):
        return self._IDBarcode

    def set_IDBarcode(self, val: str):
        self._IDBarcode = val

    def get_loyaltyCardBarcode(self):
        return self._loyaltyCardBarcode

    def set_loyaltyCardBarcode(self, v: str):
        self._loyaltyCardBarcode = v

    def get_productBarcodeLength(self):
        return self._productBarcodeLength

    @Slot()
    def barcode_read(self):
        productBarcodeLength = self._productBarcodeLength + self._scannerWorker.get_extraCharacter()
        IDBarcodeLength = self._IDBarcodeLength + self._scannerWorker.get_extraCharacter()
        LoyaltyCardBarcodeLength = self._LoyaltyCardBarcodeLength + self._scannerWorker.get_extraCharacter()

        if len(self._scannerWorker.get_readBytes()) == productBarcodeLength:
            self._barcode = self._scannerWorker.get_readBytes()[1:-1].decode('latin1')
            self.EAN13ReadSignal.emit()
        elif len(self._scannerWorker.get_readBytes()) == IDBarcodeLength:
            self._IDBarcode = self._scannerWorker.get_readBytes()[1:-1].decode('latin1')
            self.IDBarcodeReadSignal.emit()
            # if self._outOfLogic:
            #     self.goToSettingSignal.emit()
            # else:
            #     self.IDBarcodeReadSignal()
        elif len(self._scannerWorker.get_readBytes()) == LoyaltyCardBarcodeLength:
            self._loyaltyCardBarcode = self._scannerWorker.get_readBytes()[1:-1].decode('latin1')
            self.loyaltyCardBarcodeReadSignal.emit()



        # elif len(self._scannerWorker.readed_bytes) > 3:
        #     self.iranbarcode = self._scannerWorker.readed_bytes[1:-1].decode('latin1')
        #     self.Qr_Readed.emit()

    def go_outOfLogic(self):
        self._outOfLogic = True

    def start(self):
        self._scannerWorker.start()

    def stop(self):
        self._scannerWorker.stop()

