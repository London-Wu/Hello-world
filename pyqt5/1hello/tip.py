#tip
from PyQt5 import QtWidgets, QtGui, QtCore
import sys

class pg3(QtWidgets.QWidget):
    def __init__(self,parent = None):
        QtWidgets.QWidget.__init__(self, parent)
        
        self.setGeometry(0,0,500,300)
        self.setWindowTitle('try to move in the program...')
        self.setWindowIcon(QtGui.QIcon(r'icon.png'))
        self.setToolTip('Hello,this is a <b>Qwidget<b> widget')
        QtWidgets.QToolTip.setFont(QtGui.QFont('站酷快乐体2016修订版',100)) #设置一个有趣的字体和超超超大的文字大小

app = QtWidgets.QApplication(sys.argv)
tip = pg3()
tip.show()
sys.exit(app.exec_())
