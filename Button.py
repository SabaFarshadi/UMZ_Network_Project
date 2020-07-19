
from PyQt5 import QtCore, QtGui, QtWidgets

class Button():
    def __init__ (self,ConnectingWindow,x,y,status):

        self = QtWidgets.QPushButton(ConnectingWindow)
        self.setMinimumSize(QtCore.QSize(100,100))
        self.setMaximumSize(QtCore.QSize(100,100))
        self.setText("")
        self.move(x,y)

        if status:
            self.setStyleSheet("background-color:#50c878")
        else:
            self.setStyleSheet("background-color:#dc143c")

    def click():

        self.clicked.connect