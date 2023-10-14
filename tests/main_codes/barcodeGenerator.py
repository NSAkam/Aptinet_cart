from PySide2.QtQuick import *
from PySide2.QtGui import QImage
import code128
from PIL import Image
import re


class BarcodeGenerator(QQuickImageProvider):
    def __init__(self):
        super().__init__(QQuickImageProvider.Image)

    def requestImage(self, url, p_str, size):
        try:
            if not isinstance(url, str):
                raise TypeError("url must be a string")

            barcode_param = url[3:-3]

            if len(barcode_param) == 13 and re.match(r'^\d+$', barcode_param):
                barcode_image = code128.image(barcode_param, height=100)
                w, h = barcode_image.size
                new_h, margin = self.set_new_height(h)

                new_image = Image.new('RGBA', (w, new_h), (255, 255, 255))

                new_image.paste(barcode_image, (0, margin))
                # im = new_image.toqimage()
                im = QImage(new_image.tobytes(), new_image.size[0], new_image.size[1], QImage.Format_RGBA8888)
                return im
            else:
                raise Exception("Invalid barcode_param")
        except Exception as e:
            print("Error:", str(e))

    def set_new_height(self, old_height, margin=20):
        try:
            if isinstance(old_height, float) or isinstance(old_height, int):
                margin = 20
                new_height = old_height + (2 * margin)
                return new_height, margin
            else:
                raise TypeError("Input must be a float!")
        except TypeError as e:
            print(e)
