from PySide2.QtCore import QObject, Signal, Property, Slot,QThread
import numpy as np
from time import sleep
from statistics import mean
from copy import copy

class HX711(QObject):
    def __init__(self, pin1, pin2):
        pass

    def set_offset(self, offset):
        pass

    def set_scale(self, scale):
        pass

    def get_grams(self, times):
        return 100

class WeightSensorWorker(QThread):

    _offset: float = 0 # A variable to store offset receiving from the offset.txt
    _scale: float = 0 # A variable to store scale receiving from the scale.txt
    _startWeight: int = 0  # If _atstartUp is true, it means we are at the start of weighting.Then this variable
    # will set on the mean of read_weight_buffer
    _BasketWeight1: int = 0  # A variable to store _BasketWeight2
    _BasketWeight2: int = 0  # A variable to store weight (mean of the read_weight_buffer)
    _currentWeight: int = 0
    _tolerance: float = 25
    _basketweight = 0
    _canread = False
    _atstartUp = True
    _startUpHandler = 0
    _isStable: bool = False

    noise_reduction_buffer_size = 20
    noise_reduction_buffer = []
    last_weight = 0
    read_weight_buffer_size = 20 # buffer size for shifting weights to it
    read_weight_buffer = [] #buffer for shifting weights to it
    lightest_weight = 25  # 8
    lightest_weight_for_remove = 17  # 25 - 8
    acceptable_tolerance = 8
    ignored_bits = 0
    is_stable_tolerance = 25

    def __init__(self):
        super().__init__()
        self._startUpHandler = self.noise_reduction_buffer_size
        self.hx = HX711(23, 24)

        # Creating a list named read_weight_buffer containing of zeros as much as read_weight_buffer_size
        for i in range(self.read_weight_buffer_size):
            self.read_weight_buffer.append(0)

        # Creating a list named noise_reduction_buffer containing of zeros as much as noise_reduction_buffer_size
        for i in range(self.noise_reduction_buffer_size):
            self.noise_reduction_buffer.append(0)

        self.read_offset_from_file()
        self.hx.set_offset(self._offset)

        self.read_scale_from_file()
        self.hx.set_scale(self.scale)

        self.lightest_weight_register = self.lightest_weight


    @Signal
    def changed(self):
        pass

    @Signal
    def currentweight_changed(self):
        pass

    @Signal
    def isstable_changed(self):
        pass

    def getOffset(self):
        return self._offset

    def setOffset(self, v):
        self._offset = v
        self.changed.emit()

    offset = Property(float, getOffset, setOffset, notify=changed)

    def getScale(self):
        return self._scale

    def setScale(self, v):
        self._scale = v
        self.changed.emit()

    scale = Property(float, getScale, setScale, notify=changed)

    def getcurrentweight(self):
        return self._currentWeight

    def setcurrentweight(self, val):
        self._currentWeight = val
        self.currentweight_changed.emit()

    currentweight = Property(int, getcurrentweight, setcurrentweight, notify=currentweight_changed)

    startWeightchanged = Signal(int)

    def readbasketweight(self):
        return self._basketweight

    def setbasketweight(self, val):
        self._basketweight = val
        self.changed.emit()

    basketweight_changed = Signal(int, int)
    basketweight = Property(int, readbasketweight, setbasketweight, notify=changed)

    def getstartWeight(self):
        return self._startWeight

    def setstartWeight(self, val: int):
        # print("set start weight is " + str(val))
        self._startWeight = val
        self.startWeightchanged.emit(val)

    startWeight = Property(int, getstartWeight, setstartWeight, notify=startWeightchanged)

    def getisstable(self):
        return self._isStable

    def setisstable(self, val):
        try:
            if isinstance(val, bool):
                self._isStable = val
                self.isstable_changed.emit()
            else:
                raise TypeError("Value must be a boolean")
        except TypeError as e:
            print(e)

    isstable = Property(bool, getisstable, setisstable, notify=isstable_changed)

    def read_offset_from_file(self):
        with open("offset.txt", 'r') as f:
            data = f.readline()
            try:
                self.setOffset(float(data))
            except ValueError:
                print('Invalid data! The type of data is', type(data))

    def read_scale_from_file(self):
        with open("scale.txt", 'r') as f:
            data = f.readline()
            try:
                self.setScale(float(data))
            except ValueError:
                print('Invalid data! The type of data is', type(data))

    def check_list_for_abnormalities(self, list, size):
        for i in range(size):
            for j in range(i, size):
                # Calculating the absolute difference between a value with other values in read_weight_buffer
                diff = abs(list[i] - list[j])
                if diff >= self.is_stable_tolerance:
                    self.setisstable(False)
                    self._canread = False
                    break
                elif diff >= self.acceptable_tolerance:
                    self._canread = False

    def filter_by_second_quartile(self, list):
        a = np.array(list)  # Converting read_weight_buffer to a numpy array
        half_quartile = np.percentile(a, 50)  # Calculating the q2 of the a
        c = 0  # A counter
        s = 0  # A summation
        for w in list:
            if w >= half_quartile:  # If a weight in read_weight_list is bigger than q2
                c += 1  # Adding 1 to the counter
                s += w  # Summing it with s
        return int(s / c)  # Calculating the mean of weights greater than q2

    def outlierRemover(self, data_list, outlier_margin=1.5):
        """
        Removes outlier data from weghit sensor's output
        :param data_list: receiving data from weight sensor
        :param outlier_margin: a constant with is multiplied to extend the range of data
        :return: the mean of selected weights list
        """
        try:
            a = np.array(data_list)
            upper_quartile = np.percentile(a, 75)  # q3
            lower_quartile = np.percentile(a, 25)  # q1
            IQR = max(((upper_quartile - lower_quartile) * outlier_margin), 8)  # IQR = (q3 - q1 )
            quartileSet = (lower_quartile - IQR, upper_quartile + IQR)
            resultList = []
            for raw_number in a.tolist():
                if quartileSet[0] <= raw_number <= quartileSet[1]:
                    resultList.append(raw_number)
            # print(resultList)
            return int(sum(resultList) / len(resultList)) if len(resultList) > 0 else 0
        except Exception as e:
            print(f"An error occurred: {e}")
            return 0

    def run(self):
        # while True:
        result: int = self.hx.get_grams(times=1)

        self.noise_reduction_buffer.pop(0)  # Removing a zero from noise_reduction_buffer list
        self.noise_reduction_buffer.append(int(result))  # Adding receiving weights from sensor
        # to the noise_reduction_buffer list

        # Removing outliers from the noise_reduction_buffer list and set the result to _currentWeight
        self.setcurrentweight(self.outlierRemover(self.noise_reduction_buffer, 1))

        self.read_weight_buffer.pop(0)  # Removing zeros from read_weight_buffer list
        self.read_weight_buffer.append(self.getcurrentweight())  # Adding _currentWeight to read_weight_buffer
        if self._startUpHandler > 0:  # It has been set to self.noise_reduction_buffer_size=20 at first
            self._startUpHandler = self._startUpHandler - 1
        else:
            self.setisstable(True)
            self._canread = True
            self.check_list_for_abnormalities(self.read_weight_buffer, self.read_weight_buffer_size)

            if self._canread:
                if self._atstartUp == True:
                    # Set _startWeight, _BasketWeight2 and _BasketWeight1 on the mean of read_weight_buffer
                    self.setstartWeight(mean(self.read_weight_buffer))
                    self._BasketWeight2 = mean(self.read_weight_buffer)
                    self._BasketWeight1 = self._BasketWeight2
                    self._atstartUp = False
                else:
                    if mean(self.read_weight_buffer) > self._BasketWeight1:
                        self._BasketWeight2 = self.filter_by_second_quartile(self.read_weight_buffer)

                    else:
                        self._BasketWeight2 = mean(self.read_weight_buffer)
                    if (self._BasketWeight2 - self._BasketWeight1) >= self.lightest_weight or (
                            self._BasketWeight2 - self._BasketWeight1) <= (
                            -1 * min(self.lightest_weight, self.lightest_weight_for_remove)):
                        self.basketweight_changed.emit(self._BasketWeight2, self._BasketWeight1)
                        self.setbasketweight(int(self._BasketWeight2))

                    self._BasketWeight1 = self._BasketWeight2

    def stopWeightSensorRead(self):
        del self.hx

    def __del__(self):
        print(" >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Weight Sensor Deleted <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
