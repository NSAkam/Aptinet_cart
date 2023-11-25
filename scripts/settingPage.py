from PySide2.QtCore import QObject, Signal, Property,Slot,QUrl


class SettingPage(QObject):
    def __init__(self):
        super().__init__()