import math
import time
from PyQt5.QtCore import QObject, QTimer, pyqtSignal as Signal

class AHRS(QObject):
    changed = Signal()

    heading = 0
    pitch = 0
    roll = 0
    slip = 0

    def __init__(self):
        super(AHRS, self).__init__()

    def listen(self):
        self.start_time = time.time()

        self.timer = QTimer()
        self.timer.setInterval(10)
        self.timer.timeout.connect(self._timeout)
        self.timer.start()

    def _timeout(self):
        time_now = time.time()
        time_elapsed = time_now - self.start_time

        self.heading = (math.sin(time_elapsed) * 180) % 359
        self.pitch = math.cos(time_elapsed) * 10
        self.roll = math.sin(time_elapsed) * 20

        self.slip = math.cos(time_elapsed) * 1

        self.changed.emit()
