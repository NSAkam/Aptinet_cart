from Services.battery import BatteryWorker
from PySide2.QtCore import QObject, Signal, Property, Slot
from statistics import mean


class BatteryHelper(QObject):
    _batteryWorker: BatteryWorker
    _batteryLevel: int
    _noiseReductionBuffer = []
    _inStartUp: int

    ### Setting ###################
    _noiseReductionBufferSize: int = 15

    def __init__(self):
        super().__init__()
        self._batteryWorker = BatteryWorker()
        self._batteryWorker.newLevelSignal.connect(self.new_levelRead)
        self.set_batteryLevel(50)
        self._inStartUp = 0

    batteryLevelChangedSignal = Signal()
    chargingSignal = Signal()
    stopChargingSignal = Signal()

    def get_batteryLevel(self):
        return self._level

    def set_batteryLevel(self, v: int):
        self._batteryLevel = v
        self.batteryLevelChangedSignal.emit()

    batteryLevel = Property(int, get_batteryLevel, set_batteryLevel, notify=batteryLevelChangedSignal)

    @Slot()
    def new_levelRead(self):
        if self._inStartUp < self._noiseReductionBufferSize:
            self._noiseReductionBuffer.append(self._batteryWorker.get_level())
            self._inStartUp += 1

        elif self._inStartUp == self._noiseReductionBufferSize:
            self._noiseReductionBuffer.pop(0)
            self._noiseReductionBuffer.append(self._batteryWorker.get_level())
            self.set_batteryLevel(int(mean(self._noiseReductionBuffer)))
            self._inStartUp += 1

        else:
            self._noiseReductionBuffer.pop(0)
            self._noiseReductionBuffer.append(self._batteryWorker.get_level())

            newLevel = self._batteryWorker.outlierRemover(self._noiseReductionBuffer, outlier_margin=1)
            if newLevel < self._batteryLevel:
                canChange = True
                for level in self._noiseReductionBuffer:
                    if self._batteryLevel < level:
                        canChange = False
                if canChange:
                    self.stopChargingSignal.emit()
                    self.set_batteryLevel(self._batteryLevel - 1)

            elif newLevel > self._batteryLevel:
                canChange = True
                for level in self._noiseReductionBuffer:
                    if level < self._batteryLevel:
                        canChange = False
                if canChange:
                    self.chargingSignal.emit()

    def start(self):
        self._batteryWorker.start()

    def stop(self):
        self._batteryWorker.stop()

