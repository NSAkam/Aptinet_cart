from PySide2.QtMultimedia import QMediaPlayer, QMediaContent, QSound


def deleteSound():
    QSound.play("/home/aptinet/files/hazf.wav")


def insertSound():
    QSound.play("/home/aptinet/files/ezafe.wav")


def notifSound():
    QSound.play("/home/aptinet/files/notif.wav")


def notifSound2():
    QSound.play("/home/aptinet/files/notif2.wav")


def playSound(fileName: str):
    path = "/home/aptinet/files" + fileName + ".wav"
    QSound.play(path)