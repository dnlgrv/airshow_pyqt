from PyQt5.QtCore import Qt, pyqtSlot as Slot
from PyQt5.QtWidgets import QGridLayout, QWidget

from widgets.attitude.aircraft import Aircraft
from widgets.attitude.altitude import Altitude
from widgets.attitude.horizon import Horizon
from widgets.attitude.pitch_scale import PitchScale
from widgets.attitude.roll_scale import RollScale
from widgets.attitude.slip_indicator import SlipIndicator

class AttitudeWidget(QWidget):
    def __init__(self, ahrs, settings, parent=None):
        super(AttitudeWidget, self).__init__(parent)

        self.ahrs = ahrs
        ahrs.changed.connect(self.on_ahrs_changed)

        self.settings = settings
        settings.changed.connect(self.on_settings_changed)

        self.horizon = Horizon(self)

        self.altitude = Altitude(self.settings.qnh, self)
        self.pitch_scale = PitchScale(self)
        self.roll_scale = RollScale(self)
        self.slip_indicator = SlipIndicator(self)

        self.aircraft = Aircraft(self)

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
        layout.addWidget(self.pitch_scale, 2, 1, 1, 1, Qt.Alignment())
        layout.addWidget(self.aircraft, 2, 1, 1, 1, Qt.Alignment())
        layout.addWidget(self.roll_scale, 0, 1, 5, 1, Qt.Alignment())
        layout.addWidget(self.slip_indicator, 3, 1, 2, 1, Qt.Alignment())
        layout.addWidget(self.altitude, 0, 2, 5, 1, Qt.Alignment())

    @Slot()
    def on_ahrs_changed(self):
        heading = self.ahrs.heading
        pitch = self.ahrs.pitch
        roll = self.ahrs.roll

        self.horizon.setAhrs(heading, pitch, roll)
        self.pitch_scale.setAhrs(heading, pitch, roll)
        self.roll_scale.setAhrs(heading, pitch, roll)

        self.slip_indicator.setAhrs(self.ahrs.slip)

    @Slot()
    def on_settings_changed(self):
        self.horizon.setVerticalOffset(self.settings.vertical_offset)
        self.pitch_scale.setVerticalOffset(self.settings.vertical_offset)

        self.altitude.setQNH(self.settings.qnh)
