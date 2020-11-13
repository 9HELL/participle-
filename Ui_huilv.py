# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\86131\Desktop\build\huilv.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(546, 395)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/tp/蕾姆1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 546, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionsj = QtWidgets.QAction(MainWindow)
        self.actionsj.setObjectName("actionsj")
        self.actionpre = QtWidgets.QAction(MainWindow)
        self.actionpre.setObjectName("actionpre")
        self.menu.addAction(self.actionsj)
        self.menu.addAction(self.actionpre)
        self.menubar.addAction(self.menu.menuAction())
        self.pushButton.setMouseTracking(True)
        self.pushButton.installEventFilter(self)
        self.pushButton_2.setMouseTracking(True)
        self.pushButton_2.installEventFilter(self)
        self.pushButton_3.setMouseTracking(True)
        self.pushButton_3.installEventFilter(self)
        self.retranslateUi(MainWindow)
        self.pushButton_4.clicked.connect(self.textBrowser.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "分词统计"))
        self.label_3.setText(_translate("MainWindow", "文件内容显示区"))
        self.pushButton_4.setText(_translate("MainWindow", "清除显示区内容"))
        self.pushButton.setText(_translate("MainWindow", "生成txt"))
        self.pushButton_2.setText(_translate("MainWindow", "生成json"))
        self.pushButton_3.setText(_translate("MainWindow", "生成csv"))
        self.menu.setTitle(_translate("MainWindow", "文件 "))
        self.actionsj.setText(_translate("MainWindow", "打开"))
        self.actionpre.setText(_translate("MainWindow", "介绍"))
import tb_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
