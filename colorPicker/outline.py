# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\Anudeep\GUI\colorPicker\outline.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(367, 198)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-20, -30, 521, 371))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(20, 30, 371, 251))
        self.frame_2.setStyleSheet("background-color: rgb(0,0,0);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.dial_red = QtWidgets.QDial(self.frame_2)
        self.dial_red.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.dial_red.setMaximum(255)
        self.dial_red.setObjectName("dial_red")
        self.horizontalLayout.addWidget(self.dial_red)
        self.dial_green = QtWidgets.QDial(self.frame_2)
        self.dial_green.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.dial_green.setMaximum(255)
        self.dial_green.setObjectName("dial_green")
        self.horizontalLayout.addWidget(self.dial_green)
        self.dial_blue = QtWidgets.QDial(self.frame_2)
        self.dial_blue.setStyleSheet("background-color: rgb(0, 0, 255);")
        self.dial_blue.setMaximum(255)
        self.dial_blue.setObjectName("dial_blue")
        self.horizontalLayout.addWidget(self.dial_blue)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.spinBox_red = QtWidgets.QSpinBox(self.frame_3)
        self.spinBox_red.setGeometry(QtCore.QRect(20, 1, 80, 22))
        self.spinBox_red.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.spinBox_red.setMaximum(255)
        self.spinBox_red.setObjectName("spinBox_red")
        self.spinBox_green = QtWidgets.QSpinBox(self.frame_3)
        self.spinBox_green.setGeometry(QtCore.QRect(140, 0, 80, 22))
        self.spinBox_green.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.spinBox_green.setMaximum(255)
        self.spinBox_green.setObjectName("spinBox_green")
        self.spinBox_blue = QtWidgets.QSpinBox(self.frame_3)
        self.spinBox_blue.setGeometry(QtCore.QRect(260, 1, 80, 22))
        self.spinBox_blue.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.spinBox_blue.setMaximum(255)
        self.spinBox_blue.setObjectName("spinBox_blue")
        self.gridLayout.addWidget(self.frame_3, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 367, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

