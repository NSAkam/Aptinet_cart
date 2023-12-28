from PySide2.QtNetwork import QHttpMultiPart, QHttpPart, QNetworkRequest, QNetworkReply, QNetworkAccessManager
from PySide2 import QtNetwork
from PySide2.QtCore import QThread, Signal, Slot, QEventLoop, QFile, QIODevice


class Downloader(QThread):

    setTotalProgressSignal = Signal(int, arguments=["v"])
    setCurrentProgressSignal = Signal(int, arguments=["v"])
    succeededSignal = Signal()

    def __init__(self, url):
        self.url = url
        super().__init__()

    @Slot(int, int)
    def progressbar(self, a: int, b: int):
        if (a > 0 and b > 0):
            print(int((float(a)/float(b))*100.0))
            self.setCurrentProgressSignal.emit(int((float(a)/float(b))*100.0))
        else:
            pass

    @Slot(QNetworkReply)
    def downloadFinished(self, reply: QNetworkReply):
        if (reply.size() > 1):
            if (reply.error() == QNetworkReply.NoError):
                print("start save file")
                dfile = QFile("/home/aptinet/AptinetFiles.zip")
                if dfile.open(QIODevice.WriteOnly):
                    dfile.write(reply.readAll())

        dfile.close()
        self.succeededSignal.emit()
        self.loop.quit()

    def run(self):
        self.loop = QEventLoop()
        manager = QtNetwork.QNetworkAccessManager()
        netAcc = manager.networkAccessible
        manager.finished.connect(self.downloadFinished)
        req = QNetworkRequest(self.url)

        rep = manager.get(req)
        rep.downloadProgress.connect(self.progressbar)

        self.loop.exec_()
        print("exitted")
