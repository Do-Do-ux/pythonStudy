from random import randint
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.Qt import QMessageBox


form_class = uic.loadUiType("pyqt08.ui")[0]

    
    





class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.num = ""
        self.setupUi(self)
       
        self.pb1.clicked.connect(self.pbclick)
        self.pb2.clicked.connect(self.pbclick)
        self.pb3.clicked.connect(self.pbclick)
        self.pb4.clicked.connect(self.pbclick)
        self.pb5.clicked.connect(self.pbclick)
        self.pb6.clicked.connect(self.pbclick)
        self.pb7.clicked.connect(self.pbclick)
        self.pb8.clicked.connect(self.pbclick)
        self.pb9.clicked.connect(self.pbclick)
        self.pb0.clicked.connect(self.pbclick)
        self.call.clicked.connect(self.callclick)
        
    def pbclick(self):
        pb1_button = self.sender()
        pbt1 = pb1_button.text()
        self.num += pbt1
        self.le.setText(self.num)
        
    def callclick(self):
        calltext = self.le.text()
        QMessageBox.about(self, "call...", "{}".format(calltext))
    
        
        
    
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
