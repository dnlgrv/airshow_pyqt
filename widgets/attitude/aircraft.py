from PyQt5.QtCore import Qt, QPoint, QRect
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QColor, QPainter, QPen, QPolygon

class Aircraft(QWidget):
    def __init__(self,  parent=None):
        super(Aircraft, self).__init__(parent)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)

        center_x = self.width() / 2
        center_y = self.height() / 2

        nose = QRect(center_x - 5, 0, 10, 10)

        left = [
                QPoint(0, 0),
                QPoint(center_x - 15, 0),
                QPoint(center_x - 15, self.height()),
                QPoint(center_x - 20, self.height()),
                QPoint(center_x - 20, 5),
                QPoint(0, 5)
            ]

        right = [
                QPoint(self.width(), 0),
                QPoint(center_x + 15, 0),
                QPoint(center_x + 15, self.height()),
                QPoint(center_x + 20, self.height()),
                QPoint(center_x + 20, 5),
                QPoint(self.width(), 5)
            ]

        qp.setBrush(Qt.yellow)
        qp.drawRect(nose)
        qp.drawPolygon(QPolygon(left))
        qp.drawPolygon(QPolygon(right))

        qp.end()
