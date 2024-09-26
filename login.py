"""
管理员登录模块
"""
import sys

from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import QWidget, QApplication, QMessageBox

import main
from dao import userDao
from entity.UserModel import User


class Ui_Form(QWidget):

    def __init__(self):
        super(Ui_Form, self).__init__()
        self.setupUi(self)
        self.resetBtn.clicked.connect(self.resetForm)
        self.loginBtn.clicked.connect(self.login)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.formLayoutWidget = QtWidgets.QWidget(parent=Form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(60, 70, 241, 151))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(10, 10, 10, 10)
        self.formLayout.setHorizontalSpacing(25)
        self.formLayout.setVerticalSpacing(40)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_2)
        self.uerNameInput = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.uerNameInput.setObjectName("uerNameInput")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.uerNameInput)
        self.passwordInput = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.passwordInput.setObjectName("passwordInput")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.passwordInput)
        self.widget = QtWidgets.QWidget(parent=Form)
        self.widget.setGeometry(QtCore.QRect(80, 240, 202, 26))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(50)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.loginBtn = QtWidgets.QPushButton(parent=self.widget)
        self.loginBtn.setObjectName("loginBtn")
        self.horizontalLayout.addWidget(self.loginBtn)
        self.resetBtn = QtWidgets.QPushButton(parent=self.widget)
        self.resetBtn.setObjectName("resetBtn")
        self.horizontalLayout.addWidget(self.resetBtn)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "管理员登录"))
        self.label.setText(_translate("Form", "用户名:"))
        self.label_2.setText(_translate("Form", "密码:"))
        self.loginBtn.setText(_translate("Form", "登录"))
        self.resetBtn.setText(_translate("Form", "重置"))

    def resetForm(self):
        self.uerNameInput.clear()
        self.passwordInput.clear()

    def login(self):
        """
        用户登录判断, 数据库判断成功, 则打开主窗体, 否则提示错误
        :return:
        """
        userName = self.uerNameInput.text()
        password = self.passwordInput.text()
        if userName == '' or password == '':
            QMessageBox.warning(None, '系统提示', '用户名或密码不能为空')
        else:
            user = User(userName, password)
            resultUser = userDao.login(user)
            if resultUser:
                print('登录成功')
                userDao.currentUser = user
                self.mw = main.Ui_MainWindow()  # 实例化主窗体
                self.mw.show()  # 显示主窗体
                self.close()  # 关闭登录窗体
            else:
                QMessageBox.warning(None, '系统提示', '用户名或密码错误')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = Ui_Form()
    ui.show()

    sys.exit(app.exec())
