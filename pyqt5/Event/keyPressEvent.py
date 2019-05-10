'''用esc退出'''
import sys
from PyQt5 import QtWidgets, QtCore

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle('try to press \'Esc\'')
        self.resize(250,150)

    def keyPressEvent(self, event):#重新定义keyPressEvent()方法
        if event.key() == QtCore.Qt.Key_Escape:
            self.close()

app = QtWidgets.QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
sys.exit(app.exec_())
