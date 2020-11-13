# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from math import *
from Ui_huilv import Ui_MainWindow
from PyQt5.QtWidgets import *
import time
from PyQt5.QtCore import *
import tools

class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

    @pyqtSlot()
    def eventFilter(self, object, event):
        if object == self.pushButton:
            if event.type() == QEvent.Enter:
                self.statusBar.showMessage("分词后的txt文件生成",0)
            elif event.type() == QEvent.Leave:
                self.statusBar.showMessage("exit", 1)
        if object == self.pushButton_2:
            if event.type() == QEvent.Enter:
                self.statusBar.showMessage("分词后的json文件生成",0)
            elif event.type() == QEvent.Leave:
                self.statusBar.showMessage("exit", 1)
        if object == self.pushButton_3:
            if event.type() == QEvent.Enter:
                self.statusBar.showMessage("分词后的csv文件生成", 0)
            elif event.type() == QEvent.Leave:
                self.statusBar.showMessage("exit", 1)
        return QWidget.eventFilter(self, object, event)

    @pyqtSlot()
    def on_pushButton_clicked(self):
        file = QFileDialog.getOpenFileName(self, "dakai", "*.txt")
        path=tools.document(file[0])
        QMessageBox.about(self, '输出文件', path)

    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        file = QFileDialog.getOpenFileName(self, "dakai", "*_OutPut.txt")
        path = tools.generatesg(file[0])
        QMessageBox.about(self, '输出文件', path)

    @pyqtSlot()
    def on_pushButton_3_clicked(self):
        file = QFileDialog.getOpenFileName(self, "dakai", "*_OutPut.json")
        path = tools.csvstorage(file[0])
        QMessageBox.about(self, '输出文件', path)

    @pyqtSlot()
    def on_actionpre_triggered(self):
        """
        Slot documentation goes here.
        """
        QMessageBox.about(self, '介绍', '一个分词计数工具，分词首先txt需要生成，再其次是json生成，最后是csv生成，需要按照这个顺序生成，后续会改进')

    @pyqtSlot()
    def on_actionsj_triggered(self):
        file = QFileDialog.getOpenFileName(self, "dakai", "*./")
        if file[0]:
            f = open(file[0], encoding='utf-8', errors='ignore')
            with f:
                data = f.read()
                self.textBrowser.append(str(data))
            f.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    splash = QSplashScreen(QtGui.QPixmap(":/tp/ZHpng.png"))
    splash.setFont(QtGui.QFont('隶书', 39))
    splash.showMessage('正在加载程序...', Qt.AlignCenter, Qt.blue)
    splash.show()
    time.sleep(1)
    splash.clearMessage()
    splash.showMessage('欢迎使用', Qt.AlignCenter, Qt.green)
    splash.show()
    time.sleep(1)
    app.processEvents()
    ui = MainWindow()
    ui.show()
    splash.finish(ui)
    sys.exit(app.exec_())
