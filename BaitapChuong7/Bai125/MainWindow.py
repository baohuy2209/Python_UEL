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
        MainWindow.resize(454, 362)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(0, 50))
        self.label.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetFixedSize)
        self.gridLayout.setObjectName("gridLayout")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)
        self.lineEditFullName = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditFullName.setClearButtonEnabled(True)
        self.lineEditFullName.setObjectName("lineEditFullName")
        self.gridLayout.addWidget(self.lineEditFullName, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.lineEditEmail = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditEmail.setObjectName("lineEditEmail")
        self.gridLayout.addWidget(self.lineEditEmail, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.lineEditCityProvince = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditCityProvince.setObjectName("lineEditCityProvince")
        self.gridLayout.addWidget(self.lineEditCityProvince, 3, 1, 1, 1)
        self.lineEditUsername = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditUsername.setObjectName("lineEditUsername")
        self.gridLayout.addWidget(self.lineEditUsername, 1, 1, 1, 1)
        self.lineEditPassword = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.gridLayout.addWidget(self.lineEditPassword, 4, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 5, 0, 1, 1)
        self.lineEditConfirmPassword = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditConfirmPassword.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEditConfirmPassword.setObjectName("lineEditConfirmPassword")
        self.gridLayout.addWidget(self.lineEditConfirmPassword, 5, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButtonRegister = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonRegister.setObjectName("pushButtonRegister")
        self.horizontalLayout.addWidget(self.pushButtonRegister)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButtonClose = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonClose.setObjectName("pushButtonClose")
        self.horizontalLayout.addWidget(self.pushButtonClose)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.gridLayout_2.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 454, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButtonClose.clicked.connect(MainWindow.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#0000ff;\">Register Information</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "City/Province:"))
        self.label_6.setText(_translate("MainWindow", "Password:"))
        self.lineEditFullName.setPlaceholderText(_translate("MainWindow", "Enter your fullname here "))
        self.label_3.setText(_translate("MainWindow", "User Name:"))
        self.label_4.setText(_translate("MainWindow", "Email: "))
        self.label_2.setText(_translate("MainWindow", "Full Name: "))
        self.label_7.setText(_translate("MainWindow", "Confirm Password: "))
        self.pushButtonRegister.setText(_translate("MainWindow", "Register"))
        self.pushButtonClose.setText(_translate("MainWindow", "Close"))
