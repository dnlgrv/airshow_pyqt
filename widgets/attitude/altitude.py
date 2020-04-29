import math
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QColor, QPainter, QPen

class Altitude(QWidget):
    altitude = 0
    pressure = 1013

    qnh = 1013
    unit = 'hPa'

    def __init__(self, qnh, parent=None):
        super(Altitude, self).__init__(parent)
        self.qnh = qnh
        self._update_altitude()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)

        height = self.rect().height() * 0.7
        width = self.rect().width() * 0.6
        tlx = (self.rect().width() / 2) - (width / 2)
        tly = (self.rect().height() / 2) - (height / 2)

        container = QRect(tlx, tly, width, height)

        qp.setPen(Qt.white)
        qp.drawRect(container)

        qp.setBrush(QColor(0, 0, 0, 50))

        header = QRect(tlx, tly, width, 30)
        qp.drawRect(header)

        footer = QRect(tlx, tly + height - 30, width, 30)
        qp.drawRect(footer)

        qp.setPen(Qt.cyan)
        qp.drawText(header, Qt.AlignCenter, str(self.altitude))
        qp.drawText(footer, Qt.AlignCenter, '{} {}'.format(self.qnh, self.unit))

        qp.end()

    def setQNH(self, qnh):
        self.qnh = qnh
        self._update_altitude()
        self.update()

    def _update_altitude(self):
        # to be replaced with calculation from sensor library
        self.altitude = math.ceil(44330.0 * (1.0 - math.pow(self.pressure / self.qnh, (1.0 / 5.255))))
