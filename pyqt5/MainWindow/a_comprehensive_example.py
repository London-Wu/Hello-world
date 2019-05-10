#MainWindow的一个综合的例子
from PyQt5 import QtWidgets, QtGui
import sys

class MainWindow(QtWidgets.QMainWindow):
    window_width = 350
    window_height = 250

    def closeEvent(self, Event):
        reply = QtWidgets.QMessageBox.question(self, '退出', '你真的要退出吗?',
                                               QtWidgets.QMessageBox.Yes,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            Event.accept()
        else:
            Event.ignore()

    def exit_window(self):
        reply = QtWidgets.QMessageBox.question(self, '退出', '你真的要退出吗?',
                                               QtWidgets.QMessageBox.Yes,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            QtWidgets.qApp.quit()

    def __init__(self):
        super().__init__()

        self.resize(self.window_width, self.window_height)
        self.setWindowTitle(r'记事本v0.0.1')
        self.setWindowIcon(QtGui.QIcon(r'icon.png'))

        text_edit = QtWidgets.QTextEdit()
        self.setCentralWidget(text_edit)

        self.exit_action = QtWidgets.QAction(QtGui.QIcon(r'exit.png'), '退出', self)
        self.exit_action.setStatusTip('点击退出程序')
        self.exit_action.setShortcut('Ctrl+Q')
        self.exit_action.triggered.connect(self.exit_window)

        self.statusBar()

        self.menu_bar = self.menuBar()
        file = self.menu_bar.addMenu('文件')
        file.addAction(self.exit_action)

        self.toolbar = self.addToolBar('退出')
        self.toolbar.addAction(self.exit_action)

app = QtWidgets.QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
sys.exit(app.exec_())