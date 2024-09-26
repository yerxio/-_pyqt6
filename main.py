import sys

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMainWindow, QLabel

from dao import userDao


class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        # 设置只显示最小化和关闭按钮
        # self.setWindowFlags(QtCore.Qt.WindowType.WindowMinimizeButtonHint | QtCore.Qt.WindowType.WindowCloseButtonHint)
        self.setupUi(self)

        # 设置背景图片
        self.centralwidget.setStyleSheet("border-image:url('./images/1.jpeg')")
        # 设置状态栏内容
        myLabel = QLabel()
        myLabel.setText('当前登录用户:' + f'{userDao.currentUser.username}')
        self.statusbar.addWidget(myLabel)


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(parent=self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(parent=self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(parent=self.menubar)
        self.menu_3.setObjectName("menu_3")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtGui.QAction(parent=MainWindow)
        self.action.setObjectName("action")
        self.action_2 = QtGui.QAction(parent=MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtGui.QAction(parent=MainWindow)
        self.action_3.setObjectName("action_3")
        self.action_4 = QtGui.QAction(parent=MainWindow)
        self.action_4.setObjectName("action_4")
        self.action_5 = QtGui.QAction(parent=MainWindow)
        self.action_5.setObjectName("action_5")
        self.action_6 = QtGui.QAction(parent=MainWindow)
        self.action_6.setObjectName("action_6")
        self.action_8 = QtGui.QAction(parent=MainWindow)
        self.action_8.setObjectName("action_8")
        self.action_9 = QtGui.QAction(parent=MainWindow)
        self.action_9.setObjectName("action_9")
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_2)
        self.menu_2.addAction(self.action_3)
        self.menu_2.addAction(self.action_4)
        self.menu_3.addAction(self.action_5)
        self.menu_3.addAction(self.action_6)
        self.menu_3.addSeparator()
        self.menu_3.addAction(self.action_8)
        self.menu_3.addAction(self.action_9)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "图书管理系统"))
        self.menu.setTitle(_translate("MainWindow", "图书管理"))
        self.menu_2.setTitle(_translate("MainWindow", "图书类别管理"))
        self.menu_3.setTitle(_translate("MainWindow", "系统设置"))
        self.action.setText(_translate("MainWindow", "图书添加"))
        self.action_2.setText(_translate("MainWindow", "图书信息管理"))
        self.action_3.setText(_translate("MainWindow", "图书类别添加"))
        self.action_4.setText(_translate("MainWindow", "图书类别信息管理"))
        self.action_5.setText(_translate("MainWindow", "修改密码"))
        self.action_6.setText(_translate("MainWindow", "安全退出"))
        self.action_8.setText(_translate("MainWindow", "关于作者"))
        self.action_9.setText(_translate("MainWindow", "广告位:python222"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow()
    ui.show()

    sys.exit(app.exec())
