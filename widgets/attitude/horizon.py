from PyQt5.QtCore import Qt, QPoint, QRect
from PyQt5.QtGui import QColor, QPainter, QPen
from PyQt5.QtWidgets import QWidget

class Horizon(QWidget):
    angle = 0
    azimuth = 0

    def __init__(self, parent=None):
        super(Horizon, self).__init__(parent)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)

        azpix = self.parent().geometry().height() / 60.

        qp.translate(self.width() / 2, (self.height() / 2) + (azpix * self.azimuth))
        qp.rotate(-self.angle)

        ground = QRect(-2 * (self.width() / 2), 0, 2 * self.width(), 2 * self.height())
        sky = QRect(-2 * (self.width() / 2), -2 * (self.height() / 2), 2 * self.width(), 2 * (self.height() / 2))

        qp.setPen(Qt.NoPen)

        qp.setBrush(QColor(170, 90, 85))
        qp.drawRect(ground)

        qp.setBrush(QColor(0, 130, 235))
        qp.drawRect(sky)

        qp.end()

    def setAhrs(self, _heading, azimuth, angle):
        self.angle = angle
        self.azimuth = azimuth
        self.update()
