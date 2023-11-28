from PySide2.QtCore import QObject, Signal, Property, Slot, QThread
from Module.hx711 import HX711
import numpy as np


class WeightSensorWorker(QThread):

    _canReadWeight: bool
    _hx = HX711
    _offset: float
    _scale: float
    _elecNoiseReducBuffer = []
    _startUpHandler: int
    _weight: int

    ### Setting ###################
    _elecNoiseReducBufferSize: int = 20

    def __init__(self):
        super().__init__()

        self.hx = HX711(24, 23)
        self._canReadWeight = True
        with open("/home/aptinet/offset.txt", 'r') as f:
            self.set_offset(float(f.readline()))
        self.hx.set_offset(self._offset)
        with open("/home/aptinet/scale.txt", 'r') as f:
            self.set_scale(float(f.readline()))
        self.hx.set_scale(self.scale)

        self._weight = 0
        self._startUpHandler = 0

    changedSignal = Signal()
    newWeightSignal = Signal()

    def get_offset(self):
        return self._offset

    def set_offset(self, v):
        self._offset = v
        self.changedSignal.emit()

    offset = Property(float, get_offset, set_offset, notify=changedSignal)

    def get_scale(self):
        return self._scale

    def set_scale(self, v):
        self._scale = v
        self.changedSignal.emit()

    scale = Property(float, get_scale, set_scale, notify=changedSignal)

    def get_weight(self):
        return self._weight

    def set_weight(self, v: int):
        self._weight = v
        self.newWeightSignal.emit()

    weight = Property(int, get_weight, set_weight, notify=newWeightSignal)

    def get_elecNoiseReducBufferSize(self):
        return self._elecNoiseReducBufferSize

    def set_elecNoiseReducBufferSize(self, v: int):
        self._elecNoiseReducBufferSize = v
        self.changedSignal.emit()

    elecNoiseReducBufferSize = Property(int, get_elecNoiseReducBufferSize, set_elecNoiseReducBufferSize,
                                        notify=changedSignal)

    def outlier_remover(self, data_list, outlier_margin=1.5):
        a = np.array(data_list)
        upper_quartile = np.percentile(a, 75)
        lower_quartile = np.percentile(a, 25)
        IQR = max(((upper_quartile - lower_quartile) * outlier_margin), 8)
        quartileSet = (lower_quartile - IQR, upper_quartile + IQR)
        resultList = []
        for raw_number in a.tolist():
            if quartileSet[0] <= raw_number <= quartileSet[1]:
                resultList.append(raw_number)
        return int(sum(resultList) / len(resultList)) if len(resultList) > 0 else 0

    def run(self):
        while self._canReadWeight:
            result: int = self.hx.get_grams(times=1)

            if self._startUpHandler < self._elecNoiseReducBufferSize:
                self._elecNoiseReducBuffer.append(result)
                self._startUpHandler += 1
            else:
                self._elecNoiseReducBuffer.pop(0)
                self._elecNoiseReducBuffer.append(result)

                self.set_weight(self.outlier_remover(self._elecNoiseReducBuffer, 1))

    def stop(self):
        self._canReadWeight = False
        del self.hx
