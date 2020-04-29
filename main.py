# import board
# import busio
# from adafruit_bmp280 import Adafruit_BMP280_I2C
# from adafruit_bno055 import BNO055_I2C, CONFIG_MODE, NDOF_MODE

# i2c = busio.I2C(board.SCL, board.SDA)
# bmp280 = Adafruit_BMP280_I2C(i2c)
# bmp280.seaLevelhPa = 1013.25

# bno055 = BNO055_I2C(i2c)
# bno055.mode = CONFIG_MODE
# bno055._write_register(0x42, 0b00000110)
# bno055.mode = NDOF_MODE

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QStackedLayout, QWidget

from widgets.attitude import AttitudeWidget

import ahrs
import settings

class Airshow(QWidget):
    def __init__(self, parent=None):
        super(Airshow, self).__init__(parent)

        self.setWindowTitle('Airshow')
        self.settings = settings.Settings()

        self.ahrs = ahrs.AHRS()
        self.ahrs.listen()

        self.attitudeWidget = AttitudeWidget(self.ahrs, self.settings)

        layout = QStackedLayout()
        layout.addWidget(self.attitudeWidget)

        self.setLayout(layout)

    def keyReleaseEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()
        elif event.key() == Qt.Key_Up:
            self.settings.increase_qnh()
            # self.settings.inrease_vertical_offset()
        elif event.key() == Qt.Key_Down:
            self.settings.decrease_qnh()
            # self.settings.decrease_vertical_offset()

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    airshow = Airshow()
    airshow.setFixedSize(800, 480)
    airshow.show()

    sys.exit(app.exec_())
