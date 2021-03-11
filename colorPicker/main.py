import sys
from PyQt5 import QtWidgets
import random

import outline

class main(outline.Ui_MainWindow, QtWidgets.QMainWindow):

    def __init__(self):
        super(main, self).__init__()
        self.setupUi(self)



        self.red = self.randomNumber()
        self.green = self.randomNumber()
        self.blue = self.randomNumber()

        
        self.spinBox_red.setValue(self.red)
        self.spinBox_green.setValue(self.green)
        self.spinBox_blue.setValue(self.blue)

        self.dial_red.setValue(self.red)
        self.dial_green.setValue(self.green)
        self.dial_blue.setValue(self.blue)

        self.colorChange()

        self.dial_red.valueChanged.connect(self.changeRedDial)
        self.dial_green.valueChanged.connect(self.changeGreenDial)
        self.dial_blue.valueChanged.connect(self.changeBlueDial)

        self.spinBox_red.valueChanged.connect(self.changeRedBox)
        self.spinBox_green.valueChanged.connect(self.changeGreenBox)
        self.spinBox_blue.valueChanged.connect(self.changeBlueBox)


    def changeRedDial(self):
        self.red = self.dial_red.value()
        self.spinBox_red.setValue(self.red)
        self.colorChange()
        return


    def changeGreenDial(self):
        self.green = self.dial_green.value()
        self.spinBox_green.setValue(self.green)
        self.colorChange()
        return


    def changeBlueDial(self):
        self.blue = self.dial_blue.value()
        self.spinBox_blue.setValue(self.blue)
        self.colorChange()
        return


    def changeRedBox(self):
        self.red = self.spinBox_red.value()
        self.dial_red.setValue(self.red)
        self.colorChange()
        return


    def changeGreenBox(self):
        self.green = self.spinBox_green.value()
        self.dial_green.setValue(self.green)
        self.colorChange()
        return


    def changeBlueBox(self):
        self.blue = self.spinBox_blue.value()
        self.dial_blue.setValue(self.blue)
        self.colorChange()
        return

    
    def colorChange(self):
        self.frame_2.setStyleSheet(f"background-color: rgb({self.red},{self.green},{self.blue});")
        return


    def randomNumber(self):
        return random.randint(0,255)

    
    

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    qt_app = main()
    qt_app.show()
    app.exec_()