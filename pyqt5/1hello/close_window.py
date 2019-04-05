#QPushButton(string text, QWidget parent = None)
from PyQt5 import QtWidgets, QtGui, QtCore
import sys

class pg4(QtWidgets.QWidget):
    def __init__(self,parent = None):
        QtWidgets.QWidget.__init__(self, parent)
        
        self.setGeometry(300,300,250,150)
        self.setWindowTitle('close')
        self.setWindowIcon(QtGui.QIcon(r'icon.png'))

        quit_button = QtWidgets.QPushButton('quit', self)#创建一个按钮并将其放在QWidget部件上
        quit_button.setGeometry(180,115,60,25)
        quit_button.clicked.connect(QtWidgets.qApp.quit)
        quit_button.setToolTip('try to press me...')

app = QtWidgets.QApplication(sys.argv)
a = pg4()
a.show()
sys.exit(app.exec_())
