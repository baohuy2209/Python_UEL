# Form implementation generated from reading ui file 'SignalandSlotsMainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(566, 262)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.labelTitle = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelTitle.setGeometry(QtCore.QRect(40, 0, 481, 71))
        self.labelTitle.setObjectName("labelTitle")
        self.lineEditName = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditName.setGeometry(QtCore.QRect(60, 90, 461, 20))
        self.lineEditName.setObjectName("lineEditName")
        self.labelName = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelName.setGeometry(QtCore.QRect(60, 120, 461, 31))
        self.labelName.setText("")
        self.labelName.setObjectName("labelName")
        self.pushButtonChangeColor = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonChangeColor.setGeometry(QtCore.QRect(110, 190, 75, 23))
        self.pushButtonChangeColor.setObjectName("pushButtonChangeColor")
        self.pushButtonEXit = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonEXit.setGeometry(QtCore.QRect(390, 190, 75, 23))
        self.pushButtonEXit.setObjectName("pushButtonEXit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 566, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.lineEditName.textChanged['QString'].connect(self.labelName.setText) # type: ignore
        self.pushButtonEXit.clicked.connect(MainWindow.close) # type: ignore
        self.pushButtonChangeColor.clicked.connect(MainWindow.repaint) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelTitle.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; color:#ff0000;\">Signal and Slots</span></p></body></html>"))
        self.pushButtonChangeColor.setText(_translate("MainWindow", "ChangeColor"))
        self.pushButtonEXit.setText(_translate("MainWindow", "Exit"))
