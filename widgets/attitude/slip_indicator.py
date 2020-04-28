from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QColor, QPainter, QBrush, QPen
from PyQt5.QtWidgets import QWidget

class SlipIndicator(QWidget):
    slip = 0

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)

        qp.setPen(Qt.NoPen)

        width = self.width() / 3
        height = self.height() / 5
        tlx = (self.width() / 2) - (width / 2)
        tly = (self.height() / 2) - (height / 2)

        brush = QBrush(Qt.SolidPattern)
        brush.setColor(QColor(0, 0, 0, 50))
        qp.setBrush(brush)

        box = QRect(tlx, tly, width, height)
        qp.drawRect(box)

        brush.setColor(QColor(255, 255, 255, 100))
        qp.setBrush(brush)

        qp.translate(-self.slip * width / 2, 0)
        ball = QRect(tlx + (width / 2) - (height / 2), tly, height, height)
        qp.drawEllipse(ball)

        qp.end()

    def setAhrs(self, slip):
        self.slip = slip
        self.update()
