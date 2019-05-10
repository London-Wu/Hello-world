'''发射信号(biu,biu,biu)'''
import sys
from PyQt5 import QtWidgets,QtCore

class Main(QtWidgets.QWidget):

    closeEmitApp = QtCore.pyqtSignal()#创建信号closeEmitApp(),信号需作为类的属性定义

    def __init__(self):
        super(Main, self).__init__()

        self.setWindowTitle('发射信号 biu,biu,biu')
        self.resize(300, 150)

        self.closeEmitApp.connect(self.close)#连接信号

    def mousePressEvent(self, QMouseEvent):
        self.closeEmitApp.emit()#发射信号

app = QtWidgets.QApplication(sys.argv)
es = Main()
es.show()
sys.exit(app.exec_())
