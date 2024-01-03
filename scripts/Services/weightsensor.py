from PySide2.QtCore import QObject, Signal, Property, Slot, QThread
from Module.hx711 import HX711
import numpy as np
from time import sleep
from statistics import mean
from copy import copy


class WeightSensorWorker(QThread):
    _offset: float
    _scale: float
    _startWeight: int = 0
    _BasketWeight1: int = 0
    _BasketWeight2: int = 0
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
    read_weight_buffer_size = 50  # buffer size for shifting weights to it
    read_weight_buffer = []  # buffer for shifting weights to it
    lightest_weight = 8  # 8
    lightest_weight_for_remove = 17  # 25 - 8
    acceptable_tolerance = 8
    ignored_bits = 0
    is_stable_tolerance = 25

    def __init__(self):
        super().__init__()
        self._startUpHandler = self.noise_reduction_buffer_size
        self.hx = HX711(24, 23)
        for i in range(self.read_weight_buffer_size):
            self.read_weight_buffer.append(0)
        for i in range(self.noise_reduction_buffer_size):
            self.noise_reduction_buffer.append(0)
        with open("/home/aptinet/offset.txt", 'r') as f:
            self.setOffset(float(f.readline()))
        self.hx.set_offset(self._offset)
        with open("/home/aptinet/scale.txt", 'r') as f:
            self.setScale(float(f.readline()))
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
        self._isStable = val
        self.isstable_changed.emit()

    isstable = Property(bool, getisstable, setisstable, notify=isstable_changed)

    def outlierRemover(self, data_list, outlier_margin=1.5):
        a = np.array(data_list)
        upper_quartile = np.percentile(a, 75)
        lower_quartile = np.percentile(a, 25)
        IQR = max(((upper_quartile - lower_quartile) * outlier_margin), 8)
        quartileSet = (lower_quartile - IQR, upper_quartile + IQR)
        resultList = []
        for raw_number in a.tolist():
            if quartileSet[0] <= raw_number <= quartileSet[1]:
                resultList.append(raw_number)
        # print(resultList)
        return int(sum(resultList) / len(resultList)) if len(resultList) > 0 else 0

    def run(self):
        while True:
            result: int = self.hx.get_grams(times=1)

            self.noise_reduction_buffer.pop(0)
            self.noise_reduction_buffer.append(int(result))

            self.setcurrentweight(self.outlierRemover(self.noise_reduction_buffer, 1))

            self.read_weight_buffer.pop(0)
            self.read_weight_buffer.append(self.getcurrentweight())
            if self._startUpHandler > 0:
                self._startUpHandler = self._startUpHandler - 1
            else:
                self.setisstable(True)
                self._canread = True
                for i in range(self.read_weight_buffer_size):
                    for j in range(i, self.read_weight_buffer_size):
                        diff = abs(self.read_weight_buffer[i] - self.read_weight_buffer[j])
                        if diff >= self.is_stable_tolerance:
                            self.setisstable(False)
                            self._canread = False
                            break
                        elif diff >= self.acceptable_tolerance:
                            self._canread = False

                if self._canread:
                    if self._atstartUp == True:
                        self.setstartWeight(mean(self.read_weight_buffer))
                        self._BasketWeight2 = mean(self.read_weight_buffer)
                        self._BasketWeight1 = self._BasketWeight2
                        self._atstartUp = False
                    else:
                        if mean(self.read_weight_buffer) > self._BasketWeight1:
                            a = np.array(self.read_weight_buffer)
                            half_quartile = np.percentile(a, 50)
                            c = 0
                            s = 0
                            for w in self.read_weight_buffer:
                                if w >= half_quartile:
                                    c += 1
                                    s += w
                            self._BasketWeight2 = int(s / c)
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

#### new weight sensor commented ##################################################
# from PySide2.QtCore import QObject, Signal, Property, Slot, QThread
# from Module.hx711 import HX711
# import numpy as np
#
#
# class WeightSensorWorker(QThread):
#
#     _canReadWeight: bool
#     _hx = HX711
#     _offset: float
#     _scale: float
#     _elecNoiseReducBuffer = []
#     _startUpHandler: int
#     _weight: int
#
#     ### Setting ###################
#     _elecNoiseReducBufferSize: int = 20
#
#     def __init__(self):
#         super().__init__()
#
#         self.hx = HX711(24, 23)
#         self._canReadWeight = True
#         with open("/home/aptinet/offset.txt", 'r') as f:
#             self.set_offset(float(f.readline()))
#         self.hx.set_offset(self._offset)
#         with open("/home/aptinet/scale.txt", 'r') as f:
#             self.set_scale(float(f.readline()))
#         self.hx.set_scale(self.scale)
#
#         self._weight = 0
#         self._startUpHandler = 0
#
#     changedSignal = Signal()
#     newWeightSignal = Signal()
#
#     def get_offset(self):
#         return self._offset
#
#     def set_offset(self, v):
#         self._offset = v
#         self.changedSignal.emit()
#
#     offset = Property(float, get_offset, set_offset, notify=changedSignal)
#
#     def get_scale(self):
#         return self._scale
#
#     def set_scale(self, v):
#         self._scale = v
#         self.changedSignal.emit()
#
#     scale = Property(float, get_scale, set_scale, notify=changedSignal)
#
#     def get_weight(self):
#         return self._weight
#
#     def set_weight(self, v: int):
#         self._weight = v
#         self.newWeightSignal.emit()
#
#     weight = Property(int, get_weight, set_weight, notify=newWeightSignal)
#
#     def get_elecNoiseReducBufferSize(self):
#         return self._elecNoiseReducBufferSize
#
#     def set_elecNoiseReducBufferSize(self, v: int):
#         self._elecNoiseReducBufferSize = v
#         self.changedSignal.emit()
#
#     elecNoiseReducBufferSize = Property(int, get_elecNoiseReducBufferSize, set_elecNoiseReducBufferSize,
#                                         notify=changedSignal)
#
#     def outlier_remover(self, data_list, outlier_margin=1.5):
#         a = np.array(data_list)
#         upper_quartile = np.percentile(a, 75)
#         lower_quartile = np.percentile(a, 25)
#         IQR = max(((upper_quartile - lower_quartile) * outlier_margin), 8)
#         quartileSet = (lower_quartile - IQR, upper_quartile + IQR)
#         resultList = []
#         for raw_number in a.tolist():
#             if quartileSet[0] <= raw_number <= quartileSet[1]:
#                 resultList.append(raw_number)
#         return int(sum(resultList) / len(resultList)) if len(resultList) > 0 else 0
#
#     def run(self):
#         while self._canReadWeight:
#             result: int = self.hx.get_grams(times=1)
#
#             if self._startUpHandler < self._elecNoiseReducBufferSize:
#                 self._elecNoiseReducBuffer.append(result)
#                 self._startUpHandler += 1
#             else:
#                 self._elecNoiseReducBuffer.pop(0)
#                 self._elecNoiseReducBuffer.append(result)
#
#                 self.set_weight(self.outlier_remover(self._elecNoiseReducBuffer, 1))
#
#     def stop(self):
#         self._canReadWeight = False
#         del self.hx
