from PyQt5.QtCore import Qt, QRect
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QPen

class RollDial(QWidget):
    angle = 0

    def __init__(self,  parent=None):
        super(RollDial, self).__init__(parent)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)

        qp.translate(self.width() / 2, (self.height() / 2))
        qp.rotate(-self.angle)
        qp.translate(-(self.width() / 2), -((self.height() / 2)))

        inner_rect = QRect(self.width() / 2 - (self.height() / 2 ), 0, self.height(), self.height())

        qp.setPen(Qt.white)

        startAngle = 30 * 16
        spanAngle = 120 * 16
        qp.drawArc(inner_rect, startAngle, spanAngle)

        qp.end()

    def setAhrs(self, _heading, _pitch, angle):
        self.angle = angle
        self.update()
