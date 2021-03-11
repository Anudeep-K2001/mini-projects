import sys
import math
from PyQt5 import QtWidgets

import outline

class main(outline.Ui_MainWindow, QtWidgets.QMainWindow):

    def __init__(self):
        super(main, self).__init__()
        self.setupUi(self)

        self.pushButton_one.clicked.connect(self.one)
        self.pushButton_two.clicked.connect(self.two)
        self.pushButton_three.clicked.connect(self.three)
        self.pushButton_four.clicked.connect(self.four)
        self.pushButton_five.clicked.connect(self.five)
        self.pushButton_six.clicked.connect(self.six)
        self.pushButton_seven.clicked.connect(self.seven)
        self.pushButton_eight.clicked.connect(self.eight)
        self.pushButton_nine.clicked.connect(self.nine)
        self.pushButton_zero.clicked.connect(self.zero)

        self.pushButton_equal.clicked.connect(self.equal)
        self.pushButton_plus.clicked.connect(self.plus)
        self.pushButton_minus.clicked.connect(self.minus)
        self.pushButton_multi.clicked.connect(self.multi)
        self.pushButton_div.clicked.connect(self.div)
        self.pushButton_power.clicked.connect(self.power)
        self.pushButton_open.clicked.connect(self.openb)
        self.pushButton_close.clicked.connect(self.closeb)
        self.pushButton_clear.clicked.connect(self.clear)
        self.pushButton_back.clicked.connect(self.back)
        self.pushButton_ans.clicked.connect(self.ans)
        self.pushButton_plusorminus.clicked.connect(self.plusorminus)
        self.pushButton_dot.clicked.connect(self.dot)

        self.expr = ''
        self.answer = ''
    

    def one(self):
        self.expr += '1'
        self.textBrowser.setText(self.expr)
        return


    def two(self):
        self.expr += '2'
        self.textBrowser.setText(self.expr)
        return
    
    def three(self):
        self.expr += '3'
        self.textBrowser.setText(self.expr)
        return
    
    def four(self):
        self.expr += '4'
        self.textBrowser.setText(self.expr)
        return
    
    def five(self):
        self.expr += '5'
        self.textBrowser.setText(self.expr)
        return

    def six(self):
        self.expr += '6'
        self.textBrowser.setText(self.expr)
        return
        
    def seven(self):
        self.expr += '7'
        self.textBrowser.setText(self.expr)
        return
    
    def eight(self):
        self.expr += '8'
        self.textBrowser.setText(self.expr)
        return

    def nine(self):
        self.expr += '9'
        self.textBrowser.setText(self.expr)
        return

    def zero(self):
        self.expr += '0'
        self.textBrowser.setText(self.expr)
        return

    def plus(self):
        self.expr += '+'
        self.textBrowser.setText(self.expr)
        return
    
    def minus(self):
        self.expr += '-'
        self.textBrowser.setText(self.expr)
        return

    def multi(self):
        self.expr += '*'
        self.textBrowser.setText(self.expr)
        return

    def div(self):
        self.expr += '/'
        self.textBrowser.setText(self.expr)
        return

    def power(self):
        self.expr += '**'
        self.textBrowser.setText(self.expr)
        return
    
    def openb(self):
        self.expr += '('
        self.textBrowser.setText(self.expr)
        return

    def closeb(self):
        self.expr += ')'
        self.textBrowser.setText(self.expr)
        return
    
    def clear(self):
        self.expr = ''
        self.textBrowser.setText(self.expr)
        return
    
    def back(self):
        self.expr = self.expr[:-1]
        self.textBrowser.setText(self.expr)
        return

    def ans(self):
        self.expr += self.answer
        self.textBrowser.setText(self.expr)
        return

    def plusorminus(self):
        for i in range(len(self.expr)-1,0,-1):
            if not self.expr[i].isdigit():
                pre = self.expr[:i+1]
                post = self.expr[i+1:]
                if self.expr[i] == '-':
                    self.expr = pre[:-1] + '+' + post
                elif self.expr[i] == '+':
                    self.expr = pre[:-1] + '-' + post
                else:
                    self.expr = pre + '-' + post
                self.textBrowser.setText(self.expr)
                return             
        else:
            self.expr = '-' + self.expr
            self.textBrowser.setText(self.expr)
            return

    def dot(self):
        self.expr += '.'
        self.textBrowser.setText(self.expr)
        return

    
    def equal(self):
        try:
            self.answer = str(eval(self.expr))
            self.expr = self.answer
            self.textBrowser.setText(self.answer)
            return
        except:
            self.expr = ''
            self.textBrowser.setText('error')
            return
















if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    qt_app = main()
    qt_app.show()
    app.exec_()