from PyQt5 import QtWidgets, QtGui, QtCore
import sys

class pg5(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle(r"press the 'x'")
        self.setWindowIcon(QtGui.QIcon(r'icon.png'))

    def closeEvent(self, Event):
        reply = QtWidgets.QMessageBox.question(self, 'Message', 'Are you sure to close the program?',
                                               QtWidgets.QMessageBox.Yes,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            Event.accept()
        else:
            Event.ignore()


app = QtWidgets.QApplication(sys.argv)
a = pg5()
a.show()
sys.exit(app.exec_())
