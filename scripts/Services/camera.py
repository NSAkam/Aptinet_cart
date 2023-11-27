import time
import cv2
from PySide2.QtCore import QObject, Signal, Property, Slot, QThread
import numpy as np
from datetime import datetime
from PySide2.QtGui import QImage
from threading import Thread


class CameraWorker(QThread):
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
        self._camera1 = cv2.VideoCapture(0)
        self._camera2 = cv2.VideoCapture(1)
        self._canReadFrame = False

        self._canTimerTick = True
        # self._timerThread = Thread(target=self.timerSlot)
        # self._timerThread.start()

    newFrameReadSignal = Signal()


    # def find_cameraID(self):
    #     for i in range(10):
    #         camera = cv2.VideoCapture(i)
    #         ret, frame = camera.read()
    #         if frame is not None:
    #             self._cameraID.append(int(i))

    def run(self):
        self._canReadFrame = True
        _, frame1 = self._camera1.read()
        # _, frame2 = self._camera2.read()

        while self._canReadFrame:
            if self._readFromCamera1:
                frame = frame1
                if self._camera1.isOpened():
                    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
                    image = QImage(frame, frame.shape[1], frame.shape[0],
                                   frame.strides[0], QImage.Format_RGB888)
                    self.newFrameReadSignal.emit()
                    self.capturedImage = image
                else:
                    print("cam1 no frame")
            else:
                # frame = frame2
                if self._camera2.isOpened():
                    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
                    image = QImage(frame, frame.shape[1], frame.shape[0],
                                   frame.strides[0], QImage.Format_RGB888)
                    self.newFrameReadSignal.emit()
                    self.capturedImage = image
                else:
                    print("cam2 no frame")

    def stop(self):
        self._canReadFrame = False
        self._canTimerTick = False

    def timerSlot(self):
        while self._canTimerTick:
            time.sleep(self._switchTime)
            if self._readFromCamera1:
                self._readFromCamera1 = False
            else:
                self._readFromCamera1 = True
