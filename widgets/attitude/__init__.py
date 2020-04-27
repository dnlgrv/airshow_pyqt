from PyQt5.QtCore import Qt, pyqtSlot as Slot
from PyQt5.QtWidgets import QGridLayout, QWidget

from widgets.attitude.aircraft import Aircraft
from widgets.attitude.horizon import Horizon
from widgets.attitude.roll_dial import RollDial

class AttitudeWidget(QWidget):
    def __init__(self, ahrs, parent=None):
        super(AttitudeWidget, self).__init__(parent)

        self.ahrs = ahrs
        self.ahrs.changed.connect(self.on_ahrs_changed)

        self.horizon = Horizon(self)
        self.aircraft = Aircraft(self)
        self.roll_dial = RollDial(self)

        layout = QGridLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        layout.setColumnStretch(0, 1)
        layout.setColumnStretch(1, 3)
        layout.setColumnStretch(2, 1)
        layout.setRowStretch(0, 1)
        layout.setRowStretch(1, 1)
        layout.setRowStretch(2, 3)
        layout.setRowStretch(3, 1)
        layout.setRowStretch(4, 1)

        layout.addWidget(self.horizon, 0, 0, 5, 3, Qt.Alignment())
        layout.addWidget(self.aircraft, 2, 1, 1, 1, Qt.Alignment())
        layout.addWidget(self.roll_dial, 1, 1, 3, 1, Qt.Alignment())

    @Slot(float, float, float)
    def on_ahrs_changed(self, heading, pitch, roll):
        self.horizon.setAhrs(heading, pitch, roll)
        self.roll_dial.setAhrs(heading, pitch, roll)
