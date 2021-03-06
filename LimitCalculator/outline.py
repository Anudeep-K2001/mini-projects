# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'outline.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(571, 183)
        MainWindow.setStyleSheet("background:rgb(245,245,245)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 801, 561))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(160, 20, 113, 22))
        self.lineEdit.setStyleSheet("background:rgb(255,255,255);")
        self.lineEdit.setObjectName("lineEdit")
        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(340, 90, 191, 18))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.targetVal = QtWidgets.QLabel(self.layoutWidget)
        self.targetVal.setText("")
        self.targetVal.setObjectName("targetVal")
        self.horizontalLayout.addWidget(self.targetVal)
        self.stopLossVal = QtWidgets.QLabel(self.layoutWidget)
        self.stopLossVal.setText("")
        self.stopLossVal.setObjectName("stopLossVal")
        self.horizontalLayout.addWidget(self.stopLossVal)
        self.layoutWidget1 = QtWidgets.QWidget(self.frame)
        self.layoutWidget1.setGeometry(QtCore.QRect(340, 120, 195, 32))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.buy = QtWidgets.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.buy.setFont(font)
        self.buy.setStyleSheet("background:rgb(85, 170, 255);\n"
"color:rgb(245,245,245);")
        self.buy.setObjectName("buy")
        self.horizontalLayout_2.addWidget(self.buy)
        self.sell = QtWidgets.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.sell.setFont(font)
        self.sell.setStyleSheet("background:rgb(255, 93, 93);\n"
"color:rgb(245,245,245);")
        self.sell.setObjectName("sell")
        self.horizontalLayout_2.addWidget(self.sell)
        self.layoutWidget2 = QtWidgets.QWidget(self.frame)
        self.layoutWidget2.setGeometry(QtCore.QRect(340, 20, 75, 51))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(9)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_3.addWidget(self.label_7)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(9)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(30, 47, 71, 20))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(9)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 45, 113, 22))
        self.lineEdit_2.setStyleSheet("background:rgb(255,255,255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(30, 22, 40, 18))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(31, 134, 88, 18))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(31, 81, 48, 18))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(31, 108, 72, 18))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.layoutWidget3 = QtWidgets.QWidget(self.frame)
        self.layoutWidget3.setGeometry(QtCore.QRect(161, 81, 111, 71))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.target = QtWidgets.QLabel(self.layoutWidget3)
        self.target.setText("")
        self.target.setObjectName("target")
        self.verticalLayout.addWidget(self.target)
        self.stopLoss = QtWidgets.QLabel(self.layoutWidget3)
        self.stopLoss.setText("")
        self.stopLoss.setObjectName("stopLoss")
        self.verticalLayout.addWidget(self.stopLoss)
        self.totalValue = QtWidgets.QLabel(self.layoutWidget3)
        self.totalValue.setText("")
        self.totalValue.setObjectName("totalValue")
        self.verticalLayout.addWidget(self.totalValue)
        self.layoutWidget4 = QtWidgets.QWidget(self.frame)
        self.layoutWidget4.setGeometry(QtCore.QRect(410, 20, 61, 51))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.PROFIT = QtWidgets.QLabel(self.layoutWidget4)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.PROFIT.setFont(font)
        self.PROFIT.setStyleSheet("color:rgb(71, 255, 169);")
        self.PROFIT.setText("")
        self.PROFIT.setObjectName("PROFIT")
        self.verticalLayout_4.addWidget(self.PROFIT)
        self.LOSS = QtWidgets.QLabel(self.layoutWidget4)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.LOSS.setFont(font)
        self.LOSS.setStyleSheet("color:rgb(255, 89, 89);")
        self.LOSS.setText("")
        self.LOSS.setObjectName("LOSS")
        self.verticalLayout_4.addWidget(self.LOSS)
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(470, 20, 69, 51))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout_2.addWidget(self.lineEdit_3)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout_2.addWidget(self.lineEdit_4)
        self.widget1 = QtWidgets.QWidget(self.frame)
        self.widget1.setGeometry(QtCore.QRect(540, 20, 21, 51))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.widget1)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_5.addWidget(self.label_5)
        self.label_9 = QtWidgets.QLabel(self.widget1)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_5.addWidget(self.label_9)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 571, 26))
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
        self.buy.setText(_translate("MainWindow", "Buy"))
        self.sell.setText(_translate("MainWindow", "Sell"))
        self.label_7.setText(_translate("MainWindow", "Profit"))
        self.label_6.setText(_translate("MainWindow", "Loss"))
        self.label_8.setText(_translate("MainWindow", "Quantity"))
        self.label.setText(_translate("MainWindow", "Price"))
        self.label_4.setText(_translate("MainWindow", "Total value"))
        self.label_2.setText(_translate("MainWindow", "Target"))
        self.label_3.setText(_translate("MainWindow", "Stop Loss"))
        self.label_5.setText(_translate("MainWindow", "%"))
        self.label_9.setText(_translate("MainWindow", "%"))
