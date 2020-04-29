from PyQt5.QtCore import QObject, pyqtSignal as Signal

class Settings(QObject):
    changed = Signal()

    vertical_offset = 0
    qnh = 1013

    def __init__(self):
        super(Settings, self).__init__()

    def increase_qnh(self):
        self.qnh += 1
        self.changed.emit()

    def decrease_qnh(self):
        self.qnh -= 1
        self.changed.emit()

    def inrease_vertical_offset(self):
        self._set_vertical_offset(self.vertical_offset + 1)

    def decrease_vertical_offset(self):
        self._set_vertical_offset(self.vertical_offset - 1)

    def _set_vertical_offset(self, new_value):
        self.vertical_offset = max(min(new_value, 20), -20)
        self.changed.emit()
