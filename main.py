import board
import busio
from adafruit_bmp280 import Adafruit_BMP280_I2C
from adafruit_bno055 import BNO055_I2C, CONFIG_MODE, NDOF_MODE

i2c = busio.I2C(board.SCL, board.SDA)
bmp280 = Adafruit_BMP280_I2C(i2c)
bmp280.seaLevelhPa = 1013.25

bno055 = BNO055_I2C(i2c)
bno055.mode = CONFIG_MODE
bno055._write_register(0x42, 0b00000110)
bno055.mode = NDOF_MODE

from PyQt5 import QtCore
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QStackedLayout, QWidget

from widgets.attitude import AttitudeWidget

class Airshow(QWidget):
    def __init__(self, parent=None):
        super(Airshow, self).__init__(parent)

        self.setWindowTitle('Airshow')

        self.attitudeWidget = AttitudeWidget()

        layout = QStackedLayout()
        layout.addWidget(self.attitudeWidget)

        self.setLayout(layout)

        self.timer = QTimer()
        self.timer.setInterval(50)
        self.timer.timeout.connect(self._timeout)
        self.timer.start()

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            self.close()

    def _timeout(self):
        sys, gyro, accel, mag = bno055.calibration_status
        print(sys, gyro, accel, mag)

        heading, roll, pitch = bno055.euler
        print(heading, roll, pitch)

        self.attitudeWidget.angle = roll
        self.attitudeWidget.azimuth = pitch
        self.attitudeWidget.update()

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    airshow = Airshow()
    airshow.setFixedSize(800, 480)
    airshow.show()

    sys.exit(app.exec_())
