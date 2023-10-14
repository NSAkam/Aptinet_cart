import unittest
from PySide2.QtGui import QImage
from tests.main_codes.barcodeGenerator import BarcodeGenerator


class TestBarcodeGenerator(unittest.TestCase):
    def setUp(self) -> None:
        self.BarcodeGenerator = BarcodeGenerator()
        self.barcode_param_str = 'der6261643501970cdr'
        self.barcode_param_int = 1116261643501970111

    def test_set_new_height_true_value_1(self):
        self.old_height = 30
        new_height, margin = self.BarcodeGenerator.set_new_height(self.old_height)
        self.assertEqual(new_height, 70)

    def test_set_new_height_raise_exception_1(self):
        self.old_height = "gdf"
        new_height = self.BarcodeGenerator.set_new_height(self.old_height)
        self.assertRaises(Exception)

    def test_set_new_height_true_value_2(self):
        self.old_height = 30.0
        new_height, margin = self.BarcodeGenerator.set_new_height(self.old_height)
        self.assertEqual(new_height, 70.0)

    def test_requestImage_true_value_1(self): # output is None
        im = self.BarcodeGenerator.requestImage(url=self.barcode_param_str, p_str='a', size=1)
        self.assertIsNotNone(im)
        self.assertIsInstance(im, QImage)

    def test_requestImage_raise_exception_1(self):
        im = self.BarcodeGenerator.requestImage(url=self.barcode_param_int, p_str='a', size=1)
        self.assertRaises(Exception)

    def test_requestImage_raise_exception_2(self):
        im = self.BarcodeGenerator.requestImage(url='der626164t3501970cdr', p_str='a', size=1)
        self.assertRaises(TypeError)




