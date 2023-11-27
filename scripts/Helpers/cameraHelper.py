import cv2
from PySide2.QtCore import QObject, Signal, Property, Slot, Qt
from Services.camera import CameraWorker
from PySide2.QtGui import QImage
from PySide2.QtQuick import QQuickImageProvider
import numpy as np


class CameraHelper(QQuickImageProvider):
    frameHeight = 184
    FrameWidth = 236
    _camera: CameraWorker
    _image: QImage

    def __init__(self,_c:CameraWorker):
        # self._camera = CameraWorker()
        self._camera = _c
        self._camera.newFrameReadSignal.connect(self.read_frame)
        self._image = QImage(self.frameHeight, self.FrameWidth, QImage.Format_RGBA8888)
        self._image.fill(Qt.black)
        # self.start()
        super().__init__(QQuickImageProvider.Image)

    # newImageReadSignal = Signal()
    @Signal
    def newImageReadSignal(self):
        pass

    @Slot()
    def read_frame(self):
        self._image = self._camera.capturedImage

        # frame = self._camera.get_frame()
        # # print("helper. befor resize:")
        # # print(np.shape(frame))
        # try:
        #     frame = cv2.resize(frame, (self.frameHeight, self.FrameWidth))

        # except:
        #     frame = np.ndarray((236, 184))

        # # print("helper. after resize:")
        # # print(np.shape(frame))
        # frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        # # print("coler convert")
        # self._image = QImage(frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888)
        # # print("Q imqge")
        # # self.newImageReadSignal.emit()
        # # print("image signal")

    def requestImage(self, id, p_str, size):
       
        return self._image

    def start(self):
        self._camera.start()

    def stop(self):
        self._camera.stop()
