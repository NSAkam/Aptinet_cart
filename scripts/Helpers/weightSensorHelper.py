from statistics import mean
import numpy as np
from PySide2.QtCore import QObject, Signal, Property, Slot
from Services.weightsensor import WeightSensorWorker


class WeightSensorHelper(QObject):

    _weighSensorWorker: WeightSensorWorker
    _mecNoiseReducBuffer = []
    _startWeight: int
    _atStartUp: bool = True
    _canRead: bool = True
    _basketWeight1: int = 0
    _basketWeight2: int = 0
    _basketWeight: int = 0
    _momentoBasketWeight: int = 0
    _lightestWeightForRemove: int
    _lightestWeighRegister: int

    ### Setting ###################
    _elecNoiseReducBufferSize: int = 20
    _mecNoiseReducBufferSize: int = 20
    _loadCellTolerance: int = 8
    _lightestWeight: int = 25

    def __init__(self):
        super().__init__()

        self._weighSensorWorker = WeightSensorWorker()
        self._weighSensorWorker.newWeightSignal.connect(self.new_weight)
        self.start()

        for i in range(self._mecNoiseReducBufferSize):
            self._mecNoiseReducBuffer.append(0)

        self._lightestWeightForRemove = self._lightestWeight - self._loadCellTolerance
        self._lightestWeighRegister = self._lightestWeight

    changedSignal = Signal()
    startWeightSignal = Signal(int)
    stepBasketWeightChangedSignal = Signal(int, int)
    momentoBasketWeightChangedSignal = Signal(int)
    basketWeightChangedSignal = Signal(int)

    def get_startWeight(self):
        return self._startWeight

    def set_startWeight(self, v: int):
        self._startWeight = v
        self.startWeightSignal.emit(v)

    startWeight = Property(int, get_startWeight, set_startWeight, notify=startWeightSignal)

    def get_basketWeight(self):
        return self._basketWeight

    def set_basketWeight(self, v: int):
        self._basketWeight = v
        self.basketWeightChangedSignal.emit(v)

    basketWeight = Property(int, get_basketWeight, set_basketWeight, notify=basketWeightChangedSignal)

    def get_momentoBasketWeight(self):
        return self._momentoBasketWeight

    def set_momentoBasketWeight(self, v: int):
        self._momentoBasketWeight = v
        self.momentoBasketWeightChangedSignal(v)

    momentoBasketWeight = Property(int, get_momentoBasketWeight, set_momentoBasketWeight, notify=momentoBasketWeightChangedSignal)

    def get_elecNoiseReducBufferSize(self):
        return self._weighSensorWorker.get_elecNoiseReducBufferSize()

    def set_elecNoiseReducBufferSize(self, v: int):
        self._weighSensorWorker.set_elecNoiseReducBufferSize(v)
        self.changedSignal.emit()

    elecNoiseReducBufferSize = Property(int, get_elecNoiseReducBufferSize, set_elecNoiseReducBufferSize, notify=changedSignal)

    def get_mecNoiseReducBufferSize(self):
        return self._mecNoiseReducBufferSize

    def set_mecNoiseReducBufferSize(self, v: int):
        self._mecNoiseReducBufferSize = v
        self.changedSignal.emit()

    mecNoiseReducBufferSize = Property(int, get_mecNoiseReducBufferSize, set_mecNoiseReducBufferSize, notify=changedSignal)

    def get_loadCellTolerance(self):
        return self._loadCellTolerance

    def set_loadCellTolerance(self, v: int):
        self._loadCellTolerance = v
        self.changedSignal.emit()

    loadCellTolerance = Property(int, get_loadCellTolerance, set_loadCellTolerance, notify=changedSignal)

    def get_lightestWeight(self):
        return self._lightestWeight

    def set_lightestWeight(self, v: int):
        if v == 0:
            self._lightestWeight = self._lightestWeighRegister
        else:
            self._lightestWeight = v
        self.changedSignal.emit()

    lightestWeight = Property(int, get_lightestWeight, set_lightestWeight, notify=changedSignal)

    @Slot()
    def new_weight(self):
        self._mecNoiseReducBuffer.pop(0)
        self._mecNoiseReducBuffer.append(self._weighSensorWorker.get_weight())

        self.set_momentoBasketWeight(self._weighSensorWorker.outlier_remover(self._mecNoiseReducBuffer))

        self._canRead = True
        for i in range(self._mecNoiseReducBufferSize):
            for j in range(i+1, self._mecNoiseReducBufferSize):
                diff = abs(self._mecNoiseReducBuffer[i] - self._mecNoiseReducBuffer[j])
                if diff > self._loadCellTolerance:
                    self._canRead = False

        if self._canRead:
            if self._atStartUp:
                self.set_startWeight(int(mean(self._mecNoiseReducBuffer)))
                self._basketWeight1 = self._startWeight
                self._basketWeight2 = self._startWeight
                self._atStartUp = False
            else:
                if mean(self._mecNoiseReducBuffer) > self._basketWeight1:
                    a = np.array(self._mecNoiseReducBuffer)
                    half_quartile = np.percentile(a, 50)
                    c = 0
                    s = 0
                    for w in self._mecNoiseReducBuffer:
                        if w >= half_quartile:
                            c += 1
                            s += w
                    self._basketWeight2 = int(s / c)
                else:
                    self._basketWeight2 = int(mean(self._mecNoiseReducBuffer))

                if (self._basketWeight2 - self._basketWeight1) >= self.lightest_weight or (
                        self._basketWeight2 - self._basketWeight1) <= (
                        -1 * min(self.lightest_weight, self.lightest_weight_for_remove)):
                    self.stepBasketWeightChangedSignal.emit(self._basketWeight2, self._basketWeight1)
                    self.set_basketWeight(self._basketWeight2)
                self._basketWeight1 = self._basketWeight2

    def start(self):
        self._weighSensorWorker.start()

    def stop(self):
        self._weighSensorWorker.stop()
