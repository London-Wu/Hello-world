from PyQt5 import QtWidgets,QtGui
import sys

class pg(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.resize(500,250)
        self.setWindowTitle(r"工具栏")
        self.setWindowIcon(QtGui.QIcon(r'icon.png'))

        exit_menu = QtWidgets.QAction(QtGui.QIcon(r'exit.png'),'退出',self)
        exit_menu.setShortcut('Ctrl+Q')
        exit_menu.setStatusTip('点击退出程序')
        exit_menu.triggered.connect(QtWidgets.qApp.quit)

        self.statusBar()

        menubar = self.menuBar()
        file = menubar.addMenu('功能')
        file.addAction(exit_menu)

app = QtWidgets.QApplication(sys.argv)
a = pg()
a.show()
sys.exit(app.exec_())
