import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


form_class = uic.loadUiType("pyqt05.ui")[0]


class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
        
        
    def myclick(self):
        le01 = self.le01.text()
        le02 = self.le02.text()
        le03 = self.le03.text()
        le04 = self.le04.text()
        
        ile01 = int(le01)
        ile02 = int(le02)
        ile03 = int(le03)
        
        sum = 0
        for i in range(ile01 , ile02+1):
            print(i)
            if i % ile03 == 0:
                sum = sum+i
        self.le04.setText(str(sum))
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
