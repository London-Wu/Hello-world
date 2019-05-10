from PyQt5 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)

w = QtWidgets.QWidget()
w.resize(400,300)
w.setWindowTitle('The First Program')
w.show()
sys.exit(app.exec_())
