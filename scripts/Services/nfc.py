from time import sleep
import typing

from smartcard.CardMonitoring import CardMonitor, CardObserver
from smartcard.util import toHexString
from PySide2.QtCore import QObject, Signal, Property, Slot, QThread


class nfc(QObject):
    
    nfcReaderSignal = Signal()

    def __init__(self):
        super().__init__()
        cardmonitor = CardMonitor()
        cardobserver = PrintObserver()
        cardobserver.readedSignal.connect(self.read)
        cardmonitor.addObserver(cardobserver)
        sleep(1000)
        cardmonitor.deleteObserver(cardobserver)

    @Slot
    def read(self):
        self.nfcReaderSignal.emit()



    

    


# a simple card observer that prints inserted/removed cards
class PrintObserver(CardObserver,QObject):
    """A simple card observer that is notified
    when cards are inserted/removed from the system and
    prints the list of cards
    """
    readedSignal = Signal()


    def update(self, observable, actions):
        (addedcards, removedcards) = actions
        for card in addedcards:
            print("+Inserted: ", toHexString(card.atr))
            self.readedSignal.emit()
        for card in removedcards:
            print("-Removed: ", toHexString(card.atr))
            self.readedSignal.emit()
