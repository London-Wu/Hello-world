from PyQt5 import QtWidgets, QtGui, QtCore
import sys

class pg6(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self.resize(500,250)
        self.setWindowTitle(r"程序居中")
        self.setWindowIcon(QtGui.QIcon(r'icon.png'))
        self.MoveToCenter()

    def MoveToCenter(self):
        screen_size = QtWidgets.QDesktopWidget().screenGeometry()#计算出显示器的分辨率
        window_size = self.geometry()#获取 QWidget 窗口的大小
        self.move(
            (screen_size.width()-window_size.width())/2,
            (screen_size.height()-window_size.height())/2
        )

app = QtWidgets.QApplication(sys.argv)
a = pg6()
a.show()
sys.exit(app.exec_())
