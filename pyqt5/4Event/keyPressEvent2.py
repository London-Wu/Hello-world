import sys
from PyQt5 import QtWidgets, QtCore, QtGui

class MainWindow(QtWidgets.QWidget):
    the_label_num = 1
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle('test')
        self.resize(500, 250)

        self.num_label = QtWidgets.QLabel(str(self.the_label_num), self)
        self.num_label.setFont(QtGui.QFont('站酷快乐体2016修订版', 100))
        self.num_label.resize(500,250)

    def keyPressEvent(self, event):#重新定义keyPressEvent()方法
        if event.key() == QtCore.Qt.Key_Space:
            self.add_it()

    def add_it(self):
        self.the_label_num += 1
        self.num_label.setText(str(self.the_label_num))

app = QtWidgets.QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
sys.exit(app.exec_())
