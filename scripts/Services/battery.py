import time
import numpy as np
import smbus
from PySide2.QtCore import Signal, QThread
from PySide2.QtCore import QObject, Signal, Property, Slot, QUrl, QThread



class BatteryWorker(QThread):
    _level: int = 50
    _batteryLevel: int = 50
    _elecNoiseReducBufferSize: int
    _noiseReductionBufferSize: int
    _elecNoiseReducBuffer = []
    _noiseReductionBuffer = []
    _minElecNumber: int
    _maxElecNumber: int
    _i2cBus: smbus
    _devAddress: int
    _canReadLevel: bool
    _initialElecNoiseReduceBuffer: int = 0
    _initialNoiseReduceBuffer: int = 0

    def __init__(self):
        super().__init__()
        self._i2cBus = smbus.SMBus(1)
        self._devAddress = 0x4d

        self._elecNoiseReducBufferSize = 200
        self._noiseReductionBufferSize = 200

        self._minElecNumber = 4096  # MCP3221 maximum electrical number
        self._maxElecNumber = 0  # MCP3221 minimum electrical number

        with open("/home/aptinet/min.txt", 'r') as f:
            minimum = int(float(f.readline()))
            if minimum < self._minElecNumber:
                self._minElecNumber = minimum
        with open("/home/aptinet/max.txt", 'r') as f:
            maximum = int(float(f.readline()))
            if maximum > self._maxElecNumber:
                self._maxElecNumber = maximum

        self._canReadLevel = True

    newLevelSignal = Signal(int)
    stopChargingSignal = Signal()
    chargingSignal = Signal()
    showBatterySignal = Signal()


    def get_level(self):
        return self._level

    def set_level(self, v: int):
        if v < 0:
            self._level = 0
        elif v > 100:
            self._level = 100
        else:
            self._level = v

    def get_batteryLevel(self):
        return self._batteryLevel

    def set_batteryLevel(self, v: int):
        if v < 1:
            self._batteryLevel = 1
        elif v > 100:
            self._batteryLevel = 100
        else:
            self._batteryLevel = v

    def run(self):
        try:
            self._initialElecNoiseReduceBuffer: int = 0
            while self._canReadLevel:
                if self._initialElecNoiseReduceBuffer < self._elecNoiseReducBufferSize:
                    readBytes = self._i2cBus.read_i2c_block_data(self._devAddress, 0x00, 2)
                    res = (readBytes[0] << 8) + readBytes[1]
                    self._elecNoiseReducBuffer.append(res)
                    self._initialElecNoiseReduceBuffer += 1
                else:
                    self._elecNoiseReducBuffer.pop(0)
                    readBytes = self._i2cBus.read_i2c_block_data(self._devAddress, 0x00, 2)
                    res = (readBytes[0] << 8) + readBytes[1]
                    self._elecNoiseReducBuffer.append(res)
                    elecNumber = self.outlierRemover(self._elecNoiseReducBuffer)

                    if elecNumber < self._minElecNumber:
                        self.save_minElecNumber(elecNumber)
                    if elecNumber > self._maxElecNumber:
                        self.save_maxElecNumber(elecNumber)

                    x = int(((elecNumber - self._minElecNumber) / (self._maxElecNumber - self._minElecNumber)) * 100)
                    self.set_level(int((x - 30) / 65 * 100))
                    self.new_levelRead(self._level)
                    time.sleep(0.01)
        except:
            pass


    def new_levelRead(self, level: int):
        if self._initialNoiseReduceBuffer < self._noiseReductionBufferSize:
            self._noiseReductionBuffer.append(level)
            self._initialNoiseReduceBuffer += 1

        elif self._initialNoiseReduceBuffer == self._noiseReductionBufferSize:
            self._noiseReductionBuffer.pop(0)
            self._noiseReductionBuffer.append(level)
            self.set_batteryLevel(int(self.outlierRemover(self._noiseReductionBuffer)))
            self.newLevelSignal.emit(self._batteryLevel)
            self.showBatterySignal.emit()
            self._initialNoiseReduceBuffer += 1

        else:
            self._noiseReductionBuffer.pop(0)
            self._noiseReductionBuffer.append(level)

            newLevel = self.outlierRemover(self._noiseReductionBuffer, outlier_margin=1)
            if newLevel < self._batteryLevel:
                canChange = True
                for level in self._noiseReductionBuffer:
                    if self._batteryLevel < level:
                        canChange = False
                if canChange:
                    self.stopChargingSignal.emit()
                    self.set_batteryLevel(self._batteryLevel - 1)
                    self.newLevelSignal.emit(self._batteryLevel)

            elif newLevel > self._batteryLevel:
                canChange = True
                for level in self._noiseReductionBuffer:
                    if level < self._batteryLevel:
                        canChange = False
                if canChange:
                    self.chargingSignal.emit()
                    self.set_batteryLevel(self._batteryLevel + 1)


    def save_minElecNumber(self, v: int):
        self._minElecNumber = v
        with open("/home/aptinet/min.txt", 'w') as f:
            f.write(str(v))

    def save_maxElecNumber(self, v: int):
        self._maxElecNumber = v
        with open("/home/aptinet/max.txt", 'w') as f:
            f.write(str(v))

    def outlierRemover(self, data_list, outlier_margin=1.5):
        a = np.array(data_list)
        upper_quartile = np.percentile(a, 75)
        lower_quartile = np.percentile(a, 25)
        IQR = (upper_quartile - lower_quartile) * outlier_margin
        quartileSet = (lower_quartile - IQR, upper_quartile + IQR)
        resultList = []
        for raw_number in a.tolist():
            if quartileSet[0] <= raw_number <= quartileSet[1]:
                resultList.append(raw_number)
        # print(resultList)
        return int(sum(resultList) / len(resultList)) if len(resultList) > 0 else 0

    def stop(self):
        self._canReadLevel = False


