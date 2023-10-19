from PySide2.QtCore import QObject
from PySide2.QtCore import QObject, Signal, Property

class Suggestion(QObject):
    _id: int
    _pBarcode: str
    _psBarcode: str

    def __init__(self):
        super().__init__()

    changed = Signal()

    def getId(self):
        return self._id

    def setId(self, val):
        self._id = val
        self.changed.emit()

    id = Property(int, getId, setId, notify=changed)

    def getPBarcode(self):
        return self._pBarcode

    def setPBarcode(self, val):
        self._pBarcode = val
        self.changed.emit()

    pBarcode = Property(str, getPBarcode, setPBarcode, notify=changed)

    def getPsBarcode(self):
        return self._psBarcode

    def setPsBarcode(self, val):
        self._psBarcode = val
        self.changed.emit()

    psBarcode = Property(str, getPsBarcode, setPsBarcode, notify=changed)
