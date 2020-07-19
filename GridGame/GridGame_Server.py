# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GridTest.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from Button import Button
from server import Server


class Ui_ConnectingWindow(object):

    def __init__(self):
        self.server = Server()
        self.server.connect()

    def sendData(self):
        self.message = (0,1,1,0)
        self.server.send(self.message)
        self.clientStatus = self.server.get()

    def setupUi(self, ConnectingWindow):
        ConnectingWindow.setObjectName("ConnectingWindow")
        ConnectingWindow.resize(635, 493)
        ConnectingWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(ConnectingWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(220, 120, 200, 200))
        self.gridLayoutWidget.setMinimumSize(QtCore.QSize(200, 200))
        self.gridLayoutWidget.setMaximumSize(QtCore.QSize(200, 200))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")

        self.bt1 = Button(ConnectingWindow,100,100,self.clientStatus[0])
        self.bt2 = Button(ConnectingWindow,200,100,self.clientStatus[1])
        self.bt3 = Button(ConnectingWindow,100,200,self.clientStatus[2])
        self.bt4 = Button(ConnectingWindow,200,200,self.clientStatus[3])


    

        ConnectingWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ConnectingWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 635, 21))
        self.menubar.setObjectName("menubar")
        ConnectingWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ConnectingWindow)
        self.statusbar.setObjectName("statusbar")
        ConnectingWindow.setStatusBar(self.statusbar)

       # label = QtWidgets.QLabel(ConnectingWindow)
       # label.setText("My Text!")
       # label.move(50,50)


        self.retranslateUi(ConnectingWindow)
        QtCore.QMetaObject.connectSlotsByName(ConnectingWindow)

    def retranslateUi(self, ConnectingWindow):
        _translate = QtCore.QCoreApplication.translate
        ConnectingWindow.setWindowTitle(_translate("ConnectingWindow", "SERVER"))


      #  self = QtWidgets.QPushButton(app.gridLayoutWidget)
      #  self.setMinimumSize(QtCore.QSize(50,50))
      #  self.setMaximumSize(QtCore.QSize(200,200))
      #  self.setText("")
      #  app.gridLayout.addWidget(self, 1, 0, 1, 1)

     #   self.Button3 = QtWidgets.QPushButton(self.gridLayoutWidget)
     #   self.Button3.setMinimumSize(QtCore.QSize(50, 50))
     #   self.Button3.setMaximumSize(QtCore.QSize(200, 200))
     #   self.Button3.setText("")
     #   self.Button3.setObjectName("Button3")
     #   self.gridLayout.addWidget(self.Button3, 1, 0, 1, 1)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ConnectingWindow = QtWidgets.QMainWindow()
    ui = Ui_ConnectingWindow()
    ui.sendData()
    ui.setupUi(ConnectingWindow)
    ConnectingWindow.show()
    sys.exit(app.exec_())
    
   
