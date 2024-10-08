# Form implementation generated from reading ui file '图书类别添加.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.
import sys

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QWidget, QMessageBox

from dao import bookTypeDao
from entity.BookTypeModel import BookType


class Ui_Form(QWidget):

    def __init__(self):
        super(QWidget, self).__init__()
        self.setupUi(self)

        self.resetBtn.clicked.connect(self.reset)
        self.addBtn.clicked.connect(self.add)
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.formLayoutWidget = QtWidgets.QWidget(parent=Form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 311, 181))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(10, 10, 10, 15)
        self.formLayout.setHorizontalSpacing(30)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label)
        self.bookTypeNameInput = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.bookTypeNameInput.setObjectName("bookTypeNameInput")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.bookTypeNameInput)
        self.label_2 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_2)
        self.bookTypeDescInput = QtWidgets.QPlainTextEdit(parent=self.formLayoutWidget)
        self.bookTypeDescInput.setObjectName("bookTypeDescInput")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.bookTypeDescInput)
        self.addBtn = QtWidgets.QPushButton(parent=Form)
        self.addBtn.setGeometry(QtCore.QRect(20, 230, 75, 24))
        self.addBtn.setObjectName("addBtn")
        self.resetBtn = QtWidgets.QPushButton(parent=Form)
        self.resetBtn.setGeometry(QtCore.QRect(120, 230, 75, 24))
        self.resetBtn.setObjectName("resetBtn")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "图书类别添加 "))
        self.label.setText(_translate("Form", "图书类别名称:"))
        self.label_2.setText(_translate("Form", "图书类别描述: "))
        self.addBtn.setText(_translate("Form", "添加"))
        self.resetBtn.setText(_translate("Form", "重置"))

    def reset(self):
        """
        重置
        :return:
        """
        self.bookTypeNameInput.setText('')
        self.bookTypeDescInput.setPlainText('')

    def add(self):
        """
        添加图书类别信息
        :return:
        """
        bookTypeName = self.bookTypeNameInput.text()
        bookTypeDesc = self.bookTypeDescInput.toPlainText()
        if bookTypeName.strip() == '':
            QMessageBox.warning(None, '系统提示', '图书类别名称不能为空')
        else:
            bookType = BookType(bookTypeName, bookTypeDesc)
            if bookTypeDao.add(bookType):
                QMessageBox.information(None, '系统提示', '添加成功')
                self.reset()
            else:
                QMessageBox.warning(None, '系统提示', '添加失败')

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui_Form()
    window.show()
    sys.exit(app.exec())
