#绝对定位
import sys
from PyQt5 import QtWidgets, QtGui
import random

class MainWindow(QtWidgets.QMainWindow):
    window_width = 430
    window_height = 285
    label_print_width = window_width - 100
    label_print_height = window_height - 55

    def __init__(self):
        super().__init__()

        self.resize(self.window_width, self.window_height)
        self.setWindowTitle('绝对定位')
        self.setWindowIcon(QtGui.QIcon(r'icon.png'))

        randly_print_buttom = QtWidgets.QPushButton('show it!', self)
        randly_print_buttom.setGeometry(self.window_width - 70, self.window_height - 35, 60, 25)
        randly_print_buttom.clicked.connect(self.randlyPrintLebal)

    def randlyPrintLebal(self):
        randly_print_num = random.randint(-99999,99999)
        num_label = QtWidgets.QLabel(str(randly_print_num), self)
        num_label.move(random.randint(0,self.label_print_width),random.randint(0,self.label_print_height))#定位到随机位置
        num_label.show()

app = QtWidgets.QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
sys.exit(app.exec_())
