from PyQt5 import QtWidgets,QtGui
import sys

class pg(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.resize(500,250)
        self.setWindowTitle(r"状态栏")
        self.setWindowIcon(QtGui.QIcon(r'icon.png'))
        a = self.statusBar()
        a.showMessage('我是状态栏')

app = QtWidgets.QApplication(sys.argv)
a = pg()
a.show()
sys.exit(app.exec_())
