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
        MainWindow.resize(437, 268)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.labelFahrenheit = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelFahrenheit.setGeometry(QtCore.QRect(10, 10, 211, 51))
        self.labelFahrenheit.setObjectName("labelFahrenheit")
        self.lineEditFahrenheit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditFahrenheit.setGeometry(QtCore.QRect(280, 20, 121, 41))
        self.lineEditFahrenheit.setObjectName("lineEditFahrenheit")
        self.pushButtonConvert = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonConvert.setGeometry(QtCore.QRect(280, 100, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButtonConvert.setFont(font)
        self.pushButtonConvert.setObjectName("pushButtonConvert")
        self.labelCelsius = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelCelsius.setGeometry(QtCore.QRect(10, 140, 141, 51))
        self.labelCelsius.setObjectName("labelCelsius")
        self.labelDisplayResult = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelDisplayResult.setGeometry(QtCore.QRect(210, 150, 191, 31))
        self.labelDisplayResult.setText("")
        self.labelDisplayResult.setObjectName("labelDisplayResult")
        self.labelError = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelError.setGeometry(QtCore.QRect(200, 70, 231, 20))
        self.labelError.setText("")
        self.labelError.setObjectName("labelError")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 437, 21))
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
        self.labelFahrenheit.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">Nhập năm dương lịch:</span></p></body></html>"))
        self.pushButtonConvert.setText(_translate("MainWindow", "Convert"))
        self.labelCelsius.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Năm âm lịch:</span></p></body></html>"))