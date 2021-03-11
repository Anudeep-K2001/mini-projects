import sys
import random
from PyQt5 import QtWidgets

import outline

class main(outline.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(main, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.submit)
        self.pushButton_2.clicked.connect(self.randomNumber)

    
    def submit(self):
        number = self.lineEdit.text()
        if not number:
            QtWidgets.QMessageBox.about(self, " ", "Enter a number")
            return
        try:
            number = int(number)
        except:
            QtWidgets.QMessageBox.about(self, " ", "Enter a valid number")
            return
        self.output(self.square(number))
#        print('ok')


    def randomNumber(self):
        number = random.randint(0,100)
        self.lineEdit.setText(str(number))
        self.output(self.square(number))
#        print(number)


    def square(self, number):
        return number ** 2


    def output(self, val):
        self.lineEdit_2.setText(str(val))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    qt_app = main()
    qt_app.show()
    app.exec_()
