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
        Form.resize(800, 485)
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
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.label = QtGui.QLabel(self.login)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_4.addWidget(self.label)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout_6.addLayout(self.horizontalLayout_4)
        self.verticalLayout_3.addLayout(self.verticalLayout_6)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.label_2 = QtGui.QLabel(self.login)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_5.addWidget(self.label_2)
        self.lineEdit = QtGui.QLineEdit(self.login)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout_5.addWidget(self.lineEdit)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem4)
        self.label_3 = QtGui.QLabel(self.login)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_7.addWidget(self.label_3)
        self.lineEdit_2 = QtGui.QLineEdit(self.login)
        self.lineEdit_2.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.horizontalLayout_7.addWidget(self.lineEdit_2)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem5)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.pushButton = QtGui.QPushButton(self.login)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_6.addWidget(self.pushButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        spacerItem6 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem6)
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
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem7)
        self.label_4 = QtGui.QLabel(self.adminMenu)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_8.addWidget(self.label_4)
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem8)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.pushButton_2 = QtGui.QPushButton(self.adminMenu)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.verticalLayout_8.addWidget(self.pushButton_2)
        self.verticalLayout_4.addLayout(self.verticalLayout_8)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.pushButton_3 = QtGui.QPushButton(self.adminMenu)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.horizontalLayout_10.addWidget(self.pushButton_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_24 = QtGui.QHBoxLayout()
        self.horizontalLayout_24.setObjectName(_fromUtf8("horizontalLayout_24"))
        self.pushButton_4 = QtGui.QPushButton(self.adminMenu)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.horizontalLayout_24.addWidget(self.pushButton_4)
        self.verticalLayout_4.addLayout(self.horizontalLayout_24)
        self.verticalLayout_9 = QtGui.QVBoxLayout()
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.pushButton_12 = QtGui.QPushButton(self.adminMenu)
        self.pushButton_12.setObjectName(_fromUtf8("pushButton_12"))
        self.verticalLayout_9.addWidget(self.pushButton_12)
        self.verticalLayout_4.addLayout(self.verticalLayout_9)
        spacerItem9 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem9)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.stackedWidget.addWidget(self.adminMenu)
        self.userMenu = QtGui.QWidget()
        self.userMenu.setObjectName(_fromUtf8("userMenu"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.userMenu)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.horizontalLayout_15 = QtGui.QHBoxLayout()
        self.horizontalLayout_15.setObjectName(_fromUtf8("horizontalLayout_15"))
        spacerItem10 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem10)
        self.label_12 = QtGui.QLabel(self.userMenu)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.horizontalLayout_15.addWidget(self.label_12)
        spacerItem11 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem11)
        self.verticalLayout_5.addLayout(self.horizontalLayout_15)
        self.pushButton_5 = QtGui.QPushButton(self.userMenu)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.verticalLayout_5.addWidget(self.pushButton_5)
        self.pushButton_6 = QtGui.QPushButton(self.userMenu)
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.verticalLayout_5.addWidget(self.pushButton_6)
        self.horizontalLayout_3.addLayout(self.verticalLayout_5)
        self.stackedWidget.addWidget(self.userMenu)
        self.pca = QtGui.QWidget()
        self.pca.setObjectName(_fromUtf8("pca"))
        self.verticalLayout_11 = QtGui.QVBoxLayout(self.pca)
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
        spacerItem12 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_11.addItem(spacerItem12)
        self.verticalLayout_10 = QtGui.QVBoxLayout()
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        spacerItem13 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem13)
        self.label_16 = QtGui.QLabel(self.pca)
        self.label_16.setText(_fromUtf8(""))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.horizontalLayout_11.addWidget(self.label_16)
        spacerItem14 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem14)
        self.label_17 = QtGui.QLabel(self.pca)
        self.label_17.setText(_fromUtf8(""))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.horizontalLayout_11.addWidget(self.label_17)
        spacerItem15 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem15)
        self.verticalLayout_10.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_22 = QtGui.QHBoxLayout()
        self.horizontalLayout_22.setObjectName(_fromUtf8("horizontalLayout_22"))
        spacerItem16 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_22.addItem(spacerItem16)
        self.label_20 = QtGui.QLabel(self.pca)
        self.label_20.setText(_fromUtf8(""))
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.horizontalLayout_22.addWidget(self.label_20)
        spacerItem17 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_22.addItem(spacerItem17)
        self.label_21 = QtGui.QLabel(self.pca)
        self.label_21.setText(_fromUtf8(""))
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.horizontalLayout_22.addWidget(self.label_21)
        spacerItem18 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_22.addItem(spacerItem18)
        self.verticalLayout_10.addLayout(self.horizontalLayout_22)
        self.verticalLayout_11.addLayout(self.verticalLayout_10)
        spacerItem19 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_11.addItem(spacerItem19)
        self.horizontalLayout_19 = QtGui.QHBoxLayout()
        self.horizontalLayout_19.setObjectName(_fromUtf8("horizontalLayout_19"))
        self.verticalLayout_12 = QtGui.QVBoxLayout()
        self.verticalLayout_12.setObjectName(_fromUtf8("verticalLayout_12"))
        self.horizontalLayout_20 = QtGui.QHBoxLayout()
        self.horizontalLayout_20.setObjectName(_fromUtf8("horizontalLayout_20"))
        self.label_18 = QtGui.QLabel(self.pca)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.horizontalLayout_20.addWidget(self.label_18)
        self.lineEdit_12 = QtGui.QLineEdit(self.pca)
        self.lineEdit_12.setObjectName(_fromUtf8("lineEdit_12"))
        self.horizontalLayout_20.addWidget(self.lineEdit_12)
        self.label_19 = QtGui.QLabel(self.pca)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.horizontalLayout_20.addWidget(self.label_19)
        self.lineEdit_13 = QtGui.QLineEdit(self.pca)
        self.lineEdit_13.setObjectName(_fromUtf8("lineEdit_13"))
        self.horizontalLayout_20.addWidget(self.lineEdit_13)
        self.verticalLayout_12.addLayout(self.horizontalLayout_20)
        self.pushButton_10 = QtGui.QPushButton(self.pca)
        self.pushButton_10.setObjectName(_fromUtf8("pushButton_10"))
        self.verticalLayout_12.addWidget(self.pushButton_10)
        self.horizontalLayout_19.addLayout(self.verticalLayout_12)
        self.verticalLayout_11.addLayout(self.horizontalLayout_19)
        self.stackedWidget.addWidget(self.pca)
        self.addUserMenu = QtGui.QWidget()
        self.addUserMenu.setObjectName(_fromUtf8("addUserMenu"))
        self.horizontalLayout_9 = QtGui.QHBoxLayout(self.addUserMenu)
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.verticalLayout_13 = QtGui.QVBoxLayout()
        self.verticalLayout_13.setObjectName(_fromUtf8("verticalLayout_13"))
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.label_5 = QtGui.QLabel(self.addUserMenu)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_13.addWidget(self.label_5)
        self.lineEdit_3 = QtGui.QLineEdit(self.addUserMenu)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.horizontalLayout_13.addWidget(self.lineEdit_3)
        self.verticalLayout_13.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_14 = QtGui.QHBoxLayout()
        self.horizontalLayout_14.setObjectName(_fromUtf8("horizontalLayout_14"))
        self.label_6 = QtGui.QLabel(self.addUserMenu)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_14.addWidget(self.label_6)
        self.lineEdit_4 = QtGui.QLineEdit(self.addUserMenu)
        self.lineEdit_4.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.horizontalLayout_14.addWidget(self.lineEdit_4)
        self.label_7 = QtGui.QLabel(self.addUserMenu)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_14.addWidget(self.label_7)
        self.lineEdit_5 = QtGui.QLineEdit(self.addUserMenu)
        self.lineEdit_5.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.horizontalLayout_14.addWidget(self.lineEdit_5)
        self.verticalLayout_13.addLayout(self.horizontalLayout_14)
        self.verticalLayout_14 = QtGui.QVBoxLayout()
        self.verticalLayout_14.setObjectName(_fromUtf8("verticalLayout_14"))
        self.fsm = QtGui.QFileSystemModel()
        self.index = self.fsm.setRootPath("databases")
        self.comboBox = QtGui.QComboBox(self.addUserMenu)
        self.comboBox.setModel(self.fsm)
        self.comboBox.setRootModelIndex(self.index)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.verticalLayout_14.addWidget(self.comboBox)
        self.verticalLayout_13.addLayout(self.verticalLayout_14)
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        spacerItem20 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem20)
        self.radioButton = QtGui.QRadioButton(self.addUserMenu)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.horizontalLayout_12.addWidget(self.radioButton)
        self.radioButton_2 = QtGui.QRadioButton(self.addUserMenu)
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.horizontalLayout_12.addWidget(self.radioButton_2)
        spacerItem21 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem21)
        self.verticalLayout_13.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_16 = QtGui.QHBoxLayout()
        self.horizontalLayout_16.setObjectName(_fromUtf8("horizontalLayout_16"))
        self.pushButton_7 = QtGui.QPushButton(self.addUserMenu)
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.horizontalLayout_16.addWidget(self.pushButton_7)
        self.pushButton_8 = QtGui.QPushButton(self.addUserMenu)
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.horizontalLayout_16.addWidget(self.pushButton_8)
        self.verticalLayout_13.addLayout(self.horizontalLayout_16)
        spacerItem22 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_13.addItem(spacerItem22)
        self.horizontalLayout_9.addLayout(self.verticalLayout_13)
        self.stackedWidget.addWidget(self.addUserMenu)
        self.addDBMenu = QtGui.QWidget()
        self.addDBMenu.setObjectName(_fromUtf8("addDBMenu"))
        self.horizontalLayout_17 = QtGui.QHBoxLayout(self.addDBMenu)
        self.horizontalLayout_17.setObjectName(_fromUtf8("horizontalLayout_17"))
        self.verticalLayout_15 = QtGui.QVBoxLayout()
        self.verticalLayout_15.setObjectName(_fromUtf8("verticalLayout_15"))
        self.horizontalLayout_18 = QtGui.QHBoxLayout()
        self.horizontalLayout_18.setObjectName(_fromUtf8("horizontalLayout_18"))
        spacerItem23 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem23)
        self.label_9 = QtGui.QLabel(self.addDBMenu)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_18.addWidget(self.label_9)
        spacerItem24 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem24)
        self.verticalLayout_15.addLayout(self.horizontalLayout_18)
        self.horizontalLayout_23 = QtGui.QHBoxLayout()
        self.horizontalLayout_23.setObjectName(_fromUtf8("horizontalLayout_23"))
        spacerItem25 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_23.addItem(spacerItem25)
        self.label_8 = QtGui.QLabel(self.addDBMenu)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_23.addWidget(self.label_8)
        self.lineEdit_6 = QtGui.QLineEdit(self.addDBMenu)
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.horizontalLayout_23.addWidget(self.lineEdit_6)
        spacerItem26 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_23.addItem(spacerItem26)
        self.verticalLayout_15.addLayout(self.horizontalLayout_23)
        self.horizontalLayout_21 = QtGui.QHBoxLayout()
        self.horizontalLayout_21.setObjectName(_fromUtf8("horizontalLayout_21"))
        self.pushButton_11 = QtGui.QPushButton(self.addDBMenu)
        self.pushButton_11.setObjectName(_fromUtf8("pushButton_11"))
        self.horizontalLayout_21.addWidget(self.pushButton_11)
        self.pushButton_9 = QtGui.QPushButton(self.addDBMenu)
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
        self.horizontalLayout_21.addWidget(self.pushButton_9)
        self.verticalLayout_15.addLayout(self.horizontalLayout_21)
        spacerItem27 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_15.addItem(spacerItem27)
        self.horizontalLayout_17.addLayout(self.verticalLayout_15)
        self.stackedWidget.addWidget(self.addDBMenu)
        self.editUserMenu = QtGui.QWidget()
        self.editUserMenu.setObjectName(_fromUtf8("editUserMenu"))
        self.horizontalLayout_25 = QtGui.QHBoxLayout(self.editUserMenu)
        self.horizontalLayout_25.setObjectName(_fromUtf8("horizontalLayout_25"))
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.horizontalLayout_27 = QtGui.QHBoxLayout()
        self.horizontalLayout_27.setObjectName(_fromUtf8("horizontalLayout_27"))
        spacerItem28 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_27.addItem(spacerItem28)
        self.label_10 = QtGui.QLabel(self.editUserMenu)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_27.addWidget(self.label_10)
        spacerItem29 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_27.addItem(spacerItem29)
        self.verticalLayout_7.addLayout(self.horizontalLayout_27)
        self.users_combo = QtGui.QComboBox(self.editUserMenu)
        self.users_combo.setObjectName(_fromUtf8("users_combo"))
        self.verticalLayout_7.addWidget(self.users_combo)
        self.dbs_combo = QtGui.QComboBox(self.editUserMenu)
        self.dbs_combo.setObjectName(_fromUtf8("dbs_combo"))
        self.verticalLayout_7.addWidget(self.dbs_combo)
        self.horizontalLayout_26 = QtGui.QHBoxLayout()
        self.horizontalLayout_26.setObjectName(_fromUtf8("horizontalLayout_26"))
        self.pushButton_15 = QtGui.QPushButton(self.editUserMenu)
        self.pushButton_15.setObjectName(_fromUtf8("pushButton_15"))
        self.horizontalLayout_26.addWidget(self.pushButton_15)
        self.verticalLayout_7.addLayout(self.horizontalLayout_26)
        spacerItem30 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem30)
        self.horizontalLayout_25.addLayout(self.verticalLayout_7)
        self.stackedWidget.addWidget(self.editUserMenu)
        self.verticalLayout.addWidget(self.stackedWidget)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "3BDB-FR", None))
        self.label.setText(_translate("Form", "Login", None))
        self.label_2.setText(_translate("Form", "User name", None))
        self.label_3.setText(_translate("Form", "Password", None))
        self.pushButton.setText(_translate("Form", "Login", None))
        self.label_4.setText(_translate("Form", "Administrator Options", None))
        self.pushButton_2.setText(_translate("Form", "Add Database", None))
        self.pushButton_3.setText(_translate("Form", "Add User", None))
        self.pushButton_4.setText(_translate("Form", "Edit User", None))
        self.pushButton_12.setText(_translate("Form", "Log Out", None))
        self.label_12.setText(_translate("Form", "Please Position Camera", None))
        self.pushButton_5.setText(_translate("Form", "Capture", None))
        self.pushButton_6.setText(_translate("Form", "Done", None))
        self.label_18.setText(_translate("Form", "DB Name", None))
        self.label_19.setText(_translate("Form", "User (1-40)", None))
        self.pushButton_10.setText(_translate("Form", "Test", None))
        self.label_5.setText(_translate("Form", "User name", None))
        self.label_6.setText(_translate("Form", "Password", None))
        self.label_7.setText(_translate("Form", "Re-enter Password", None))
        self.radioButton.setText(_translate("Form", "Administrator", None))
        self.radioButton_2.setText(_translate("Form", "User", None))
        self.pushButton_7.setText(_translate("Form", "Go Back", None))
        self.pushButton_8.setText(_translate("Form", "Add New User", None))
        self.label_9.setText(_translate("Form", "Add Database", None))
        self.label_8.setText(_translate("Form", "Database Name:", None))
        self.pushButton_11.setText(_translate("Form", "Go Back", None))
        self.pushButton_9.setText(_translate("Form", "Add Database", None))
        self.label_10.setText(_translate("Form", "Edit User", None))
        self.pushButton_15.setText(_translate("Form", "Add/Edit Pictures", None))

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
        if lines[0] == "admin":
            self.stackedWidget.setCurrentIndex(1)
        elif lines[0] == "user":
            self.stackedWidget.setCurrentIndex(2)
        else:
            QtGui.QMessageBox.warning(self, 'Not Found', 'Not Found')

    @QtCore.pyqtSignature("on_pushButton_2_clicked()")
    def gotoAddDBMenu(self):
        self.stackedWidget.setCurrentIndex(5)

    @QtCore.pyqtSignature("on_pushButton_9_clicked()")
    def createDatabaseMenu(self):
        name = str(self.lineEdit_6.text())
        os.system("python create_database.py " + "databases/" + name)
        lines = self.readContextFile()
        print lines
        if lines[0] == "database created":
            QtGui.QMessageBox.information(self, 'Success', 'Data Base ' + name + " created.")
        else:
            QtGui.QMessageBox.warning(self, 'Database not created', 'A database with that name already exists.')
        self.lineEdit_6.setText("")
        
    @QtCore.pyqtSignature("on_pushButton_11_clicked()")
    def gobacktoAdminMenu(self):
        self.stackedWidget.setCurrentIndex(1)

    @QtCore.pyqtSignature("on_pushButton_3_clicked()")
    def gotoAddUserMenu(self):
        self.stackedWidget.setCurrentIndex(4)

    @QtCore.pyqtSignature("on_pushButton_8_clicked()")
    def addUsermenu(self):
        # set up databases list
        
   
        user = str(self.lineEdit_3.text())
        password = str(self.lineEdit_4.text())
        reenteredPassword = str(self.lineEdit_5.text())
        
        if password != reenteredPassword:
            QtGui.QMessageBox.warning(self, 'Error', 'Passwords do not match.')
            return

        # check for privileges
        if self.radioButton.isChecked():
            privileges = "admin"
        elif self.radioButton_2.isChecked():
            privileges = "user"
        else:
            QtGui.QMessageBox.warning(self, 'Error', 'Please choose administrator or user.')
            return


        dbname = str(self.comboBox.currentText())
        os.system("python add_user.py " + user + ' ' + password + ' ' + privileges + ' ' + "databases/" + dbname)
        lines = self.readContextFile()
        if lines[0] == "user created":
            QtGui.QMessageBox.information(self, 'Success', 'User ' + user + " created.")
        else:
            QtGui.QMessageBox.warning(self, 'Error', 'Username already exists.')
        
    @QtCore.pyqtSignature("on_pushButton_4_clicked()")
    def removeUserMenu(self):
        username = str(self.lineEdit_9.text())
        dbname = str(self.lineEdit_8.text())
        os.system("python remove_user.py " + username + ' ' + dbname )
        lines = self.readContextFile()
        if lines[0] == "user removed":
            QtGui.QMessageBox.information(self, 'Success', 'User ' + username + " removed.")
        else:
            QtGui.QMessageBox.warning(self, 'Error', 'User not found.')
     
    @QtCore.pyqtSignature("on_pushButton_5_clicked()")
    def takePicturesUserMenu(self): 
        os.system("python camera.py 2")
        pixmap = QtGui.QPixmap("att_faces/s2/6.pgm")
        self.label_12.setPixmap(pixmap)
        self.label_12.show()
        self.pushButton_5.setText(_translate("3BDB-FR", "Re-Capture", None))

    @QtCore.pyqtSignature("on_pushButton_6_clicked()")
    def doneWithUserMenu(self):
        self.stackedWidget.setCurrentIndex(0)
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")

    @QtCore.pyqtSignature("on_pushButton_7_clicked()")
    def gobacktoMenu(self):
        self.stackedWidget.setCurrentIndex(1)
    
    def populateDbMenu(self):
        dbname = str(self.lineEdit_11.text())
        os.system("python populate_database.py " + dbname )
        self.lineEdit_11.setText("")

    def pcaMenu(self):
        dbname = str(self.lineEdit_10.text())
        os.system("python pca.py " + dbname )
        self.lineEdit_10.setText("")

    @QtCore.pyqtSignature("on_pushButton_10_clicked()")
    def testMenu(self):
        dbname = str(self.lineEdit_12.text())
        number = str(self.lineEdit_13.text())
        os.system("python test.py " + dbname + ' ' + number )
        with open("fr_results.txt") as f:
            lines = f.read().splitlines()
        file1 = lines[2]
        file2 = lines[3]
        pixmap1 = QtGui.QPixmap("att_faces/" + file1)
        pixmap2 = QtGui.QPixmap(dbname + '/' + file2)
        self.label_16.setPixmap(pixmap1)
        self.label_16.show()
        self.label_17.setPixmap(pixmap2)
        self.label_17.show()
        self.label_20.setText("Query")
        self.label_21.setText("Match")

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Ui_Form()
    ex.show()
    sys.exit(app.exec_())

