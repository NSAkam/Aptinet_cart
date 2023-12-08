import cv2
from PySide2.QtCore import QObject, Signal, Property, Slot, Qt
from Services.camera import CameraWorker
from PySide2.QtGui import QImage
from PySide2.QtQuick import QQuickImageProvider,QQuickAsyncImageProvider
import numpy as np


class CameraHelper(QQuickImageProvider):
    frameHeight = 184
    frameWidth = 236


    _camera: CameraWorker
    _image: QImage

    def __init__(self, camera: CameraWorker):
        self._camera = camera
        self._camera.newFrameReadSignal.connect(self.read_frame)
        image = QImage(self.frameHeight, self.frameWidth, QImage.Format_RGBA8888)
        image.fill(Qt.black)
        self._image = image
        super().__init__(QQuickImageProvider.Image)

    @Signal
    def newImageReadSignal(self):
        pass

    @Slot()
    def read_frame(self):
        if(self._image != self._camera.capturedImage):
            self._image = self._camera.capturedImage
            # self._image = image

    def requestImage(self, id, p_str, size):
        return self._image
    
    # def requestImageResponse(self,id,_):
    #     return self._image

    # def start(self):
    #     self._camera.start()

    # def stop(self):
    #     self._camera.stop()
