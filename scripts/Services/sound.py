from PySide2.QtMultimedia import QMediaPlayer,QMediaContent,QSound


def deleteSound():
    QSound.play("/home/aptinet/hazf.wav")

def insertSound():
    QSound.play("/home/aptinet/ezafe.wav")

def notifSound():
    QSound.play("/home/aptinet/notif.wav")

def notifSound2():
    QSound.play("/home/aptinet/notif2.wav")
