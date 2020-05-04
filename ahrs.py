import math
import time
from PyQt5.QtCore import QObject, QTimer, pyqtSignal as Signal

class AHRS(QObject):
    changed = Signal()

    heading = 0
    pitch = 0
    roll = 0
    slip = 0

    simulated = False

    def __init__(self):
        super(AHRS, self).__init__()

        try:
            import board
            import busio
            from adafruit_bmp280 import Adafruit_BMP280_I2C
            from adafruit_bno055 import BNO055_I2C, CONFIG_MODE, NDOF_MODE
            i2c = busio.I2C(board.SCL, board.SDA)
            self.axis_sensor = BNO055_I2C(i2c)
        except NotImplementedError:
            self.simulated = True

    def listen(self):
        self.start_time = time.time()

        self.timer = QTimer()
        self.timer.setInterval(10)
        self.timer.timeout.connect(self._timeout)
        self.timer.start()

    def _timeout(self):
        if self.simulated:
            time_now = time.time()
            time_elapsed = time_now - self.start_time

            self.heading = (math.sin(time_elapsed) * 180) % 359
            self.pitch = math.cos(time_elapsed) * 10
            self.roll = math.sin(time_elapsed) * 20

            self.slip = math.cos(time_elapsed) * 1
        else:
            heading, pitch, roll = self.axis_sensor.euler

            self.heading = heading
            self.pitch = pitch
            self.roll = roll

        self.changed.emit()
