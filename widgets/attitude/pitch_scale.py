from PyQt5.QtCore import Qt, QRect
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QPen

markers = list(range(-90, 95, 5))

class PitchScale(QWidget):
    angle = 0
    azimuth = 0
    vertical_offset = 0

    def __init__(self,  parent=None):
        super(PitchScale, self).__init__(parent)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)

        azpix = self.parent().geometry().height() / 60.

        qp.translate(self.rect().center())
        qp.rotate(-self.angle)
        qp.translate(-self.rect().center())
        qp.translate(self.rect().center().x(), self.rect().center().y() + (azpix * self.azimuth) + (azpix * self.vertical_offset))

        qp.setPen(Qt.white)

        for marker in markers:
            if marker == 0:
                continue

            x1 = -(self.width() / 10)
            x2 = self.width() / 10
            y = azpix * marker

            if marker % 15 == 0:
                x1 -= 30
                x2 += 30

            qp.drawText(x1 - 20, y + 4, str(abs(marker)))
            qp.drawText(x2 + 10, y + 4, str(abs(marker)))
            qp.drawLine(x1, y, x2, y)

        qp.end()

    def setAhrs(self, _heading, azimuth, angle):
        self.angle = angle
        self.azimuth = azimuth
        self.update()

    def setVerticalOffset(self, vertical_offset):
        self.vertical_offset = vertical_offset
        self.update()
