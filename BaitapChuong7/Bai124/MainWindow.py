# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(647, 651)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.labelTitle = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelTitle.setGeometry(QtCore.QRect(0, 0, 611, 51))
        self.labelTitle.setObjectName("labelTitle")
        self.pushButtonChangeText = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonChangeText.setGeometry(QtCore.QRect(70, 60, 75, 23))
        self.pushButtonChangeText.setObjectName("pushButtonChangeText")
        self.pushButtonFontSize = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonFontSize.setGeometry(QtCore.QRect(170, 60, 75, 23))
        self.pushButtonFontSize.setObjectName("pushButtonFontSize")
        self.pushButtonAlignLeft = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonAlignLeft.setGeometry(QtCore.QRect(350, 60, 75, 23))
        self.pushButtonAlignLeft.setObjectName("pushButtonAlignLeft")
        self.pushButtonAlignCenter = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonAlignCenter.setGeometry(QtCore.QRect(430, 60, 75, 23))
        self.pushButtonAlignCenter.setObjectName("pushButtonAlignCenter")
        self.pushButtonAlignRight = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonAlignRight.setGeometry(QtCore.QRect(510, 60, 75, 23))
        self.pushButtonAlignRight.setObjectName("pushButtonAlignRight")
        self.pushButtonShowPNG = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonShowPNG.setGeometry(QtCore.QRect(180, 90, 111, 41))
        self.pushButtonShowPNG.setObjectName("pushButtonShowPNG")
        self.pushButtonShowGIF = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonShowGIF.setGeometry(QtCore.QRect(310, 90, 111, 41))
        self.pushButtonShowGIF.setObjectName("pushButtonShowGIF")
        self.labelImage = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelImage.setGeometry(QtCore.QRect(0, 150, 641, 481))
        self.labelImage.setText("")
        self.labelImage.setPixmap(QtGui.QPixmap("./images/bumlancute.png"))
        self.labelImage.setScaledContents(False)
        self.labelImage.setObjectName("labelImage")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 647, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelTitle.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ff0000;\">Nguyen Bao Huy</span></p></body></html>"))
        self.pushButtonChangeText.setText(_translate("MainWindow", "Change Text"))
        self.pushButtonFontSize.setText(_translate("MainWindow", "Font Size ++ "))
        self.pushButtonAlignLeft.setText(_translate("MainWindow", "Align Left"))
        self.pushButtonAlignCenter.setText(_translate("MainWindow", "Align Center"))
        self.pushButtonAlignRight.setText(_translate("MainWindow", "Align Right"))
        self.pushButtonShowPNG.setText(_translate("MainWindow", "Show .PNG Format"))
        self.pushButtonShowGIF.setText(_translate("MainWindow", "Show .GIF Format"))
