from PyQt5.QtCore import Qt, QRect
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QPen

class Aircraft(QWidget):
    def __init__(self,  parent=None):
        super(Aircraft, self).__init__(parent)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)

        rect = self.rect()

        center_x = self.width() / 2
        center_y = self.height() / 2

        nose_width = 10
        wing_width = self.width() / 6

        nose = QRect(rect.center().x() - nose_width / 2, rect.center().y() - nose_width / 2, nose_width, nose_width)
        left = QRect(center_x - 15 - wing_width, center_y - 5, wing_width, 10)
        right = QRect(center_x + 15, center_y - 5, wing_width, 10)

        qp.setBrush(Qt.yellow)
        qp.drawRect(nose)
        qp.drawRect(left)
        qp.drawRect(right)

        qp.end()
