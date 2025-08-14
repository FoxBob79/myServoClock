# servo.py
# Kevin McAleer
# March 2021

from pca9685_b2 import PCA9685B2
import math


class ServosB2:
    def __init__(self, i2c, address=0x41, freq=50, min_us=600, max_us=2400,   ### address 0x40 for board 1, 0x41 for board 2, etc ###
                 degrees=180):
        self.period = 1000000 / freq
        self.min_duty = self._us2duty(min_us)
        self.max_duty = self._us2duty(max_us)
        self.degrees = degrees
        self.freq = freq
        self.pca9685_b2 = PCA9685B2(i2c, address)
        self.pca9685_b2.freq(freq)

    def _us2duty(self, value):
        return int(4095 * value / self.period)

    def position(self, index, degrees=None, radians=None, us=None, duty=None):
        span = self.max_duty - self.min_duty
        if degrees is not None:
            duty = self.min_duty + span * degrees / self.degrees
        elif radians is not None:
            duty = self.min_duty + span * radians / math.radians(self.degrees)
        elif us is not None:
            duty = self._us2duty(us)
        elif duty is not None:
            pass
        else:
            return self.pca9685_b2.duty(index)
        duty = min(self.max_duty, max(self.min_duty, int(duty)))
        self.pca9685_b2.duty(index, duty)

    def release(self, index):
        self.pca9685_b2.duty(index, 20)