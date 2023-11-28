import RPi.GPIO as GPIO
from PySide2.QtCore import QThread


class GreenLight(QThread):
    _active: bool
    _gpioNumber: int = 5   # or 6

    def __init__(self, active: bool):
        QThread.__init__(self)
        self._active = active

    def run(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self._gpioNumber, GPIO.OUT)
        if self._active:
            GPIO.output(self._gpioNumber, GPIO.HIGH)
        else:
            GPIO.output(self._gpioNumber, GPIO.LOW)


class Fan:
    _gpioNumber: int = 17

    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self._gpioNumber, GPIO.OUT)

    def turn_onFan(self):
        GPIO.output(self._gpioNumber, GPIO.HIGH)

    def turn_offFan(self):
        GPIO.output(self._gpioNumber, GPIO.LOW)

