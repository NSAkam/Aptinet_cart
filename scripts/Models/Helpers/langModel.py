from ast import Dict
from typing import Any
from PySide2.QtCore import Signal, Property, QAbstractListModel, QModelIndex, Slot
from PySide2.QtCore import QModelIndex, Qt, QByteArray
from Models.lang import Lang


class LangModel(QAbstractListModel):
    NameRole = Qt.UserRole

    m_data = [Lang]

    def __init__(self):
        super().__init__()
        self.m_data = []

    @Signal
    def changed(self):
        pass

    # Function #################################################################

    def rowCount(self, parent) -> int:  # Override
        if (parent.isValid()):
            return 0
        return len(self.m_data)

    def data(self, index, role: int) -> Any:  # Override
        if (not index.isValid()):
            return
        lan = self.m_data[index.row()]
        if (role == self.NameRole):
            return lan.name
        else:
            return None

    def roleNames(self) -> Dict:  # Override
        default = super().roleNames()
        default[self.NameRole] = QByteArray(b"name")
        return default

    def clearData(self):
        self.beginResetModel()
        self.m_data.clear()
        self.changed.emit()
        self.endResetModel()

    def count(self) -> int:
        return len(self.m_data)

    def insert_languageList(self, langs: [Lang]):
        self.beginResetModel()
        for l in langs:
            self.m_data.append(l)
        self.endResetModel()

    def initialize_productList(self, prods: [Lang]):
        self.beginResetModel()
        self.m_data = prods
        self.endResetModel()
