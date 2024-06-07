import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import random


form_class = uic.loadUiType("./pyqt09.ui")[0]



class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.pb.clicked.connect(self.myclick)
        
        self.arr = [1,2,3,4,5,6,7,8,9]
    
        for i in range(10000) :
            rnd = int(random()*9)
            a = self.arr[0]
            self.arr[0]=self.arr[rnd]
            self.arr[rnd]=a
        
        print(self.arr[0],self.arr[1],self.arr[2])
    def myclick(self):
        me = self.le.text()
        
        myNum1 = int(me[0:1])
        myNum2 = int(me[1:2])
        myNum3 = int(me[2:3]) 
        strike = 0
        ball = 0
        
        if self.arr[0] == myNum1:
            strike += 1
        if self.arr[1] == myNum2:
            strike += 1
        if self.arr[2] == myNum3:
            strike += 1
        if self.arr[0] == myNum2 or self.arr[0] == myNum3 :
            ball += 1
        if self.arr[1] == myNum1 or self.arr[1] == myNum3 :
            ball += 1
        if self.arr[2] == myNum2 or self.arr[2] == myNum1 :
            ball += 1
        if strike == 3:
            self.pte.setPlainText("☆★☆성공★☆★")
           
        print("{} = {}Strike! {}Ball!".format(me,strike,ball))
        self.pte.appendPlainText("{} = {}Strike! {}Ball!".format(me,strike,ball))
            


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()