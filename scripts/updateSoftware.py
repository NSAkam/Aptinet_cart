from PySide2.QtCore import QUrl,QObject, Signal,Property, Slot
from Services.downloader import Downloader
import zipfile
import os,sys
import glob


class UpdateSoftware(QObject):

    _downloader:Downloader
    
    def __init__(self):
        super().__init__()
    
    @Signal
    def changed(self):
        pass
        
    setTotalProgressSignal = Signal(int,arguments=["v"])
    setCurrentProgressSignal = Signal(int,arguments=["v"])
    succeededSignal = Signal()


    @Slot()
    def startDownload(self):     
        self._downloader = Downloader("http://app.aptinet.com/api/APP/download")
        self._downloader.setTotalProgressSignal.connect(self.setTotalProgressSignal)
        self._downloader.setCurrentProgressSignal.connect(self.setCurrentProgressSignal)
        print("started Download")

        self._downloader.succeededSignal.connect(self.downloadSucceeded)
        self._downloader.finished.connect(self.downloadFinished)
        self._downloader.start()

    def downloadSucceeded(self):
        self.succeededSignal.emit()
        print("successFull Download")
    def downloadFinished(self):
        print("download Compeleted")
        try:
            print("unzipping")
            os.system("unzip -o /home/aptinet/Aptinet.zip -d /home/aptinet/Aptinet_cart")
            # os.remove("/home/Aptinet/Aptinet.zip")
            os.system("sudo reboot")
        except:
            try:
                os.remove("/home/Aptinet/Aptinet.zip")
            except:
                pass
        del self._downloader



class UpdateFiles(QObject):

    _downloader:Downloader
    
    def __init__(self):
        super().__init__()
    
    @Signal
    def changed(self):
        pass
        
    setTotalProgressSignal = Signal(int,arguments=["v"])
    setCurrentProgressSignal = Signal(int,arguments=["v"])
    succeededSignal = Signal()


    @Slot()
    def startDownload(self):     
        self._downloader = Downloader("http://app.aptinet.com/api/APP/downloadProdpics")
        self._downloader.setTotalProgressSignal.connect(self.setTotalProgressSignal)
        self._downloader.setCurrentProgressSignal.connect(self.setCurrentProgressSignal)
        print("started Download")

        self._downloader.succeededSignal.connect(self.downloadSucceeded)
        self._downloader.finished.connect(self.downloadFinished)
        self._downloader.start()

    def downloadSucceeded(self):
        self.succeededSignal.emit()
        print("successFull Download")
    def downloadFinished(self):
        print("download Compeleted")
        try:
            print("unzipping")
            files = glob.glob('/home/aptinet/files/*')
            for f in files:
                os.remove(f)
            os.system("unzip -o /home/aptinet/AptinetFiles.zip -d /home/aptinet/files")
            # zipfile.ZipFile.extractall("/home/kast/FinalFASKET/FASKET.zip")
            os.remove("/home/aptinet/AptinetFiles.zip")
            # os.system("sudo reboot")
        except:
            try:
                os.remove("/home/aptinet/AptinetFiles.zip")
            except:
                pass
        del self._downloader

