from PyQt5.QtCore import Qt, QPoint, QRect, pyqtSlot as Slot
from PyQt5.QtGui import QColor, QPainter, QPen
from PyQt5.QtWidgets import QWidget

from widgets.attitude.aircraft import Aircraft

class AttitudeWidget(QWidget):
    angle = 0
    azimuth = 0

    def __init__(self, ahrs, parent=None):
        super(AttitudeWidget, self).__init__(parent)

        self.ahrs = ahrs
        self.ahrs.changed.connect(self.on_ahrs_changed)

        self.setAutoFillBackground(True)

        p = self.palette()
        p.setColor(self.backgroundRole(), QColor(0, 130, 235))
        self.setPalette(p)

        self.aircraft = Aircraft(self)
        self.aircraft.resize(180, 20)
        self.aircraft.show()

    def paintEvent(self, event):
        self.aircraft.move(self.width() / 2 - 90, self.height() / 2 - 5)

        qp = QPainter()
        qp.begin(self)

        azpix = self.height() / 60.

        qp.translate(self.width() / 2, (self.height() / 2) + (azpix * self.azimuth))
        qp.rotate(-self.angle)

        ground = QRect(-2 * (self.width() / 2), 0, 2 * self.width(), 2 * self.height())

        qp.setPen(Qt.NoPen)
        qp.setBrush(QColor(170, 90, 85))
        qp.drawRect(ground)

        l1 = QPoint(-(self.width() / 10), 0)
        r1 = QPoint((self.width() / 10), 0)

        qp.setBrush(Qt.black)
        pen = QPen()
        pen.setColor(Qt.black)
        pen.setWidth(self.height() / 200)
        pen.setStyle(Qt.SolidLine)
        qp.setPen(pen)

        qp.end()

    @Slot(float, float, float)
    def on_ahrs_changed(self, heading, pitch, roll):
        self.angle = roll
        self.azimuth = pitch
        self.update()
