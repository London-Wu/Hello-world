#icon
from PyQt5 import QtWidgets,QtGui
import sys

class pg2(QtWidgets.QWidget):
    def __init__(self,parent = None):
        QtWidgets.QWidget.__init__(self,parent)
        
        self.setGeometry(0,0,500,300)
        self.setWindowTitle('Do you notice the icon?')
        self.setWindowIcon(QtGui.QIcon(r'icon.png'))
        

app = QtWidgets.QApplication(sys.argv)
icon = pg2()
icon.show()
sys.exit(app.exec_())
