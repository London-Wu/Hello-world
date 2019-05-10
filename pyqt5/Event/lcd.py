from PyQt5 import QtWidgets, QtCore
import sys

class Main(QtWidgets.QWidget):
    def __init__(self):
        super(Main, self).__init__()

        self.setWindowTitle('LCD')

        lcd = QtWidgets.QLCDNumber(self)
        slider = QtWidgets.QSlider(QtCore.Qt.Horizontal, self)

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(lcd)
        v_box.addWidget(slider)

        self.setLayout(v_box)
        slider.valueChanged.connect(lcd.display)
        self.resize(250,150)

app = QtWidgets.QApplication(sys.argv)
main_window = Main()
main_window.show()
sys.exit(app.exec_())