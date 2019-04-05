#Box定位
#https://fishc.com.cn/thread-61103-1-1.html
import sys
from PyQt5 import QtWidgets, QtGui

class MainWindow(QtWidgets.QWidget):

    window_width = 300
    window_height = 150

    def __init__(self):
        super().__init__()

        self.setWindowTitle('Box定位')
        self.setWindowIcon(QtGui.QIcon(r'icon.png'))

        self.ok_button = QtWidgets.QPushButton('确定')
        self.cancel_button = QtWidgets.QPushButton('确定')

        self.h_box = QtWidgets.QHBoxLayout() #创建一个水平 box 布局
        self.h_box.addStretch(1)#伸缩间隔元素
        self.h_box.addWidget(self.ok_button)
        self.h_box.addWidget(self.cancel_button)

        self.v_box = QtWidgets.QVBoxLayout()#创建一个垂直 box 布局
        self.v_box.addStretch(1)
        self.v_box.addLayout(self.h_box)

        self.setLayout(self.v_box)

        self.resize(self.window_width, self.window_height)

app = QtWidgets.QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
sys.exit(app.exec_())