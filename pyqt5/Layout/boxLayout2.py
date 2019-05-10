from PyQt5 import QtWidgets
import sys

class Test(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.btn_1 = QtWidgets.QPushButton('我叫Btn1', self)
        self.btn_2 = QtWidgets.QPushButton('我叫Btn2', self)
        self.btn_3 = QtWidgets.QPushButton('我叫Btn3', self)
        self.btn_4 = QtWidgets.QPushButton('我叫Btn4', self)
        self.btn_5 = QtWidgets.QPushButton('我叫Btn5', self)
        self.btn_6 = QtWidgets.QPushButton('我叫Btn6', self)

        self.v_box1 = QtWidgets.QVBoxLayout()#垂直布局框
        self.v_box2 = QtWidgets.QVBoxLayout()

        self.v_box1.setSpacing(10)  # 设置布局中每个部件间隔为3个空白
        self.v_box1.addWidget(self.btn_1)
        self.v_box1.addWidget(self.btn_2)
        self.v_box1.addSpacing(30)  # 添加3个空白到里面
        self.v_box1.addWidget(self.btn_3)

        self.v_box2.setSpacing(10)
        self.v_box2.addWidget(self.btn_4)
        self.v_box2.addWidget(self.btn_5)
        self.v_box2.addSpacing(30)
        self.v_box2.addWidget(self.btn_6)

        self.h_box = QtWidgets.QHBoxLayout()#水平布局框
        self.h_box.addLayout(self.v_box1)
        self.h_box.addStretch(1)#添加1个拉伸到里面
        self.h_box.addLayout(self.v_box2)

        self.setLayout(self.h_box)

app = QtWidgets.QApplication(sys.argv)
main_window = Test()
main_window.show()
sys.exit(app.exec_())