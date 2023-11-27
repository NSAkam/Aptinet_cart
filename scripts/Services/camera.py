import cv2
from PySide2.QtCore import QObject, Signal, Property, Slot, QThread
import numpy as np
from datetime import datetime


class CameraWorker(QThread):
    _cameraID = []
    _camera1: cv2.VideoCapture
    _camera2: cv2.VideoCapture
    _frame: np.ndarray

    _canReadFrame: bool
    _switchTime: int = 5
    _lastSwitchTime: datetime
    _readFromCamera1: bool = True

    def __init__(self):
        super().__init__()
        self.find_cameraID()
        self._camera1 = cv2.VideoCapture(self._cameraID[0])
        self._camera2 = cv2.VideoCapture(self._cameraID[1])
        self._camera1.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self._camera1.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        self._camera2.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self._camera2.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        self._canReadFrame = False
        # self._frame = np.ndarray((480, 640, 3))

    newFrameReadSignal = Signal()

    def get_frame(self):
        return self._frame

    def find_cameraID(self):
        for i in range(10):
            camera = cv2.VideoCapture(i,cv2.CAP_V4L)
            ret, frame = camera.read()
            if frame is not None:
                self._cameraID.append(int(i))

    def run(self):
        self._canReadFrame = True
        self._lastSwitchTime = datetime.now()
        while self._canReadFrame:
            if self._readFromCamera1:
                _, self._frame = self._camera1.read()
                self.newFrameReadSignal.emit()
                now = datetime.now()
                if (now - self._lastSwitchTime).seconds >= self._switchTime:
                    self._lastSwitchTime = now
                    self._readFromCamera1 = False
            else:
                _, self._frame = self._camera2.read()
                self.newFrameReadSignal.emit()
                now = datetime.now()
                if (now - self._lastSwitchTime).seconds >= self._switchTime:
                    self._lastSwitchTime = now
                    self._readFromCamera1 = True
            # self._canReadFrame = False

    def stop(self):
        self._canReadFrame = False
