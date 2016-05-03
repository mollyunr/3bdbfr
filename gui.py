#!/usr/bin/python

import sys
import os
import datetime
import time
import results
import camera
import processImages
import create_database
import add_user
import remove_user
import login
import pca
import test
import shutil
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
        self.threshold = 0.6
        self.resultText = ""
        self.currentDatabase = "user_database"

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(776, 485)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.stackedWidget = QtGui.QStackedWidget(Form)
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))

        ########## LOGIN #####################
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
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
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
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_5.addWidget(self.label_2)
        self.lineEdit = QtGui.QLineEdit(self.login)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.lineEdit.setFont(font)
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
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_7.addWidget(self.label_3)
        self.lineEdit_2 = QtGui.QLineEdit(self.login)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.horizontalLayout_7.addWidget(self.lineEdit_2)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem5)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.pushButton = QtGui.QPushButton(self.login)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_6.addWidget(self.pushButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        spacerItem6 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem6)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.stackedWidget.addWidget(self.login)


        #######  ADMIN MENU #################
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
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.verticalLayout_8.addWidget(self.pushButton_2)
        self.verticalLayout_4.addLayout(self.verticalLayout_8)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.pushButton_3 = QtGui.QPushButton(self.adminMenu)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.horizontalLayout_10.addWidget(self.pushButton_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_24 = QtGui.QHBoxLayout()
        self.horizontalLayout_24.setObjectName(_fromUtf8("horizontalLayout_24"))
        self.pushButton_4 = QtGui.QPushButton(self.adminMenu)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.horizontalLayout_24.addWidget(self.pushButton_4)
        self.verticalLayout_4.addLayout(self.horizontalLayout_24)
        self.pushButton_19 = QtGui.QPushButton(self.adminMenu)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pushButton_19.setFont(font)
        self.pushButton_19.setObjectName(_fromUtf8("pushButton_19"))
        #self.verticalLayout_4.addWidget(self.pushButton_19)
        self.verticalLayout_9 = QtGui.QVBoxLayout()
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.pushButton_12 = QtGui.QPushButton(self.adminMenu)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setObjectName(_fromUtf8("pushButton_12"))
        #self.verticalLayout_9.addWidget(self.pushButton_12)
        self.verticalLayout_4.addLayout(self.verticalLayout_9)
        spacerItem9 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem9)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.stackedWidget.addWidget(self.adminMenu)

        ######## USER MENU ############
        self.userMenu = QtGui.QWidget()
        self.userMenu.setObjectName(_fromUtf8("userMenu"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.userMenu)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.label_12 = QtGui.QLabel(self.userMenu)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.verticalLayout_5.addWidget(self.label_12)
        self.pushButton_5 = QtGui.QPushButton(self.userMenu)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.verticalLayout_5.addWidget(self.pushButton_5)
        self.pushButton_6 = QtGui.QPushButton(self.userMenu)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.verticalLayout_5.addWidget(self.pushButton_6)
        #self.verticalLayout_5.addWidget(self.pushButton_12)
        self.horizontalLayout_3.addLayout(self.verticalLayout_5)
        self.stackedWidget.addWidget(self.userMenu)

        ####### THRESHOLD #################
        self.threshold = QtGui.QWidget()
        self.threshold.setObjectName(_fromUtf8("threshold"))
        self.verticalLayout_11 = QtGui.QVBoxLayout(self.threshold)
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
        self.verticalLayout_10 = QtGui.QVBoxLayout()
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        spacerItem10 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem10)
        self.label_13 = QtGui.QLabel(self.threshold)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.verticalLayout_10.addWidget(self.label_13)
        self.horizontalSlider = QtGui.QSlider(self.threshold)
        self.horizontalSlider.setMaximum(20000)
        self.horizontalSlider.setSingleStep(250)
        self.horizontalSlider.setProperty("value", 5000)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName(_fromUtf8("horizontalSlider"))
        self.verticalLayout_10.addWidget(self.horizontalSlider)
        self.pushButton_10 = QtGui.QPushButton(self.threshold)
        self.pushButton_10.setObjectName(_fromUtf8("pushButton_10"))
        self.verticalLayout_10.addWidget(self.pushButton_10)
        spacerItem11 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem11)
        self.verticalLayout_11.addLayout(self.verticalLayout_10)
        self.stackedWidget.addWidget(self.threshold)

        ####### ADD USER ##################
        self.addUserMenu = QtGui.QWidget()
        self.addUserMenu.setObjectName(_fromUtf8("addUserMenu"))
        self.horizontalLayout_9 = QtGui.QHBoxLayout(self.addUserMenu)
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.verticalLayout_13 = QtGui.QVBoxLayout()
        self.verticalLayout_13.setObjectName(_fromUtf8("verticalLayout_13"))
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.label_5 = QtGui.QLabel(self.addUserMenu)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_13.addWidget(self.label_5)
        self.lineEdit_3 = QtGui.QLineEdit(self.addUserMenu)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.horizontalLayout_13.addWidget(self.lineEdit_3)
        self.verticalLayout_13.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_14 = QtGui.QHBoxLayout()
        self.horizontalLayout_14.setObjectName(_fromUtf8("horizontalLayout_14"))
        self.label_6 = QtGui.QLabel(self.addUserMenu)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_14.addWidget(self.label_6)
        self.lineEdit_4 = QtGui.QLineEdit(self.addUserMenu)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.horizontalLayout_14.addWidget(self.lineEdit_4)
        self.label_7 = QtGui.QLabel(self.addUserMenu)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_14.addWidget(self.label_7)
        self.lineEdit_5 = QtGui.QLineEdit(self.addUserMenu)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.lineEdit_5.setFont(font)
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
        font = QtGui.QFont()
        font.setPointSize(22)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.verticalLayout_14.addWidget(self.comboBox)
        self.verticalLayout_13.addLayout(self.verticalLayout_14)
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        spacerItem20 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem20)
        self.radioButton = QtGui.QRadioButton(self.addUserMenu)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.horizontalLayout_12.addWidget(self.radioButton)
        self.radioButton_2 = QtGui.QRadioButton(self.addUserMenu)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.horizontalLayout_12.addWidget(self.radioButton_2)
        spacerItem21 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem21)
        self.verticalLayout_13.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_16 = QtGui.QHBoxLayout()
        self.horizontalLayout_16.setObjectName(_fromUtf8("horizontalLayout_16"))
        self.pushButton_7 = QtGui.QPushButton(self.addUserMenu)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.horizontalLayout_16.addWidget(self.pushButton_7)
        self.pushButton_8 = QtGui.QPushButton(self.addUserMenu)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.horizontalLayout_16.addWidget(self.pushButton_8)
        self.verticalLayout_13.addLayout(self.horizontalLayout_16)
        spacerItem22 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_13.addItem(spacerItem22)
        self.horizontalLayout_9.addLayout(self.verticalLayout_13)
        self.stackedWidget.addWidget(self.addUserMenu)

        ######### EDIT DATABASE ##########################
        self.addDBMenu = QtGui.QWidget()
        self.addDBMenu.setObjectName(_fromUtf8("addDBMenu"))
        self.horizontalLayout_17 = QtGui.QHBoxLayout(self.addDBMenu)
        self.horizontalLayout_17.setObjectName(_fromUtf8("horizontalLayout_17"))
        self.verticalLayout_15 = QtGui.QVBoxLayout()
        self.verticalLayout_15.setObjectName(_fromUtf8("verticalLayout_15"))
        self.horizontalLayout_18 = QtGui.QHBoxLayout()
        self.horizontalLayout_18.setObjectName(_fromUtf8("horizontalLayout_18"))
        spacerItem15 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem15)
        self.label_9 = QtGui.QLabel(self.addDBMenu)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setPointSize(22)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_18.addWidget(self.label_9)
        spacerItem16 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem16)
        self.verticalLayout_15.addLayout(self.horizontalLayout_18)
        self.horizontalLayout_23 = QtGui.QHBoxLayout()
        self.horizontalLayout_23.setObjectName(_fromUtf8("horizontalLayout_23"))
        self.label_8 = QtGui.QLabel(self.addDBMenu)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_23.addWidget(self.label_8)
        self.lineEdit_6 = QtGui.QLineEdit(self.addDBMenu)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.horizontalLayout_23.addWidget(self.lineEdit_6)
        self.pushButton_9 = QtGui.QPushButton(self.addDBMenu)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
        self.horizontalLayout_23.addWidget(self.pushButton_9)
        self.verticalLayout_15.addLayout(self.horizontalLayout_23)
        spacerItem17 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_15.addItem(spacerItem17)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.label_14 = QtGui.QLabel(self.addDBMenu)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setPointSize(22)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.horizontalLayout_11.addWidget(self.label_14)
        self.verticalLayout_15.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_15 = QtGui.QHBoxLayout()
        self.horizontalLayout_15.setObjectName(_fromUtf8("horizontalLayout_15"))

        self.comboBox_2 = QtGui.QComboBox(self.addDBMenu)
        self.comboBox_2.setModel(self.fsm)
        self.comboBox_2.setRootModelIndex(self.index)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.horizontalLayout_15.addWidget(self.comboBox_2)

        self.verticalLayout_15.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_21 = QtGui.QHBoxLayout()
        self.horizontalLayout_21.setObjectName(_fromUtf8("horizontalLayout_21"))
        self.pushButton_11 = QtGui.QPushButton(self.addDBMenu)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setObjectName(_fromUtf8("pushButton_11"))
        self.horizontalLayout_21.addWidget(self.pushButton_11)
        self.verticalLayout_15.addLayout(self.horizontalLayout_21)
        spacerItem18 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_15.addItem(spacerItem18)
        self.horizontalLayout_17.addLayout(self.verticalLayout_15)
        self.stackedWidget.addWidget(self.addDBMenu)

        ########### EDIT USER ###########################
        self.editUserMenu = QtGui.QWidget()
        self.editUserMenu.setObjectName(_fromUtf8("editUserMenu"))
        self.horizontalLayout_25 = QtGui.QHBoxLayout(self.editUserMenu)
        self.horizontalLayout_25.setObjectName(_fromUtf8("horizontalLayout_25"))
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.horizontalLayout_27 = QtGui.QHBoxLayout()
        self.horizontalLayout_27.setObjectName(_fromUtf8("horizontalLayout_27"))
        spacerItem26 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_27.addItem(spacerItem26)
        self.label_10 = QtGui.QLabel(self.editUserMenu)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_27.addWidget(self.label_10)
        spacerItem27 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_27.addItem(spacerItem27)
        self.verticalLayout_7.addLayout(self.horizontalLayout_27)
        self.dbs_combo = QtGui.QComboBox(self.editUserMenu)

        self.dbs_combo.setModel(self.fsm)
        self.dbs_combo.setRootModelIndex(self.index)

        font = QtGui.QFont()
        font.setPointSize(22)
        self.dbs_combo.setFont(font)
        self.dbs_combo.setObjectName(_fromUtf8("dbs_combo"))
        self.verticalLayout_7.addWidget(self.dbs_combo)
        self.users_combo = QtGui.QComboBox(self.editUserMenu)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.users_combo.setFont(font)
        self.users_combo.setObjectName(_fromUtf8("users_combo"))
        self.verticalLayout_7.addWidget(self.users_combo)
        self.horizontalLayout_26 = QtGui.QHBoxLayout()
        self.horizontalLayout_26.setObjectName(_fromUtf8("horizontalLayout_26"))
        self.pushButton_15 = QtGui.QPushButton(self.editUserMenu)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setObjectName(_fromUtf8("pushButton_15"))
        self.horizontalLayout_26.addWidget(self.pushButton_15)
        self.verticalLayout_7.addLayout(self.horizontalLayout_26)
        self.pushButton_16 = QtGui.QPushButton(self.editUserMenu)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setObjectName(_fromUtf8("pushButton_16"))
        self.verticalLayout_7.addWidget(self.pushButton_16)
        self.pushButton_17 = QtGui.QPushButton(self.editUserMenu)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pushButton_17.setFont(font)
        self.pushButton_17.setObjectName(_fromUtf8("pushButton_17"))
        self.verticalLayout_7.addWidget(self.pushButton_17)
        spacerItem28 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem28)
        self.horizontalLayout_25.addLayout(self.verticalLayout_7)
        self.stackedWidget.addWidget(self.editUserMenu)

        ############# ADD PICTURES #################
        self.takePictures = QtGui.QWidget()
        self.takePictures.setObjectName(_fromUtf8("takePictures"))
        self.horizontalLayout_28 = QtGui.QHBoxLayout(self.takePictures)
        self.horizontalLayout_28.setObjectName(_fromUtf8("horizontalLayout_28"))
        self.verticalLayout_16 = QtGui.QVBoxLayout()
        self.verticalLayout_16.setObjectName(_fromUtf8("verticalLayout_16"))
        self.horizontalLayout_29 = QtGui.QHBoxLayout()
        self.horizontalLayout_29.setObjectName(_fromUtf8("horizontalLayout_29"))
        self.label_11 = QtGui.QLabel(self.takePictures)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout_29.addWidget(self.label_11)
        self.verticalLayout_16.addLayout(self.horizontalLayout_29)
        self.pushButton_13 = QtGui.QPushButton(self.takePictures)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setObjectName(_fromUtf8("pushButton_13"))
        self.verticalLayout_16.addWidget(self.pushButton_13)
        self.pushButton_18 = QtGui.QPushButton(self.takePictures)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pushButton_18.setFont(font)
        self.pushButton_18.setObjectName(_fromUtf8("pushButton_18"))
        self.verticalLayout_16.addWidget(self.pushButton_18)
        self.pushButton_14 = QtGui.QPushButton(self.takePictures)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setObjectName(_fromUtf8("pushButton_14"))
        self.verticalLayout_16.addWidget(self.pushButton_14)
        self.horizontalLayout_28.addLayout(self.verticalLayout_16)
        self.stackedWidget.addWidget(self.takePictures)


        self.verticalLayout.addWidget(self.stackedWidget)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "3BDB-FR", None))
        self.label.setText(_translate("Form", "3BDB-FR", None))
        self.label_2.setText(_translate("Form", "Username", None))
        self.label_3.setText(_translate("Form", "Password", None))
        self.pushButton.setText(_translate("Form", "Login", None))
        self.label_4.setText(_translate("Form", "Administrator Options", None))
        self.pushButton_2.setText(_translate("Form", "Edit Databases", None))
        self.pushButton_3.setText(_translate("Form", "Add User", None))
        self.pushButton_4.setText(_translate("Form", "Edit User", None))
        self.pushButton_19.setText(_translate("Form", "Adjust Threshold", None))
        self.pushButton_12.setText(_translate("Form", "Log Out", None))
        self.label_12.setText(_translate("Form", "Get ready and then press capture", None))
        self.pushButton_5.setText(_translate("Form", "Capture", None))
        self.pushButton_6.setText(_translate("Form", "Done", None))
        self.label_13.setText(_translate("Form", "Adjust Threshold", None))
        self.pushButton_10.setText(_translate("Form", "Set", None))
        self.label_5.setText(_translate("Form", "Username", None))
        self.label_6.setText(_translate("Form", "Password", None))
        self.label_7.setText(_translate("Form", "Re-enter Password", None))
        self.comboBox.setItemText(0, _translate("Form", "user_database", None))
        self.radioButton.setText(_translate("Form", "Administrator", None))
        self.radioButton_2.setText(_translate("Form", "User", None))
        self.pushButton_7.setText(_translate("Form", "Go Back", None))
        self.pushButton_8.setText(_translate("Form", "Add New User", None))
        self.label_9.setText(_translate("Form", "Create New Database", None))
        self.label_8.setText(_translate("Form", "Database Name:", None))
        self.pushButton_9.setText(_translate("Form", "Create Database", None))
        self.label_14.setText(_translate("Form", "Set Current Database", None))
        self.pushButton_11.setText(_translate("Form", "Done", None))
        self.label_10.setText(_translate("Form", "Edit User", None))
        self.pushButton_15.setText(_translate("Form", "Change Pictures", None))
        self.pushButton_16.setText(_translate("Form", "Remove User", None))
        self.pushButton_17.setText(_translate("Form", "Back", None))
        self.label_11.setText(_translate("Form", "Get ready, then press Capture", None))
        self.pushButton_13.setText(_translate("Form", "Capture", None))
        self.pushButton_18.setText(_translate("Form", "Done", None))
        self.pushButton_14.setText(_translate("Form", "Cancel", None))
        
        self.reset()

    def reset(self):
        self.pushButton_5.setEnabled(True)
        self.pushButton_6.setEnabled(False)
        self.pushButton_18.setEnabled(False)
        self.label_12.setText(_translate("Form", "Get ready and then press capture", None))
        self.pushButton_5.setText(_translate("3BDB-FR", "Capture", None))
        self.label_11.setText(_translate("Form", "Get ready, then press Capture", None))
        self.pushButton_13.setText(_translate("3BDB-FR", "Capture", None))
        self.pushButton_18.setText(_translate("3BDB-FR", "Add Pictures", None))

    def readContextFile(self):
        with open("context.txt") as f:
            lines = f.read().splitlines()
        return lines

    @QtCore.pyqtSlot(str)
    def on_dbs_combo_currentIndexChanged(self, index):
        database = self.dbs_combo.currentText()
        print database
        fsm = QtGui.QFileSystemModel()
        index = fsm.setRootPath("databases/" + database)
        self.users_combo.setModel(fsm)
        self.users_combo.setRootModelIndex(index)

    @QtCore.pyqtSignature("on_pushButton_clicked()")
    def loginMenu(self):
        username = str(self.lineEdit.text())
        password = str(self.lineEdit_2.text())
        if username == '' or password == '':
            QtGui.QMessageBox.warning(self, 'Error', 'Please enter a username & password.')
            return;

        attempt = login.attemptLogin(self.currentDatabase, username, password)
        if attempt == "Not Found.":
            QtGui.QMessageBox.warning(self, 'Error', attempt)
            return
        elif attempt == "Password is incorrect.":
            QtGui.QMessageBox.warning(self, 'Error', attempt)
            return
        elif attempt == "admin":
            self.stackedWidget.setCurrentIndex(1)
            self.verticalLayout_9.addWidget(self.pushButton_12)
        elif attempt == "user":
            self.stackedWidget.setCurrentIndex(2)
            self.verticalLayout_5.addWidget(self.pushButton_12)

    @QtCore.pyqtSignature("on_pushButton_2_clicked()")
    def gotoAddDBMenu(self):
        self.stackedWidget.setCurrentIndex(5)

    @QtCore.pyqtSignature("on_pushButton_9_clicked()")
    def createDatabaseMenu(self):
        # check if valid db name
        name = str(self.lineEdit_6.text())
        if len(name) < 1:
            QtGui.QMessageBox.warning(self, 'Database not created', 'Database must contain at least 1 character')
            return

        # create database
        success = create_database.create(name)
        if success == True:
            QtGui.QMessageBox.information(self, 'Success', 'Data Base ' + name + " created.")
        else:
            QtGui.QMessageBox.warning(self, 'Database not created', 'A database with that name already exists.')

        # reset
        self.lineEdit_6.setText("")
        
    @QtCore.pyqtSignature("on_pushButton_11_clicked()")
    def gobacktoAdminMenu(self):
        # change selected database
        self.currentDatabase = str(self.comboBox_2.currentText()).strip('/')
        print self.currentDatabase        
        self.stackedWidget.setCurrentIndex(1)

    @QtCore.pyqtSignature("on_pushButton_3_clicked()")
    def gotoAddUserMenu(self):
        self.stackedWidget.setCurrentIndex(4)

    @QtCore.pyqtSignature("on_pushButton_8_clicked()")
    def addUsermenu(self):
        # check username
        user = str(self.lineEdit_3.text())
        if len(user) < 2:
            QtGui.QMessageBox.warning(self, 'Error', 'Username must contain at least 2 characters')
            return

        # check password
        password = str(self.lineEdit_4.text())
        reenteredPassword = str(self.lineEdit_5.text())
        if password != reenteredPassword:
            QtGui.QMessageBox.warning(self, 'Error', 'Passwords do not match.')
            return
        elif len(password) < 4:
            QtGui.QMessageBox.warning(self, 'Error', 'Password must contain at least 4 characters.')
            return

        # check for privileges
        if self.radioButton.isChecked():
            privileges = "admin"
        elif self.radioButton_2.isChecked():
            privileges = "user"
        else:
            QtGui.QMessageBox.warning(self, 'Error', 'Please choose administrator or user.')
            return

        # check database
        dbname = str(self.comboBox.currentText())
        if dbname == '/':
            QtGui.QMessageBox.warning(self, 'Error', 'Please choose database.')
            return

        # add the user
        success = add_user.add(user, password, privileges, dbname)
        if success == True:
            QtGui.QMessageBox.information(self, 'Success', 'User ' + user + " created.")
        else:
            QtGui.QMessageBox.warning(self, 'Error', 'Username already exists.')
        
    @QtCore.pyqtSignature("on_pushButton_4_clicked()")
    def gotoEditUserMenu(self):
        self.stackedWidget.setCurrentIndex(6)
     
    @QtCore.pyqtSignature("on_pushButton_5_clicked()")
    def takePicturesUserMenu(self):
        if not os.path.exists("test/testUser"):
            os.mkdir("test/testUser")
        camera.savePictures("test/testUser")
        pixmap = QtGui.QPixmap("test/testUser/4.png")
        width = self.label_12.width()
        height = self.label_12.height()
        self.label_12.setPixmap(pixmap.scaled(width, height, QtCore.Qt.KeepAspectRatio))
        self.label_12.show()
        self.pushButton_5.setText(_translate("3BDB-FR", "Re-Capture", None))
        self.pushButton_6.setEnabled(True)

    @QtCore.pyqtSignature("on_pushButton_6_clicked()")
    def doneCapturingPictures(self):
        self.pushButton_5.setEnabled(False)
        self.pushButton_6.setEnabled(False)
        username = str(self.lineEdit.text())
        test.testPCA("test/testUser", "databases/user_database", username)
        resultText = results.getResults(self.threshold);
        if resultText == "pass":
            resultText = "Welcome " + username + '!'
        else:
            resultText = "Verification of identity was not met.\n An administrator will be notified."
        self.label_12.setText(_translate("Form", resultText, None))
        if os.path.exists("test/testUser"):
            shutil.rmtree("test/testUser")

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
    def setThreshold(self):
        print self.horizontalSlider.tickPosition()

    @QtCore.pyqtSignature("on_pushButton_12_clicked()")
    def logout(self):
        f = open('context.txt', 'w')
        f.write('')
        self.reset()
        self.stackedWidget.setCurrentIndex(0)
        self.lineEdit.setText('')
        self.lineEdit_2.setText('')    

    @QtCore.pyqtSignature("on_pushButton_13_clicked()")
    def takeInitialPictures(self):
        dbname = str(self.dbs_combo.currentText())
        username = str(self.users_combo.currentText())
        directory = "databases/" + dbname + '/' + username + "/temp"

        if os.path.exists(directory):
            shutil.rmtree(directory)
        
        os.mkdir(directory)
        camera.savePictures(directory)
        processImages.crop(directory)
        processImages.deletePictures(directory, ".png")
        pixmap = QtGui.QPixmap(directory + "/5.pgm")
        width = self.label_11.width()
        height = self.label_11.height()
        self.label_11.setPixmap(pixmap.scaled(width, height, QtCore.Qt.KeepAspectRatio))
        self.label_11.show()
        self.pushButton_13.setText(_translate("3BDB-FR", "Re-Capture", None))
        self.pushButton_18.setEnabled(True)

    @QtCore.pyqtSignature("on_pushButton_14_clicked()")
    def cancelTakingPictures(self):
        dbname = str(self.dbs_combo.currentText())
        username = str(self.users_combo.currentText())
        directory = "databases/" + dbname + '/' + username
        if os.path.exists(directory + '/temp'):
            shutil.rmtree(directory + '/temp')
        self.stackedWidget.setCurrentIndex(6)
        self.reset()

    @QtCore.pyqtSignature("on_pushButton_15_clicked()")
    def gotoTakePictures(self):
        self.stackedWidget.setCurrentIndex(7)

    @QtCore.pyqtSignature("on_pushButton_16_clicked()")
    def removeUserMenu(self):
        # check if database selected
        dbname = str(self.dbs_combo.currentText())
        if dbname == '/':
            QtGui.QMessageBox.warning(self, 'Error', 'Please choose a database.')
            return
    
        # check if user selected
        username = str(self.users_combo.currentText())
        if username == '/':
            QtGui.QMessageBox.warning(self, 'Error', 'Please choose a user to remove.')
            return
        
        if add_user.findUser(username, dbname):
            reply = QtGui.QMessageBox.question(self,"Are you sure?", "Are you sure you want to remove " + username + '?', QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
            if reply == QtGui.QMessageBox.Yes:
                success = remove_user.remove(username, dbname)
                if success == True:
                    QtGui.QMessageBox.information(self, 'Success', 'User ' + username + " removed.")
                else:
                    QtGui.QMessageBox.warning(self, 'Error', 'User not found.')
        else:
            QtGui.QMessageBox.warning(self, 'Error', 'User not found.')

    @QtCore.pyqtSignature("on_pushButton_17_clicked()")
    def wrapper(self):
        self.gobacktoMenu()

    @QtCore.pyqtSignature("on_pushButton_18_clicked()")
    def movePicturesToUserFile(self):
        dbname = str(self.dbs_combo.currentText())
        username = str(self.users_combo.currentText())
        directory = "databases/" + dbname + '/' + username
        for index in range(3,13):
            shutil.move(directory + "/temp/" + str(index) + ".pgm", directory + '/' + str(index) + ".pgm")
        if os.path.exists(directory + '/temp'):
            shutil.rmtree(directory + '/temp')
        pca.runPCA(dbname)
        self.reset()
        self.gobacktoMenu()

    @QtCore.pyqtSignature("on_pushButton_19_clicked()")
    def gotoThreshold(self):
        self.stackedWidget.setCurrentIndex(3)

class TaskThread(QtCore.QThread):
    notifyProgress = QtCore.pyqtSignal(int)
    def run(self):
        for i in range(101):
            self.notifyProgress.emit(i)
            time.sleep(0.1)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Ui_Form()
    ex.show()
    sys.exit(app.exec_())

