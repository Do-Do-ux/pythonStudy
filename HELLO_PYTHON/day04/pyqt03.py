import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


form_class = uic.loadUiType("pyqt03.ui")[0]


class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
        self.le_mine.returnPressed.connect(self.myclick)
        
    def myclick(self):
        mine = self.le_mine.text()
        from random import random
        
        num = random()
        com = 0;
        me = 0;
        result = ""
        print(num)
        if num > 0.5:
            com = 1
        else:
            com = 0
        
        if mine == "홀":
            me = 1
        else:
            me = 0
        
        if me == com:
            result = "이김"
        else:
            result = "짐"
        
        if com == 1:
            com ="홀"
        else:
            com = "짝"
        print("컴:",com)
        print("나:",mine)
        print("결과:",result)
       
        self.le_com.setText(com)
        self.le_result.setText(result)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
