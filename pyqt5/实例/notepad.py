from PyQt5 import QtWidgets, QtGui
import sys


class MainWindow(QtWidgets.QMainWindow):
    file_name = None  # 该属性表示当前正在编辑的文件名,None表示未定义
    when_open_text = ''  # 该属性表示原文本,即打开或保存时的文本

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('记事本build')
        self.resize(1000, 500)

        self.editor = QtWidgets.QTextEdit()  # 编辑框
        self.setCentralWidget(self.editor)

        self.newfile = QtWidgets.QAction('新建')
        self.newfile.setShortcut('Ctrl+N')
        self.newfile.triggered.connect(self.newfileEvent)

        self.openfile = QtWidgets.QAction('打开', self)
        self.openfile.setShortcut('Ctrl+O')
        self.openfile.triggered.connect(self.openEvent)

        self.savefile = QtWidgets.QAction('保存', self)
        self.savefile.setShortcut('Ctrl+S')
        self.savefile.triggered.connect(self.saveEvent)

        self.save_ano = QtWidgets.QAction('另存为', self)
        self.save_ano.triggered.connect(self.saveAnotherEvent)

        self.exitc = QtWidgets.QAction('退出', self)
        self.exitc.triggered.connect(self.closemenuEvent)

        self.menubar = self.menuBar()
        self.file_menu = self.menubar.addMenu('文件')
        self.file_menu.addAction(self.newfile)
        self.file_menu.addAction(self.openfile)
        self.file_menu.addAction(self.savefile)
        self.file_menu.addAction(self.save_ano)
        self.file_menu.addSeparator()
        self.file_menu.addAction(self.exitc)

    def newfileEvent(self):  # 新建
        # 新建前的保存确认
        if self.editor.toPlainText() != self.when_open_text:
            answer = QtWidgets.QMessageBox.question(self, '注意!', '你将要新建一个新的文件,是否保存当前文件?',
                                                    QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No | QtWidgets.QMessageBox.Cancel
                                                    )
            if answer == QtWidgets.QMessageBox.Yes:
                if self.saveEvent() == 1:
                    return
            elif answer == QtWidgets.QMessageBox.Cancel:
                return

        # 将文件名设为未定义,并将原文本,编辑框清空
        self.file_name = None
        self.when_open_text = ''
        self.editor.setPlainText('')

    def openEvent(self):  # 打开
        # 打开前的保存确认
        if self.editor.toPlainText() != self.when_open_text:
            answer = QtWidgets.QMessageBox.question(self, '注意!', '你将要打开一个新的文件,是否保存当前文件?',
                                                    QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No | QtWidgets.QMessageBox.Cancel
                                                    )
            if answer == QtWidgets.QMessageBox.Yes:
                if self.saveEvent() == 1:
                    return
            elif answer == QtWidgets.QMessageBox.Cancel:
                return
        # 打开
        self.file_name = QtWidgets.QFileDialog.getOpenFileName(self, '选择一个要打开的文件')
        try:
            with open(self.file_name[0], 'r') as file:
                self.when_open_text = file.read()  # 更新原文本
            self.editor.setPlainText(self.when_open_text)
        except FileNotFoundError:
            self.file_name = None
        except :
            QtWidgets.QMessageBox.critical(self, '出错啦!', '不是合法的文本文件!')
            self.file_name = None

    def saveEvent(self):  # 保存
        if self.file_name == None:  # 当文件名未定义时先定义文件名
            self.file_name = QtWidgets.QFileDialog.getSaveFileName(self, '选择一个要保存的位置')
        try:
            with open(self.file_name[0], 'w') as file:
                file.write(self.editor.toPlainText())
        except FileNotFoundError:
            self.file_name = None
            return 1
        except:
            QtWidgets.QMessageBox.critical(self, '出错啦!', '文件写入出错!')
            self.file_name = None
            return 1
        self.when_open_text = self.editor.toPlainText()  # 更新原文本

    def saveAnotherEvent(self):  # 另存为
        self.file_name = QtWidgets.QFileDialog.getSaveFileName(self, '选择一个要保存的位置')
        try:
            with open(self.file_name[0], 'w') as file:
                file.write(self.editor.toPlainText())
            self.when_open_text = self.editor.toPlainText()
        except FileNotFoundError:
            self.file_name = None
            return 1
        except:
            QtWidgets.QMessageBox.critical(self, '出错啦!', '文件写入出错!')
            self.file_name = None
            return 1
        self.when_open_text = self.editor.toPlainText()  # 更新原文本

    def closeEvent(self, Event):
        '''重定义当x被点下时的行为,先确认保存再关闭'''
        if self.editor.toPlainText() != self.when_open_text:
            answer = QtWidgets.QMessageBox.question(self, '是否保存', '当前文本未保存,是否保存?',
                                           QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No | QtWidgets.QMessageBox.Cancel)
            if answer == QtWidgets.QMessageBox.Yes:
                if self.saveEvent() == 1:
                    Event.ignore()
            elif answer == QtWidgets.QMessageBox.No:
                pass
            else:
                Event.ignore()

    def closemenuEvent(self, Event):
        '''定义当菜单栏中的退出选项被选中的行为,与closeEvent类似'''
        if self.editor.toPlainText() != self.when_open_text:
            answer = QtWidgets.QMessageBox.question(self, '是否保存', '当前文本未保存,是否保存?',
                                           QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No | QtWidgets.QMessageBox.Cancel)
            if answer == QtWidgets.QMessageBox.Yes:
                if self.saveEvent() != 1:
                    QtWidgets.qApp.quit()
            elif answer == QtWidgets.QMessageBox.No:
                QtWidgets.qApp.quit()
            else:
                pass
        else:
            QtWidgets.qApp.quit()

app = QtWidgets.QApplication(sys.argv)
mainwindow = MainWindow()
mainwindow.show()
sys.exit(app.exec())