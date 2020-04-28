import math
from PyQt5.QtCore import Qt, QPoint, QRect
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QPen, QPolygon

notches = [-60, -45, -30, -20, -10, 0, 10, 20, 30, 45, 60]

class RollDial(QWidget):
    angle = 0

    def __init__(self,  parent=None):
        super(RollDial, self).__init__(parent)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        qp.setClipping(False)

        qp.translate(self.width() / 2, (self.height() / 2))
        qp.rotate(-self.angle)
        qp.translate(-(self.width() / 2), -((self.height() / 2)))

        inner_rect = QRect(self.rect().x(), 20, self.rect().width(), self.rect().width())

        # qp.setPen(Qt.red)
        # qp.drawRect(self.rect())
        # qp.setPen(Qt.green)
        # qp.drawRect(inner_rect)
        # qp.drawEllipse(inner_rect)

        origin = inner_rect.center()
        j = origin.x()
        k = origin.y()
        r = inner_rect.width() / 2

        startAngle = 31 * 16
        spanAngle = 119 * 16

        pen = QPen()
        pen.setColor(Qt.white)
        pen.setWidth(2)
        qp.setPen(pen)

        qp.drawArc(inner_rect.adjusted(20, 20, -20, -20), startAngle, spanAngle)

        for notch in notches:
            angle = 270 + notch

            if notch in [0, -30, 30, -60, 60]:
                x1 = r * math.cos(math.radians(angle)) + j
                y1 = r * math.sin(math.radians(angle)) + k
                x2 = (r - 20) * math.cos(math.radians(angle)) + j
                y2 = (r - 20) * math.sin(math.radians(angle)) + k
            else:
                x1 = (r - 10) * math.cos(math.radians(angle)) + j
                y1 = (r - 10) * math.sin(math.radians(angle)) + k
                x2 = (r - 20) * math.cos(math.radians(angle)) + j
                y2 = (r - 20) * math.sin(math.radians(angle)) + k

            qp.drawLine(x1, y1, x2, y2)

        qp.translate(self.width() / 2, (self.height() / 2))
        qp.rotate(self.angle)
        qp.translate(-(self.width() / 2), -((self.height() / 2)))

        qp.setBrush(Qt.yellow)
        qp.setPen(QPen())

        points = [
                QPoint(self.rect().center().x(), inner_rect.y() + 25),
                QPoint(self.rect().center().x() + 10, inner_rect.y() + 35),
                QPoint(self.rect().center().x() - 10, inner_rect.y() + 35),
                ]
        qp.drawPolygon(QPolygon(points))

        qp.end()

    def setAhrs(self, _heading, _pitch, angle):
        self.angle = angle
        self.update()
