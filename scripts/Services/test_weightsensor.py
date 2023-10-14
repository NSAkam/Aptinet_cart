from PySide2.QtCore import QObject, Signal, Property, Slot,QThread
from Module.hx711 import HX711
import numpy as np
from time import sleep
from statistics import mean
from copy import copy


class WeightSensorWorker(QThread):
    
    _offset: float
    _scale: float
    
    def __init__(self):
        super().__init__()
        self._startWeight: int = 0 
        self._BasketWeight1: int = 0
        self._BasketWeight2: int = 0
        self._currentWeight: int = 0
        self._tolerance: float = 25
        self._basketweight = 0
        self._canread = False
        self._atstartUp = True
        self._startUpHandler = 0
        self._isStable: bool = False
        self.noise_reduction_buffer_size = 20
        self.noise_reduction_buffer = []
        self.last_weight = 0
        self.read_weight_buffer_size = 20 # buffer size for shifting weights to it
        self.read_weight_buffer = [] #buffer for shifting weights to it
        self.lightest_weight = 25  # 8
        self.lightest_weight_for_remove = 17  # 25 - 8
        self.acceptable_tolerance = 8
        self.ignored_bits = 0
        self.is_stable_tolerance = 25
        self._startUpHandler = self.noise_reduction_buffer_size
            