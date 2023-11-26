import cv2
from PySide2.QtCore import QObject, Signal, Property, Slot


class Camera(QObject):
    _cameraID = []
    _camera1: cv2.VideoCapture
    _camera2: cv2.VideoCapture

    def __init__(self):
        super().__init__()
        self.find_cameraID()
        self._camera1 = cv2.VideoCapture(self._cameraID[0])
        self._camera2 = cv2.VideoCapture(self._cameraID[1])


    def find_cameraID(self):
        for i in range(10):
            camera = cv2.VideoCapture(i)
            ret, frame = camera.read()
            if frame is not None:
                self._cameraID.append(int(i))
