# Form implementation generated from reading ui file '图书类别维护.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(654, 547)
        self.bookTypeTable = QtWidgets.QTableWidget(parent=Form)
        self.bookTypeTable.setGeometry(QtCore.QRect(10, 80, 451, 192))
        self.bookTypeTable.setObjectName("bookTypeTable")
        self.bookTypeTable.setColumnCount(0)
        self.bookTypeTable.setRowCount(0)
        self.groupBox = QtWidgets.QGroupBox(parent=Form)
        self.groupBox.setGeometry(QtCore.QRect(20, 0, 431, 80))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(parent=self.groupBox)
        self.label.setGeometry(QtCore.QRect(70, 20, 81, 31))
        self.label.setObjectName("label")
        self.s_bookTypeNameInput = QtWidgets.QLineEdit(parent=self.groupBox)
        self.s_bookTypeNameInput.setGeometry(QtCore.QRect(170, 30, 113, 21))
        self.s_bookTypeNameInput.setObjectName("s_bookTypeNameInput")
        self.searchBtn = QtWidgets.QPushButton(parent=self.groupBox)
        self.searchBtn.setGeometry(QtCore.QRect(290, 30, 75, 24))
        self.searchBtn.setObjectName("searchBtn")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=Form)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 280, 451, 151))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(30, 20, 49, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(200, 20, 49, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(30, 50, 49, 16))
        self.label_4.setObjectName("label_4")
        self.idInput = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.idInput.setGeometry(QtCore.QRect(70, 20, 51, 21))
        self.idInput.setObjectName("idInput")
        self.bookTypeNameInput = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.bookTypeNameInput.setGeometry(QtCore.QRect(260, 20, 151, 21))
        self.bookTypeNameInput.setObjectName("bookTypeNameInput")
        self.bookTypeDescInput = QtWidgets.QPlainTextEdit(parent=self.groupBox_2)
        self.bookTypeDescInput.setGeometry(QtCore.QRect(70, 50, 261, 71))
        self.bookTypeDescInput.setObjectName("bookTypeDescInput")
        self.modifyBtn = QtWidgets.QPushButton(parent=Form)
        self.modifyBtn.setGeometry(QtCore.QRect(90, 480, 75, 24))
        self.modifyBtn.setObjectName("modifyBtn")
        self.delBtn = QtWidgets.QPushButton(parent=Form)
        self.delBtn.setGeometry(QtCore.QRect(170, 480, 75, 24))
        self.delBtn.setObjectName("delBtn")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "图书类别信息管理"))
        self.groupBox.setTitle(_translate("Form", "查询操作"))
        self.label.setText(_translate("Form", "图书类别名称: "))
        self.searchBtn.setText(_translate("Form", "搜索"))
        self.groupBox_2.setTitle(_translate("Form", "表单操作"))
        self.label_2.setText(_translate("Form", "编号"))
        self.label_3.setText(_translate("Form", "图书类别名称"))
        self.label_4.setText(_translate("Form", "描述"))
        self.modifyBtn.setText(_translate("Form", "修改"))
        self.delBtn.setText(_translate("Form", "删除"))
