from random import randint
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


form_class = uic.loadUiType("pyqt07.ui")[0]

    
    





class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
        
    def myclick(self):
        first = self.le_first.text();
        last = self.le_last.text();
        
        ifirst = int(first)
        ilast = int(last)
        
        text = ""
        for i in range(ifirst,ilast-1,-1):
            text += "◈" * i
            text += "\n"
        self.pte.appendPlainText(text)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
