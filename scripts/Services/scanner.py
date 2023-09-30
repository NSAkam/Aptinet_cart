import serial
from threading import Thread
from PySide2.QtCore import QObject, Signal, Property, QThread


class ScannerWorker(QThread):
    """
    َConnecting to the Serial port ttyS0 of Raspberry Pi and Reading data (Barcode) from it.

    ...

    Attributes
    ----------
    portConnected: bool
        A parameter to identify the serial port is connected or not.
    out_of_logic: bool
        something..

    Methods
    -------
    disconnect
        Sets portConnected attribute to False and closes the serial port.
    outOfLogic
        Sets out_of_logic attribute to True.
    barcodeValueReaded
        A signal to notify the changing of Normal Barcode value.
    iranbarcodeValueReaded
        A signal to notify the changing of Iran Barcode value.
    run
        If the serial port is connected, it read the barcode.
        If the length of the barcode equals to 15, barcodeValueReaded is emitted.
        If the length of the barcode equals to 22 or 12, It considers the value of out_of_logic to emit two
        different signals (IDbarcodeReaded or IDbarcodeReadedLogic).
        If the length of the barcode is greater than 3, iranbarcodeValueReaded is emitted.
    disconnectSignals
        It disconnects from IDbarcodeReaded signal.
    __del__
        It closes the serial port.
    """
    portConnected: bool = True
    out_of_logic: bool = False

    def disconnect(self):
        """
        Closes the serial port.
        :return: None
        """
        self.portConnected = False
        self.ser.close()

    def __init__(self):
        """
        Parameters
        ----------

        """
        self.barcode: str = ""
        self.IDbarcode: str = ""
        self.ser = serial.Serial("/dev/ttyS0", baudrate=9600, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE,
                                 bytesize=serial.EIGHTBITS, timeout=1)
        QThread.__init__(self)

    def outOfLogic(self):
        """
        It sets out_of_logic variable to True
        :return: None
        """
        self.out_of_logic = True

    @Signal
    def barcodeValueReaded(self):
        pass

    @Signal
    def iranbarcodeValueReaded(self):
        pass

    IDbarcodeReaded = Signal()
    IDbarcodeReadedLogic = Signal()

    def run(self):
        """
        It read barcode from serial port and decide to emit which signal based on the length
        of the readed barcode.
        :return: None
        """
        while self.portConnected:
            readed_bytes = self.ser.read(32)

            # Read the normal barcode value
            if len(readed_bytes) == 15:
                self.barcode = readed_bytes[1:-1].decode('latin1')
                self.barcodeValueReaded.emit()

            # Read the ID barcode
            elif len(readed_bytes) == 22 or len(readed_bytes) == 12:
                self.IDbarcode = readed_bytes[1:-1].decode('latin1')
                if self.out_of_logic:
                    self.IDbarcodeReaded.emit()
                else:
                    self.IDbarcodeReadedLogic.emit()
            elif len(readed_bytes) > 3:
                self.iranbarcode = readed_bytes[1:-1].decode('latin1')
                self.iranbarcodeValueReaded.emit()
            # print(self.barcode)

    def disconnectSignals(self):
        self.IDbarcodeReaded.disconnect(self)
    
    def __del__(self):
        if (self.ser.isOpen()):
            self.ser.close()


# class Scanner(QObject):
#     barcode: str
#     iranbarcode: str
#     IDbarcode: str
#     _canTimerTick: bool = True

#     def __init__(self):
#         super().__init__()
#         print(
#             ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Barcode Scanner Start <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
#         self.ser = serial.Serial("/dev/ttyS0", baudrate=9600, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE,
#                                  bytesize=serial.EIGHTBITS, timeout=1)
#         self._canTimerTick = True
#         self._scannerThread = Thread(target=self.readBarcode)
#         self._scannerThread.start()

#     @Signal
#     def barcodeValueReaded(self):
#         pass

#     @Signal
#     def iranbarcodeValueReaded(self):
#         pass

#     @Signal
#     def IDbarcodeReaded(self):
#         pass

#     def readBarcode(self):
#         while self._canTimerTick:
#             readed_bytes = self.ser.read(32)
#             if len(readed_bytes) == 15:
#                 self.barcode = readed_bytes[1:-1].decode('latin1')
#                 self.barcodeValueReaded.emit()
#             elif len(readed_bytes) == 22 or len(readed_bytes) == 12:
#                 self.IDbarcode = readed_bytes[1:-1].decode('latin1')
#                 self.IDbarcodeReaded.emit()
#             elif len(readed_bytes) > 3:
#                 self.iranbarcode = readed_bytes[1:-1].decode('latin1')
#                 self.iranbarcodeValueReaded.emit()
#             # print(self.barcode)

#     def stopBarcodeReader(self):
#         self._canTimerTick = False
#         self._scannerThread.join()
#         self.ser.close()

#     def __del__(self):
#         print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Serial deleted <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
#         if (self.ser.isOpen()):
#             self.ser.close()
#         del self._scannerThread
