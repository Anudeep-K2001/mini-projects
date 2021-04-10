import sys
import random
from PyQt5 import QtWidgets

import outline

class main(outline.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(main, self).__init__()
        self.setupUi(self)
        self.buy.clicked.connect(self.BUY)
        self.sell.clicked.connect(self.SELL)
        self.lineEdit_3.setText('1.2')
        self.lineEdit_4.setText('0.4')


    def BUY(self):
        text = self.lineEdit.text()
        
        if text == '':
            return
        
        self.price = float(text)
        profitPercent = float(self.lineEdit_3.text())/100
        lossPercent = float(self.lineEdit_4.text())/100

        quantity = self.lineEdit_2.text()
        
        if quantity == '':
            quantity = 1
        else:
            quantity = int(quantity)

        

        TargetPrice = round(self.price * profitPercent,2)
        StopLossPrice = round(self.price * lossPercent,2)
        TotalValue = round(self.price * quantity,2)

        target = TargetPrice + self.price
        stopLoss = self.price - StopLossPrice

        self.targetVal.setText(str(TargetPrice))
        self.stopLossVal.setText(str(StopLossPrice))
        self.target.setText(str(target))
        self.stopLoss.setText(str(stopLoss))
        self.totalValue.setText(str(TotalValue))
        self.PROFIT.setText(str(round(TargetPrice*quantity,2)))
        self.LOSS.setText(str(round(StopLossPrice*quantity,2)))


    def SELL(self):
        text = self.lineEdit.text()
        
        if text == '':
            return

        
        self.price = float(text)
        profitPercent = float(self.lineEdit_3.text())/100
        lossPercent = float(self.lineEdit_4.text())/100            
        
        quantity = self.lineEdit_2.text()
        
        if quantity == '':
            quantity = 1
        else:
            quantity = int(quantity)

    
        

        TargetPrice = round(self.price * profitPercent,2)
        StopLossPrice = round(self.price * lossPercent,2)
        TotalValue = round(self.price * quantity)


        target = self.price - TargetPrice
        stopLoss = StopLossPrice + self.price

        self.targetVal.setText(str(TargetPrice))
        self.stopLossVal.setText(str(StopLossPrice))
        self.target.setText(str(target))
        self.stopLoss.setText(str(stopLoss))
        self.totalValue.setText(str(TotalValue))
        self.PROFIT.setText(str(round(TargetPrice*quantity,2)))
        self.LOSS.setText(str(round(StopLossPrice*quantity,2)))


        



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    qt_app = main()
    qt_app.show()
    app.exec_()
