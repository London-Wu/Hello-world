import sys
from PyQt5 import QtWidgets, QtCore, QtGui

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle('计算器v0.0.1')
        self.setWindowIcon(QtGui.QIcon(r'claculator.png'))

        button_names = [
            'Cls', 'Bck', '', 'Close',
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

