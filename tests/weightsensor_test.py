import unittest
import numpy as np
from statistics import mean
from PySide2.QtCore import Signal
from weightsensor import WeightSensorWorker
from unittest.mock import MagicMock


class TestWeightSensorWorker(unittest.TestCase):

    def setUp(self) -> None:
        self.WeightSensor = WeightSensorWorker()
        self.read_weight_buffer = [980, 981, 982, 975, 986, 979, 990, 950, 1050, 1020]


    # def set_weights_atstartup(self):
    #     self.setstartWeight(mean(self.read_weight_buffer))
    #     self._BasketWeight2 = mean(self.read_weight_buffer)
    #     self._BasketWeight1 = self._BasketWeight2
    #     self._atstartUp = False
    #
    #     return self._atstartUp, self._startWeight, self._BasketWeight1, self._BasketWeight2
    #
    # def set_weights_atstartupFalse_if(self):
    #     self._BasketWeight1 = 10
    #     if mean(self.read_weight_buffer) > self._BasketWeight1:
    #         a = np.array(self.read_weight_buffer)  # Converting read_weight_buffer to a numpy array
    #         half_quartile = np.percentile(a, 50)  # Calculating the q2 of the a
    #         c = 0  # A counter
    #         s = 0  # A summation
    #         for w in self.read_weight_buffer:
    #             if w >= half_quartile:  # If a weight in read_weight_list is bigger than q2
    #                 c += 1  # Adding 1 to the counter
    #                 s += w  # Summing it with s
    #     self._BasketWeight2 = int(s / c)  # Calculating the mean of weights greater than q2
    #     return self._BasketWeight1, self._BasketWeight2
    #
    # def set_weights_atstartupFalse_else(self):
    #     self._BasketWeight1 = 940
    #     self._BasketWeight2 = mean(self.read_weight_buffer)
    #     if (self._BasketWeight2 - self._BasketWeight1) >= self.lightest_weight or (
    #             self._BasketWeight2 - self._BasketWeight1) <= (
    #             -1 * min(self.lightest_weight, self.lightest_weight_for_remove)):
    #         self.setbasketweight(int(self._BasketWeight2))
    #
    #     self._BasketWeight1 = self._BasketWeight2
    #
    #     return self._BasketWeight1, self._BasketWeight2

    def test_setOffset(self):
        self.WeightSensor.read_offset_from_file()
        # self.assertEqual(self.WeightSensor._offset, 90000)
        self.assertRaises(ValueError)

    def test_setScale(self):
        self.WeightSensor.read_scale_from_file()
        self.assertEqual(self.WeightSensor._scale, 90)
        self.assertRaises(ValueError)

    def test_outlierRemover(self):
        my_list = [-2, -1, 0, 1, 2, 3, 4, 5, 6]
        self.assertEqual(self.WeightSensor.outlierRemover(my_list), 2)

    def test_setcurrentweight(self):
        self.WeightSensor.setcurrentweight(5)
        self.assertEqual(self.WeightSensor._currentWeight, 5)

    def test_setbasketweight(self):
        self.WeightSensor.setbasketweight(10)
        self.assertEqual(self.WeightSensor._basketweight, 10)

    def test_setstartWeight(self):
        self.WeightSensor.setstartWeight(12)
        self.assertEqual(self.WeightSensor._startWeight, 12)

    def test_setisstable(self):
        self.WeightSensor.setisstable(False)
        self.WeightSensor.setisstable('fjh')
        # self.assertEqual(self.WeightSensor._isStable, False)
        self.assertRaises(Exception)

    def test_run_setcurrentweight(self):
        noise_reduction_buffer = [980, 981, 982, 975, 986, 979, 990]
        self.WeightSensor.setcurrentweight(self.WeightSensor.outlierRemover(noise_reduction_buffer,1))
        self.assertEqual(self.WeightSensor._currentWeight, 981)

    def test_run_checking_read_weight_buffer_elements(self):
        # my_list = [980, 981, 1020, 982, 975, 986, 979, 990]
        self.WeightSensor.check_list_for_abnormalities(self.read_weight_buffer, 8)
        self.assertEqual(self.WeightSensor._isStable, False)
        self.assertEqual(self.WeightSensor._canread, False)

    def test_filter_by_second_quartile(self):
        result = self.WeightSensor.filter_by_second_quartile(self.read_weight_buffer)
        self.assertEqual(result, 1005)

    # def test_run(self):
    #     self.WeightSensor.outlierRemover = MagicMock(return_value=50)
    #     self.WeightSensor.read_weight_buffer = [50, 50, 50, 50, 50]
    #     # self.WeightSensor.read_weight_buffer = self.read_weight_buffer
    #     self.WeightSensor.setstartWeight = MagicMock()
    #     # self.WeightSensor.basketweight_changed.emit = MagicMock()
    #     self.WeightSensor.setbasketweight = MagicMock()
    #     self.WeightSensor.run()
    #     # self.WeightSensor.setstartWeight.assert_called_once_with(50)
    #     # self.WeightSensor.basketweight_changed.emit.assert_not_called()
    #     # self.WeightSensor.setbasketweight.assert_not_called()
    #     #
    #     # self.WeightSensor.read_weight_buffer = [50, 50, 50, 50, 75]
    #     # self.WeightSensor.run()
    #     # self.WeightSensor.basketweight_changed.emit.assert_called_once_with(75, 50)
    #     # self.WeightSensor.setbasketweight.assert_called_once_with(75)

    def test_run(self):
        # Mock the HX711 get_grams method
        self.WeightSensor.hx.get_grams = MagicMock(return_value=100)

        # Mock the WeightSensorWorker outlierRemover method
        self.WeightSensor.outlierRemover = MagicMock(return_value=100)

        # Run the run method
        self.WeightSensor.run()

        # Assert that the HX711 get_grams method was called
        self.WeightSensor.hx.get_grams.assert_called_once_with(times=1)

        # Assert that the WeightSensorWorker outlierRemover method was called
        self.WeightSensor.outlierRemover.assert_called_once_with(self.WeightSensor.noise_reduction_buffer, 1)


    # def test_set_weights_atstartup(self):
    #     atstartUp, startWeight, BasketWeight1, BasketWeight2 = self.set_weights_atstartup()
    #     self.assertEqual(atstartUp, False)
    #     self.assertEqual(startWeight, 989.3)
    #     self.assertEqual(BasketWeight1, 989.3)
    #     self.assertEqual(BasketWeight2, 989.3)
    #
    # def test_set_weights_atstartupFalse_if(self):
    #     basketweight1, basketweight2 = self.set_weights_atstartupFalse_if()
    #     self.assertEqual(basketweight2, 1005)
    #     self.assertEqual(basketweight1, 10)
    #
    # def test_set_weights_atstartupFalse_else(self):
    #     basketweight1, basketweight2 = self.set_weights_atstartupFalse_else()
    #     self.assertEqual(basketweight2, 989.3)
    #     self.assertEqual(basketweight1, 989.3)

    def test_signals(self):
        self.assertIsInstance(self.WeightSensor.changed, Signal)
        self.assertIsInstance(self.WeightSensor.currentweight_changed, Signal)
        self.assertIsInstance(self.WeightSensor.isstable_changed, Signal)
        self.assertIsInstance(self.WeightSensor.startWeightchanged, Signal)
        self.assertIsInstance(self.WeightSensor.basketweight_changed, Signal)
        self.assertEqual(self.WeightSensor.changed, self.WeightSensor.changed)
        self.assertEqual(self.WeightSensor.currentweight_changed, self.WeightSensor.currentweight_changed)
        self.assertEqual(self.WeightSensor.isstable_changed, self.WeightSensor.isstable_changed)
        self.assertEqual(self.WeightSensor.startWeightchanged, self.WeightSensor.startWeightchanged)
        self.assertEqual(self.WeightSensor.basketweight_changed, self.WeightSensor.basketweight_changed)


    if __name__ == '__main__':
        unittest.main()



