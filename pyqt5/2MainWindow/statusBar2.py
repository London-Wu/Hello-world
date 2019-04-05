from PyQt5 import QtWidgets,QtGui
import sys

class pg(QtWidgets.QMainWindow):
    x = 0

    def __init__(self):
        super().__init__()

        self.resize(500,250)
        self.setWindowTitle(r"状态栏")
        self.setWindowIcon(QtGui.QIcon(r'icon.png'))

        but = QtWidgets.QPushButton('add it', self)
        but.setGeometry(430, 215, 60, 25)
        but.clicked.connect(self.add_it)

        self.sta = self.statusBar()
        self.sta.showMessage(str(self.x))

    def add_it(self):
            self.x += 1
            self.sta.showMessage(str(self.x))

app = QtWidgets.QApplication(sys.argv)
a = pg()
a.show()
sys.exit(app.exec_())