# class BatteryWorker2(QThread):
#     updateLevel = Signal(int)
#     buffer = []
#     size = 5
#     meanbuffer = []
#     meansize = 5
#     level: int = 100
#     in_init: bool = True
#
#     def __init__(self):
#         QThread.__init__(self)
#         for i in range(self.size):
#             self.buffer.append(0)
#         for i in range(self.meansize):
#             self.meanbuffer.append(0)
#
#     def run(self):
#         try:
#             counter = 0
#             with i2c.I2CMaster() as bus:
#                 while True:
#                     results = bus.transaction(i2c.reading(0x48, 2))
#                     hight = results[0][0]
#                     low = results[0][1]
#
#                     data = hight * 256
#                     data = data + low
#                     self.buffer.pop(0)
#                     self.buffer.append(data)
#                     res = self.outlierRemover(self.buffer)
#                     self.meanbuffer.pop(0)
#                     self.meanbuffer.append(res)
#                     if (mean(self.meanbuffer) <= 0 or counter <= 10):
#                         counter = counter + 1
#                         # print(counter)
#                         # continue
#                     else:
#                         Minfile = open("/home/kast/min.txt", "r")
#                         mindata = int(Minfile.readline())
#                         Minfile.close()
#
#                         if mean(self.meanbuffer) < mindata:
#                             Minfile = open("/home/kast/min.txt", "w")
#                             Minfile.write(str(int(mean(self.meanbuffer))))
#                             Minfile.close()
#
#                         Maxfile = open("/home/kast/max.txt", "r")
#                         maxdata = int(Maxfile.readline())
#                         Maxfile.close()
#                         if mean(self.meanbuffer) > maxdata:
#                             Maxfile = open("/home/kast/max.txt", "w")
#                             Maxfile.write(str(int(mean(self.meanbuffer))))
#                             Maxfile.close()
#
#                         if self.in_init:
#                             # if (mean(self.meanbuffer) != 0):
#                             self.in_init = False
#                             self.level = int(round((mean(self.meanbuffer) - mindata) * 100 / (maxdata - mindata)))
#                         else:
#
#                             # print(str(mindata) + ">>>>" + str(maxdata) + ">>>>>>>" + str(mean(self.meanbuffer)))
#                             # if (mean(self.meanbuffer) != 0):
#                             new_level = int(round((mean(self.meanbuffer) - mindata) * 100 / (maxdata - mindata)))
#                             if new_level == (self.level - 1):
#                                 self.level = new_level
#                                 self.updateLevel.emit(self.level)
#                             elif new_level < (self.level - 1):
#                                 self.level = self.level - 1
#                                 self.updateLevel.emit(self.level)
#                             elif new_level > (self.level + 4):
#                                 self.level = self.level + 1
#                                 self.updateLevel.emit(self.level)
#                             # self.level = int(round((mean(self.meanbuffer) - mindata) * 100 / (maxdata - mindata)))
#                             # self.updateLevel.emit(self.level)
#
#                         # print(data)
#                         # voltage = data * 2.048
#                         # voltage = voltage / 32768.0
#                         # print(voltage)
#                         # self.updateLevel.emit(voltage)
#                         if self.level > 100:
#                             self.level = 100
#                         self.updateLevel.emit(self.level)
#                     time.sleep(0.1)
#         except:
#             pass
#
#     def outlierRemover(self, data_list, outlier_margin=1.5):
#         a = np.array(data_list)
#         upper_quartile = np.percentile(a, 75)
#         lower_quartile = np.percentile(a, 25)
#         IQR = (upper_quartile - lower_quartile) * outlier_margin
#         quartileSet = (lower_quartile - IQR, upper_quartile + IQR)
#         resultList = []
#         for raw_number in a.tolist():
#             if quartileSet[0] <= raw_number <= quartileSet[1]:
#                 resultList.append(raw_number)
#         # print(resultList)
#         return int(sum(resultList) / len(resultList)) if len(resultList) > 0 else 0
#
# #
# class Battery(QObject):
#     _level: float = 50
#     _threadUpdate: BatteryWorker
#
#     def __init__(self):
#         super().__init__()
#         self._threadUpdate = BatteryWorker()
#         self._threadUpdate.newLevelSignal.connect(self.updateLevel)
#         self._threadUpdate.start()
#
#     @Slot(int)
#     def updateLevel(self, v: int):
#         self.setLevel(v)
#
#     @Signal
#     def changed(self):
#         pass
#
#     def getLevel(self):
#         return self._level
#
#     def setLevel(self, v):
#         self._level = v
#         self.changed.emit()
#
#     batterylevel = Property(float, getLevel, setLevel, notify=changed)
