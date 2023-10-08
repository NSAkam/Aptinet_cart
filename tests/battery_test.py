import unittest
from statistics import mean
import numpy as np
from unittest.mock import MagicMock, patch
from battery import BatteryWorker, i2c

class TestBattery(unittest.TestCase):

    def setUp(self) -> None:
        self.buffer = [61658, 60252, 61900, 61200, 62500]
        self.size = 5
        self.meanbuffer = [61658, 60252, 61900, 61200, 62500]
        self.meansize = 5
        self.level: int = 100
        self.in_init: bool = True
        self.counter = 0
        self.BatteryWorker = BatteryWorker()
        self.hex_number = [['F0', 'DA']]
        self.i2c = i2c()

    def test_set_data_true_value(self):
        data = self.BatteryWorker.set_data(self.hex_number)
        self.assertEqual(data, 61658)

    def test_read_file_true_value_1(self):
        with open("min.txt", "w") as file:
            file.write('1000')
        result = self.BatteryWorker.read_file('min')
        self.assertEqual(result, 46)

    def test_read_file_true_value_2(self):
        with open("min.txt", "w") as file:
            file.write("10000")
        result = self.BatteryWorker.read_file('max')
        self.assertEqual(result, 10000)

    def test_read_file_raise_exception_1(self):
        with open("min.txt", "w") as file:
            file.write("gfd")
        with self.assertRaises(Exception):
            self.BatteryWorker.read_file('min')

    def test_read_file_raise_exception_2(self):
        with open("max.txt", "w") as file:
            file.write("asjl")
        with self.assertRaises(Exception):
            self.BatteryWorker.read_file('max')

    def test_write_file_with_valid_input(self):
        self.assertIsNone(self.BatteryWorker.write_file('min', 10))

    def test_write_file_with_invalid_input(self):
        with self.assertRaises(ValueError):
            self.BatteryWorker.write_file('invalid', 10)

    def test_write_file_with_file_not_found(self):
        with self.assertRaises(Exception):
            self.BatteryWorker.write_file('min', 10)

    def test_write_file_with_zero_data(self):
        with self.assertRaises(Exception):
            self.BatteryWorker.write_file('max', 0)

    def test_normalize_data_with_valid_input(self):
        self.assertEqual(self.BatteryWorker.normalize_data(50, 0, 100), 50)

    def test_normalize_data_with_zero_division(self):
        with self.assertRaises(Exception):
            self.BatteryWorker.normalize_data(50, 100, 100)

    def test_outlierRemover(self):
        data = self.BatteryWorker.outlierRemover(self.buffer)
        self.assertEqual(data, 61502)

    @patch('time.sleep', MagicMock())  # Mock the time.sleep() function
    def test_run(self):
        self.i2c = MagicMock(return_value=500)
        self.BatteryWorker.set_data = MagicMock(return_value=500)
        self.BatteryWorker.read_file = MagicMock(return_value=100)
        self.BatteryWorker.write_file = MagicMock()
        self.BatteryWorker.normalize_data = MagicMock(return_value=50)
        self.BatteryWorker.updateLevel = MagicMock()

        self.BatteryWorker.run()

        self.BatteryWorker.set_data.assert_called_once()
        self.BatteryWorker.read_file.assert_called_once_with('min')
        self.BatteryWorker.write_file.assert_called_once_with('min', 500)
        self.BatteryWorker.normalize_data.assert_called_once_with(data=500, min=100, max=100)
        self.BatteryWorker.updateLevel.assert_called_once_with(50)