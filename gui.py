#!/usr/bin/python
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testStack.ui'
#
# Created: Thu Apr  7 09:57:26 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!
import sys
import os
import datetime
import time
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
        self.confirm = None

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(800, 480)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.stackedWidget = QtGui.QStackedWidget(Form)
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.login = QtGui.QWidget()
        self.login.setObjectName(_fromUtf8("login"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.login)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.label = QtGui.QLabel(self.login)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_4.addWidget(self.label)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.verticalLayout_6.addLayout(self.horizontalLayout_4)
        self.verticalLayout_3.addLayout(self.verticalLayout_6)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.label_2 = QtGui.QLabel(self.login)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_5.addWidget(self.label_2)
        self.lineEdit = QtGui.QLineEdit(self.login)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout_5.addWidget(self.lineEdit)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem5)
        self.label_3 = QtGui.QLabel(self.login)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_7.addWidget(self.label_3)
        self.lineEdit_2 = QtGui.QLineEdit(self.login)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.horizontalLayout_7.addWidget(self.lineEdit_2)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem6)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.pushButton = QtGui.QPushButton(self.login)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_6.addWidget(self.pushButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        spacerItem7 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem7)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.stackedWidget.addWidget(self.login)
        self.adminMenu = QtGui.QWidget()
        self.adminMenu.setObjectName(_fromUtf8("adminMenu"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.adminMenu)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem8)
        self.label_4 = QtGui.QLabel(self.adminMenu)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_8.addWidget(self.label_4)
        spacerItem9 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem9)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.label_5 = QtGui.QLabel(self.adminMenu)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_11.addWidget(self.label_5)
        self.lineEdit_3 = QtGui.QLineEdit(self.adminMenu)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.horizontalLayout_11.addWidget(self.lineEdit_3)
        self.pushButton_2 = QtGui.QPushButton(self.adminMenu)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout_11.addWidget(self.pushButton_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.label_7 = QtGui.QLabel(self.adminMenu)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_12.addWidget(self.label_7)
        self.lineEdit_4 = QtGui.QLineEdit(self.adminMenu)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.horizontalLayout_12.addWidget(self.lineEdit_4)
        self.label_6 = QtGui.QLabel(self.adminMenu)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_12.addWidget(self.label_6)
        self.lineEdit_5 = QtGui.QLineEdit(self.adminMenu)
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.horizontalLayout_12.addWidget(self.lineEdit_5)
        self.verticalLayout_7.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.label_8 = QtGui.QLabel(self.adminMenu)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_13.addWidget(self.label_8)
        self.lineEdit_6 = QtGui.QLineEdit(self.adminMenu)
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.horizontalLayout_13.addWidget(self.lineEdit_6)
        self.label_9 = QtGui.QLabel(self.adminMenu)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_13.addWidget(self.label_9)
        self.lineEdit_7 = QtGui.QLineEdit(self.adminMenu)
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        self.horizontalLayout_13.addWidget(self.lineEdit_7)
        self.verticalLayout_7.addLayout(self.horizontalLayout_13)
        self.pushButton_3 = QtGui.QPushButton(self.adminMenu)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.verticalLayout_7.addWidget(self.pushButton_3)
        self.horizontalLayout_10.addLayout(self.verticalLayout_7)
        self.verticalLayout_4.addLayout(self.horizontalLayout_10)
        self.verticalLayout_9 = QtGui.QVBoxLayout()
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.label_10 = QtGui.QLabel(self.adminMenu)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_9.addWidget(self.label_10)
        self.lineEdit_8 = QtGui.QLineEdit(self.adminMenu)
        self.lineEdit_8.setObjectName(_fromUtf8("lineEdit_8"))
        self.horizontalLayout_9.addWidget(self.lineEdit_8)
        self.verticalLayout_9.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_14 = QtGui.QHBoxLayout()
        self.horizontalLayout_14.setObjectName(_fromUtf8("horizontalLayout_14"))
        self.label_11 = QtGui.QLabel(self.adminMenu)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout_14.addWidget(self.label_11)
        self.lineEdit_9 = QtGui.QLineEdit(self.adminMenu)
        self.lineEdit_9.setObjectName(_fromUtf8("lineEdit_9"))
        self.horizontalLayout_14.addWidget(self.lineEdit_9)
        self.verticalLayout_9.addLayout(self.horizontalLayout_14)
        self.pushButton_4 = QtGui.QPushButton(self.adminMenu)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.verticalLayout_9.addWidget(self.pushButton_4)
        self.verticalLayout_4.addLayout(self.verticalLayout_9)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.stackedWidget.addWidget(self.adminMenu)
        self.userMenu = QtGui.QWidget()
        self.userMenu.setObjectName(_fromUtf8("userMenu"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.userMenu)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.label_12 = QtGui.QLabel(self.userMenu)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.verticalLayout_5.addWidget(self.label_12)
        self.horizontalLayout_3.addLayout(self.verticalLayout_5)
        self.stackedWidget.addWidget(self.userMenu)
        self.verticalLayout.addWidget(self.stackedWidget)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "Login", None))
        self.label_2.setText(_translate("Form", "User name", None))
        self.label_3.setText(_translate("Form", "Password", None))
        self.pushButton.setText(_translate("Form", "PushButton", None))
        self.label_4.setText(_translate("Form", "Admin Menu", None))
        self.label_5.setText(_translate("Form", "Name", None))
        self.pushButton_2.setText(_translate("Form", "Create New Database", None))
        self.label_7.setText(_translate("Form", "Username", None))
        self.label_6.setText(_translate("Form", "Privileges", None))
        self.label_8.setText(_translate("Form", "Password", None))
        self.label_9.setText(_translate("Form", "Database Name", None))
        self.pushButton_3.setText(_translate("Form", "Add User", None))
        self.label_10.setText(_translate("Form", "Database", None))
        self.label_11.setText(_translate("Form", "Username", None))
        self.pushButton_4.setText(_translate("Form", "Remove User", None))
        self.label_12.setText(_translate("Form", "User Menu", None))

    def readContextFile(self):
        with open("context.txt") as f:
            lines = f.read().splitlines()
        return lines

    @QtCore.pyqtSignature("on_pushButton_clicked()")
    def loginMenu(self):
        arg1 = str(self.lineEdit.text())
        arg2 = str(self.lineEdit_2.text())
        os.system("python login.py " + arg1 + ' ' + arg2)
        lines = self.readContextFile()
        print lines
        if lines[0] == "true":
            if lines[1] == "admin":
                self.stackedWidget.setCurrentIndex(1)
            elif lines[1] == "user":
		        self.stackedWidget.setCurrentIndex(2)
            else:
                QtGui.QMessageBox.warning(self, 'Not Found', 'Not Found')
        else:
            QtGui.QMessageBox.warning(self, 'Not Found', 'Not Found')

    @QtCore.pyqtSignature("on_pushButton_2_clicked()")
    def adminmenu(self):
        '''name = str(self.lineEdit_3.text())
        success = self.createDatabase(name);
        if success:
            QtGui.QMessageBox.information(self, 'Success', 'Data Base ' + name + " created.")
        else:
            QtGui.QMessageBox.warning(self, 'Database not created', 'A database with that name already exists.')
        '''
    @QtCore.pyqtSignature("on_pushButton_3_clicked()")
    def adminAddUsermenu(self):   
        '''user = str(self.lineEdit_4.text())
        password = str(self.lineEdit_6.text())
        privileges = str(self.lineEdit_5.text())
        dbname = str(self.lineEdit_7.text())
        success = self.addUser(user, password, privileges, dbname )
        if success:
            QtGui.QMessageBox.information(self, 'Success', 'User ' + user + " created.")
        else:
            QtGui.QMessageBox.warning(self, 'Error: User not created.')
        '''
    @QtCore.pyqtSignature("on_pushButton_4_clicked()")
    def removeUserMenu(self):
        '''username = str(self.lineEdit_9.text())
        print username
        dbname = str(self.lineEdit_8.text())
        print dbname
        success = self.removeUser(username, dbname)
        if success:
            QtGui.QMessageBox.information(self, 'Success', 'User ' + user + " removed.")
        else:
            QtGui.QMessageBox.warning(self, 'Error', 'User not found.')
        '''
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Ui_Form()
    ex.show()
#    ex.loginMenu()
    sys.exit(app.exec_())

