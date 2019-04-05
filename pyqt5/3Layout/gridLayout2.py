#网格布局2
#addWidget ( QWidget * widget, int row, int column, Qt::Alignment alignment = 0 )
#addWidget(QWidget * widget, int fromRow, int fromColumn, int rowSpan, int columnSpan, Qt::Alignment alignment = 0)行，列，占用行数，占用列数
import sys
from PyQt5 import QtWidgets, QtGui

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle('网格布局2')
        self.setWindowIcon(QtGui.QIcon(r'icon.png'))

        main_ground = QtWidgets.QWidget()
        self.setCentralWidget(main_ground)

        grid = QtWidgets.QGridLayout()
        grid.setSpacing(20)
        grid.addWidget(QtWidgets.QLabel('标题'), 1, 0)
        grid.addWidget(QtWidgets.QLineEdit(), 1, 1)
        grid.addWidget(QtWidgets.QLabel("作者:"), 2, 0)
        grid.addWidget(QtWidgets.QLineEdit(), 2, 1)
        grid.addWidget(QtWidgets.QLabel("评论:"), 3, 0)
        grid.addWidget(QtWidgets.QTextEdit(), 3, 1, 15, 1)

        main_ground.setLayout(grid)
        self.resize(350, 300)

app = QtWidgets.QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
sys.exit(app.exec_())