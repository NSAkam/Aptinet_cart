# import quick2wire.i2c as i2c
from PySide2.QtCore import QObject, Signal, Property, Slot, QUrl, QThread
import numpy as np
from statistics import mean

import time


class i2c(QObject):
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def I2CMaster(self):
        return self

    def reading(self, address, quantity):
        return [['F0', 'DA']]

    def transaction(self, data):
        # Simulate the transaction by returning the data
        return data



class BatteryWorker(QThread):
    updateLevel = Signal(int)
    buffer = []
    size = 5
    meanbuffer = []
    meansize = 5
    level: int = 100
    in_init: bool = True

    def __init__(self):
        QThread.__init__(self)
        for i in range(self.size):
            self.buffer.append(0)
        for i in range(self.meansize):
            self.meanbuffer.append(0)

    def set_data(self, numbers):
        hight = numbers[0][0]
        low = numbers[0][1]
        # New lines
        hight = int(hight, 16)
        low = int(low, 16)
        # end new lines
        data = hight * 256
        data = data + low
        return data

    # def read_file(self, input):
    #     try:
    #         if input == 'min':
    #             Minfile = open("min.txt", "r")
    #             mindata = int(Minfile.readline())
    #             Minfile.close()
    #             return mindata
    #         elif input == 'max':
    #             Maxfile = open("max.txt", "r")
    #             maxdata = int(Maxfile.readline())
    #             Maxfile.close()
    #             return maxdata
    #     except (ValueError, FileNotFoundError):
    #         raise ValueError("Error: Invalid data in the file or file not found.")

    def read_file(self, input):
        try:
            if input == 'min':
                with open("min.txt", "r") as Minfile:
                    mindata = int(Minfile.readline())
                return mindata
            elif input == 'max':
                with open("max.txt", "r") as Maxfile:
                    maxdata = int(Maxfile.readline())
                return maxdata
        except (ValueError, FileNotFoundError):
            raise ValueError("Error: Invalid data in the file or file not found.")

    # def write_file(self, input, data):
    #     if input == 'min':
    #         Minfile = open("/home/kast/min.txt", "w")
    #         Minfile.write(str(int(data)))
    #         Minfile.close()
    #     elif input == 'max':
    #         Maxfile = open("/home/kast/max.txt", "w")
    #         Maxfile.write(str(int(data)))
    #         Maxfile.close()

    def write_file(self, input, data):
        try:
            if input == 'min':
                Minfile = open("/home/kast/min.txt", "w")
                Minfile.write(str(int(data)))
                Minfile.close()
            elif input == 'max':
                Maxfile = open("/home/kast/max.txt", "w")
                Maxfile.write(str(int(data)))
                Maxfile.close()
            else:
                raise ValueError("Invalid input value. Expected 'min' or 'max'.")
        except FileNotFoundError:
            raise Exception("File not found.")
        except ZeroDivisionError:
            raise Exception("Data cannot be zero.")

    def normalize_data(self, data, min, max):
        try:
            if max - min == 0:
                raise ZeroDivisionError("Data cannot be zero.")
            normalized_data = int(round((data - min) * 100 / (max - min)))
            return normalized_data
        except ZeroDivisionError as e:
            raise Exception(str(e))

    def run(self):
        try:
            counter = 0
            # with i2c as bus:
            with i2c.I2CMaster() as bus:
                while True:
                    results = bus.transaction(i2c.reading(0x48, 2))
                    data = self.set_data(results)

                    self.buffer.pop(0)
                    self.buffer.append(data)

                    res = self.outlierRemover(self.buffer)
                    self.meanbuffer.pop(0)
                    self.meanbuffer.append(res)

                    if mean(self.meanbuffer) <= 0 or counter <= 10:
                        counter = counter + 1
                        # print(counter)
                        # continue

                    else:
                        mindata = self.read_file('min')

                        if mean(self.meanbuffer) < mindata:
                            self.write_file('min', mean(self.meanbuffer))

                        maxdata = self.read_file('max')

                        if mean(self.meanbuffer) > maxdata:
                            self.write_file('max', mean(self.meanbuffer))

                        if self.in_init:
                            # if (mean(self.meanbuffer) != 0):
                            self.in_init = False
                            self.level = self.normalize_data(data=mean(self.meanbuffer),min=mindata, max=maxdata)
                        else:

                            # print(str(mindata) + ">>>>" + str(maxdata) + ">>>>>>>" + str(mean(self.meanbuffer)))
                            # if (mean(self.meanbuffer) != 0):
                            new_level = self.normalize_data(data=mean(self.meanbuffer),min=mindata, max=maxdata)

                            if new_level == (self.level - 1):
                                self.level = new_level

                            elif new_level < (self.level - 1):
                                self.level = self.level - 1

                            elif new_level > (self.level + 4):
                                self.level = self.level + 1

                            self.updateLevel.emit(self.level)
                            # self.level = int(round((mean(self.meanbuffer) - mindata) * 100 / (maxdata - mindata)))
                            # self.updateLevel.emit(self.level)

                        # print(data)
                        # voltage = data * 2.048
                        # voltage = voltage / 32768.0
                        # print(voltage)
                        # self.updateLevel.emit(voltage)
                        if self.level > 100:
                            self.level = 100
                        self.updateLevel.emit(self.level)
                    time.sleep(0.1)
        except:
            pass

    # def outlierRemover(self, data_list, outlier_margin=1.5):
    #     a = np.array(data_list)
    #     upper_quartile = np.percentile(a, 75)
    #     lower_quartile = np.percentile(a, 25)
    #     IQR = (upper_quartile - lower_quartile) * outlier_margin
    #     quartileSet = (lower_quartile - IQR, upper_quartile + IQR)
    #     resultList = []
    #     for raw_number in a.tolist():
    #         if quartileSet[0] <= raw_number <= quartileSet[1]:
    #             resultList.append(raw_number)
    #     # print(resultList)
    #     return int(sum(resultList) / len(resultList)) if len(resultList) > 0 else 0

    def outlierRemover(self, data_list, outlier_margin=1.5):
        a = np.array(data_list)
        upper_quartile = np.percentile(a, 75)
        lower_quartile = np.percentile(a, 25)
        IQR = (upper_quartile - lower_quartile) * outlier_margin
        quartileSet = (lower_quartile - IQR, upper_quartile + IQR)
        resultList = a[(a >= quartileSet[0]) & (a <= quartileSet[1])]
        return int(np.mean(resultList)) if len(resultList) > 0 else 0


class Battery(QObject):
    _level: float = 50
    _threadUpdate: BatteryWorker

    def __init__(self):
        super().__init__()
        self._threadUpdate = BatteryWorker()
        self._threadUpdate.updateLevel.connect(self.updateLevel)
        self._threadUpdate.start()

    @Slot(int)
    def updateLevel(self, v: int):
        self.setLevel(v)

    @Signal
    def changed(self):
        pass

    def getLevel(self):
        return self._level

    def setLevel(self, v):
        self._level = v
        self.changed.emit()

    batterylevel = Property(float, getLevel, setLevel, notify=changed)
