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
        MainWindow.resize(556, 406)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.labelTitle = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelTitle.setGeometry(QtCore.QRect(140, 10, 251, 51))
        self.labelTitle.setObjectName("labelTitle")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 50, 121, 41))
        self.label.setObjectName("label")
        self.lineEditFullName = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditFullName.setGeometry(QtCore.QRect(140, 60, 351, 31))
        self.lineEditFullName.setObjectName("lineEditFullName")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 110, 71, 41))
        self.label_2.setObjectName("label_2")
        self.lineEditEmail = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditEmail.setGeometry(QtCore.QRect(140, 120, 351, 31))
        self.lineEditEmail.setObjectName("lineEditEmail")
        self.checkBoxMachineLearning = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.checkBoxMachineLearning.setGeometry(QtCore.QRect(140, 170, 141, 41))
        self.checkBoxMachineLearning.setStyleSheet("font-size:16px")
        self.checkBoxMachineLearning.setObjectName("checkBoxMachineLearning")
        self.checkBoxDeepLearning = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.checkBoxDeepLearning.setGeometry(QtCore.QRect(140, 210, 141, 41))
        self.checkBoxDeepLearning.setStyleSheet("font-size:16px")
        self.checkBoxDeepLearning.setObjectName("checkBoxDeepLearning")
        self.checkBoxSmartContract = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.checkBoxSmartContract.setGeometry(QtCore.QRect(140, 250, 141, 41))
        self.checkBoxSmartContract.setStyleSheet("font-size:16px")
        self.checkBoxSmartContract.setObjectName("checkBoxSmartContract")
        self.pushButtonSubmit = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonSubmit.setGeometry(QtCore.QRect(230, 300, 131, 51))
        self.pushButtonSubmit.setStyleSheet("font-size:24px")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../Downloads/submit-successfully.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonSubmit.setIcon(icon)
        self.pushButtonSubmit.setObjectName("pushButtonSubmit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 556, 21))
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
        self.labelTitle.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; color:#0000ff;\">Courses Registration </span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Full Name: </span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Email: </span></p></body></html>"))
        self.checkBoxMachineLearning.setText(_translate("MainWindow", "Machine Learning"))
        self.checkBoxDeepLearning.setText(_translate("MainWindow", "Deep Learning"))
        self.checkBoxSmartContract.setText(_translate("MainWindow", "Smart Contract"))
        self.pushButtonSubmit.setText(_translate("MainWindow", "Submit"))