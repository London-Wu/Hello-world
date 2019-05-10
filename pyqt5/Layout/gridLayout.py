#网格布局
import sys
from PyQt5 import QtWidgets, QtGui

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle('网格布局')
        self.setWindowIcon(QtGui.QIcon(r'icon.png'))

        button_names = [
            'Cls', 'Bck', '', 'Close',
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]
        main_ground = QtWidgets.QWidget()
        self.setCentralWidget(main_ground)#将main_ground置为中心部件
        grid = QtWidgets.QGridLayout()

        for [n, (x, y)] in enumerate([(i, j) for i in range(5) for j in range(4)]):
            if (x, y) == (0, 2):
                grid.addWidget(QtWidgets.QLabel(button_names[n]), x, y) #填补 Bck 和 Close 按钮之间的空白使用 QLabel 部件
            else:
                grid.addWidget(QtWidgets.QPushButton(button_names[n]), x, y)
        main_ground.setLayout(grid)

app = QtWidgets.QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
sys.exit(app.exec_())