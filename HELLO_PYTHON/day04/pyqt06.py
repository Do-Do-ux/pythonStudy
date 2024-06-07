from random import randint
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


form_class = uic.loadUiType("pyqt06.ui")[0]


class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
        
    def myclick(self):
        arr = []
        for i in range(1, 45+1):
            arr.append(i)
            
            for i in range(10000):
                rand = randint(0, len(arr) - 1)
                a = arr[0]
                arr[0] = arr[rand]
                arr[rand] = a
        print(arr[0], arr[1], arr[2], arr[3], arr[4], arr[5])
        arr2 = (arr[0], arr[1], arr[2], arr[3], arr[4], arr[5])
        for i in range(len(arr2)):
            for j in range(len(arr2)):
                if arr[i] < arr[j]:
                    a = arr[i]
                    arr[i] = arr[j]
                    arr[j] = a
        self.lcd01.display(str(arr[0]))
        self.lcd02.display(str(arr[1]))
        self.lcd03.display(str(arr[2]))
        self.lcd04.display(str(arr[3]))
        self.lcd05.display(str(arr[4]))
        self.lcd06.display(str(arr[5]))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
