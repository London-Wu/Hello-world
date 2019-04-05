#输入对话框
import sys
from PyQt5 import QtWidgets, QtCore, QtGui

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle('输入对话框')
        self.button = QtWidgets.QPushButton('Dialog',self)
        self.button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button.clicked.connect(self.show_dialog)
        self.setFocus()

        self.label = QtWidgets.QLabel(self)
        self.label.setFont(QtGui.QFont(None, 50))

        self.h_box = QtWidgets.QHBoxLayout()
        self.h_box.addSpacing(10)
        self.h_box.addWidget(self.button)
        self.h_box.addStretch(1)
        self.h_box.addWidget(self.label)
        self.setLayout(self.h_box)
    def show_dialog(self):
        text, if_ok = QtWidgets.QInputDialog.getText(self, '输入对话框', '请输入你的名字:')
        if if_ok:
            self.label.setText(text)

app = QtWidgets.QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
sys.exit(app.exec_())