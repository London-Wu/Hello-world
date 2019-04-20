from PyQt5 import QtWidgets,QtGui
import sys

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('格式化工具build')

        start_button = QtWidgets.QPushButton('Start')
        info_button = QtWidgets.QPushButton('information')
        help_button = QtWidgets.QPushButton('help')
        about_button = QtWidgets.QPushButton('about')
        aboutQt_button = QtWidgets.QPushButton('made by Qt')

        start_button.clicked.connect(self.start)
        info_button.clicked.connect(self.info)
        help_button.clicked.connect(self.help)
        about_button.clicked.connect(self.about)
        aboutQt_button.clicked.connect(self.aboutQt)

        self.status_label = QtWidgets.QLabel('就绪')
        self.status_label.setFrameStyle(QtWidgets.QFrame.Panel | QtWidgets.QFrame.Sunken)
        status_layout = QtWidgets.QHBoxLayout()
        status_layout.addWidget(QtWidgets.QLabel('status'))
        status_layout.addWidget(self.status_label)

        mainLayout = QtWidgets.QGridLayout()
        mainLayout.addLayout(status_layout, 0, 0)
        mainLayout.addWidget(start_button, 1, 0)
        mainLayout.addWidget(info_button, 2, 0)
        mainLayout.addWidget(help_button, 3, 0)
        mainLayout.addWidget(about_button, 4, 0)
        mainLayout.addWidget(aboutQt_button, 5, 0)
        self.setLayout(mainLayout)

        self.resize(400,200)

    def start(self):
        answer = QtWidgets.QMessageBox.question(self, 'Warning!', '你真的确定开始格式化吗？',
                                                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if answer == QtWidgets.QMessageBox.Yes:
            QtWidgets.QMessageBox.critical(self, 'Error!', '粗错啦:权限不足！')
            self.status_label.setText('系统格式化出错')
        else:
            self.status_label.setText('格式化：操作取消')

    def info(self):
        QtWidgets.QMessageBox.information(self, 'Information', '当前程序版本为build0.0.0001\n程序开发者:London Wu')
        self.status_label.setText('提示信息输出')

    def help(self):
        QtWidgets.QMessageBox.warning(self, 'Error!', '找不到帮助文档！')
        self.status_label.setText('帮助文档输出出错')

    def about(self):
        QtWidgets.QMessageBox.about(self, 'About', 'Copyright 2015 London Wu.\n All Right reserved.')
        self.status_label.setText('版权信息输出')

    def aboutQt(self):
        QtWidgets.QMessageBox.aboutQt(self, 'About Qt')
        self.status_label.setText('Qt信息输出')


app = QtWidgets.QApplication(sys.argv)
main_Window = MainWindow()
main_Window.show()
sys.exit(app.exec())