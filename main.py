from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QStackedLayout, QWidget

from widgets.attitude import AttitudeWidget

class Airshow(QWidget):
    def __init__(self, parent=None):
        super(Airshow, self).__init__(parent)

        self.setWindowTitle('Airshow')

        attitudeWidget = AttitudeWidget()

        layout = QStackedLayout()
        layout.addWidget(attitudeWidget)

        self.setLayout(layout)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            self.close()

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    airshow = Airshow()
    airshow.setFixedSize(800, 480)
    airshow.show()

    sys.exit(app.exec_())
