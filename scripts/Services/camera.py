import time
import cv2
from PySide2.QtCore import QObject, Signal, Property, Slot, QThread
import numpy as np
from datetime import datetime
from PySide2.QtGui import QImage, QGuiApplication
# from PySide2 import QtGui
from threading import Thread
import os
import sys


class CameraWorker(QThread):
    frameHeight = 184
    frameWidth = 236
    fps = 10

    _cameraID = []
    _camera1: cv2.VideoCapture
    _camera2: cv2.VideoCapture
    _frame: np.ndarray

    _canReadFrame: bool
    _switchTime: int = 15
    _lastSwitchTime: datetime
    _readFromCamera1: bool = True

    capturedImage: QImage

    def __init__(self):
        super().__init__()
        # self._camera1 = cv2.VideoCapture(0)
        # self._camera1.set(cv2.CAP_PROP_FRAME_WIDTH, self.frameWidth)
        # self._camera1.set(cv2.CAP_PROP_GIGA_FRAME_SENS_HEIGH, self.frameHeight)
        # self._camera1.set(cv2.CAP_PROP_FPS, self.fps)
        # self._camera2 = cv2.VideoCapture(1)
        # self._camera2.set(cv2.CAP_PROP_FRAME_WIDTH, self.frameWidth)
        # self._camera2.set(cv2.CAP_PROP_GIGA_FRAME_SENS_HEIGH, self.frameHeight)
        # self._camera2.set(cv2.CAP_PROP_FPS, self.fps)
        self._canReadFrame = False

        self._canTimerTick = True
        self._timerThread = Thread(target=self.timerSlot)
        self._timerThread.start()

    newFrameReadSignal = Signal()


    # def find_cameraID(self):
    #     for i in range(10):
    #         camera = cv2.VideoCapture(i)
    #         ret, frame = camera.read()
    #         if frame is not None:
    #             self._cameraID.append(int(i))

    def run(self):
        self._canReadFrame = True
        self._camera1 = cv2.VideoCapture(0)
        # self._camera1.set(cv2.CAP_PROP_FRAME_WIDTH, self.frameWidth)
        # self._camera1.set(cv2.CAP_PROP_FRAME_HEIGHT, self.frameHeight)
        # self._camera1.set(cv2.CAP_PROP_FPS, self.fps)
        self._camera2 = cv2.VideoCapture(1)
        # self._camera2.set(cv2.CAP_PROP_FRAME_WIDTH, self.frameWidth)
        # self._camera2.set(cv2.CAP_PROP_FRAME_HEIGHT, self.frameHeight)
        self._camera2.set(cv2.CAP_PROP_FRAME_WIDTH, self.frameHeight)
        self._camera2.set(cv2.CAP_PROP_FRAME_HEIGHT, self.frameWidth)
        self._camera2.set(cv2.CAP_PROP_FPS, self.fps)

        while self._canReadFrame:
            if self._readFromCamera1:
                ret, frame1 = self._camera1.read()
                # tempFrame = np.ascontiguousarray(frame1[80:400, 140:500])
                if frame1 is not None:
                    tempFrame = cv2.flip(np.ascontiguousarray(frame1[80:400, 140:500]), 1)
                    # frame1 = cv2.cvtColor(frame1, cv2.COLOR_RGB2BGR)
                    image = QImage(tempFrame, tempFrame.shape[1], tempFrame.shape[0], tempFrame.strides[0], QImage.Format_BGR888)
                    # frame1 = cv2.cvtColor(frame1, cv2.COLOR_RGB2BGR)
                    # image = QImage(frame1, frame1.shape[1], frame1.shape[0],
                    #                frame1.strides[0], QImage.Format_RGB888)
                    self.capturedImage = image
                    self.newFrameReadSignal.emit()
                    # QGuiApplication.processEvents()
                else:
                    print("cam1 no frame")
            else:

                ret2, frame2 = self._camera2.read()
                # if self._camera2.isOpened():
                if frame2 is not None:
                    # #frame2 = cv2.cvtColor(frame2, cv2.COLOR_RGB2BGR)
                    # image = QImage(frame2, frame2.shape[1], frame2.shape[0],
                    #                frame2.strides[0], QImage.Format_BGR888)

                    frame2 = cv2.cvtColor(frame2, cv2.COLOR_RGB2BGR)
                    temp = cv2.rotate(frame2, cv2.ROTATE_90_COUNTERCLOCKWISE)
                    image = QImage(temp, temp.shape[1], temp.shape[0],
                                   temp.strides[0], QImage.Format_RGB888)
                    
                    self.capturedImage = image
                    self.newFrameReadSignal.emit()
                    # QGuiApplication.processEvents()
                else:
                    print("cam2 no frame")
            # time.sleep(1)
            # cv2.waitKey(1000)
            time.sleep(0.03)
    
    @Slot()
    def stop(self):
        self._canReadFrame = False
        self._canTimerTick = False
        self._camera1.release()
        self._camera2.release()
        os.system("dd if=/dev/zero of=/dev/fb0")
        os.system("clear")
        os.execl(sys.executable, sys.executable, *sys.argv)

    def timerSlot(self):
        while self._canTimerTick:
            if self._readFromCamera1:
                self._readFromCamera1 = False
                time.sleep(10)
            else:
                self._readFromCamera1 = True
                time.sleep(3)

