
from PyQt5 import QtCore, QtGui, QtWidgets

class Button():

    def __init__ (self,ConnectingWindow,x,y,status):

        self.button = QtWidgets.QPushButton(ConnectingWindow)
        self.button.setMinimumSize(QtCore.QSize(100,100))
        self.button.setMaximumSize(QtCore.QSize(100,100))
        self.button.setText("")
        self.button.move(x,y)
        self.status = status
        self.color = "e1e1e1"
        self.button.setStyleSheet("background-color:#"+self.color)
        self.button.clicked.connect(self.click)

    def click(self):

        if self.status:
            self.button.setStyleSheet("background-color:#6ebfb5")
        else:
            self.button.hide()

        