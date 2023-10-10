import unittest
from statistics import mean
import numpy as np
from unittest.mock import MagicMock, patch
from battery import BatteryWorker, Battery
from PySide2.QtCore import Signal, Slot


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
        self.Battery = Battery()
        self.hex_number = [['F0', 'DA']]
        # self.i2c = i2c()

    def test_set_data_true_value(self):
        data = self.BatteryWorker.set_data(self.hex_number)
        self.assertEqual(data, 61658)

    def test_read_file_true_value_1(self):
        with open("min.txt", "w") as file:
            file.write('1000')
        result = self.BatteryWorker.read_file('min')
        self.assertEqual(result, 1000)

    def test_read_file_true_value_2(self):
        with open("max.txt", "w") as file:
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
        self.BatteryWorker.in_init = False
        self.BatteryWorker.level = 6
        self.BatteryWorker.set_data = MagicMock(return_value=5)
        self.BatteryWorker.outlierRemover = MagicMock(return_value=8)
        self.BatteryWorker.meanbuffer = [5, 5, 5, 5]
        self.BatteryWorker.read_file = MagicMock(side_effect=lambda input: 1 if input == 'min' else 2)
        self.BatteryWorker.write_file = MagicMock(side_effect=lambda input, data: 1 if input == 'min' else 2)
        self.BatteryWorker.normalize_data = MagicMock(return_value=5.75) # You can comment this one. If you do it, you
        # should comment this line: self.BatteryWorker.normalize_data.assert_called_once_with(data=5.75, min=1, max=2)
        self.BatteryWorker.updateLevel = MagicMock()

        self.BatteryWorker.run()

        self.BatteryWorker.set_data.assert_called_once()
        self.BatteryWorker.read_file.assert_any_call('min')
        self.BatteryWorker.read_file.assert_any_call('max')
        # self.BatteryWorker.write_file.assert_any_call("max", 5)
        # self.BatteryWorker.write_file.assert_any_call("min", 5)
        # self.BatteryWorker.write_file.assert_called_once()
        # self.BatteryWorker.normalize_data.assert_called()
        self.BatteryWorker.write_file.assert_called_once_with('max',5.75)
        # self.BatteryWorker.write_file.assert_any_call('min', 5)
        self.BatteryWorker.normalize_data.assert_called_once_with(data=5.75, min=1, max=2)
        self.BatteryWorker.updateLevel.emit.assert_called()

    def test_get_level_with_valid_input(self):
        self.Battery._level = 11
        self.Battery.getLevel()
        self.assertEqual(self.Battery._level, 11)

    def test_set_level_with_valid_input(self):
        self.Battery.changed = MagicMock()
        self.Battery.setLevel(15)
        self.assertEqual(self.Battery._level, 15)
        self.Battery.changed.emit.assert_called_once()

    def test_updateLevel_with_valid_input(self):
        self.Battery.changed = MagicMock()
        self.Battery.updateLevel(12)
        self.assertEqual(self.Battery._level, 12)
        self.Battery.changed.emit.assert_called_once()

    def test_changed_signal(self):
        self.assertIsInstance(self.Battery.changed, Signal)

    def test_Battery(self):
        self.Battery._level = 10
        self.assertIsInstance(self.Battery._threadUpdate, BatteryWorker)
        self.assertEqual(self.Battery._level, 10)







