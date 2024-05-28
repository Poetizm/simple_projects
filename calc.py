# Form implementation generated from reading ui file 'calc.ui'
#
# Created by: PyQt6 UI code generator 6.4.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Calc(object):
    def setupUi(self, Calc):
        Calc.setObjectName("Calc")
        Calc.resize(540, 410)
        font = QtGui.QFont()
        font.setItalic(False)
        Calc.setFont(font)
        self.label = QtWidgets.QLabel(parent=Calc)
        self.label.setGeometry(QtCore.QRect(50, 80, 180, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=Calc)
        self.label_2.setGeometry(QtCore.QRect(50, 130, 200, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(parent=Calc)
        self.lineEdit.setGeometry(QtCore.QRect(290, 80, 180, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=Calc)
        self.lineEdit_2.setGeometry(QtCore.QRect(290, 130, 180, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=Calc)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(50, 190, 420, 120))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.plus)
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.minus)
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.umn)
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.delu)
        self.horizontalLayout.addWidget(self.pushButton_5)
        self.label_3 = QtWidgets.QLabel(parent=Calc)
        self.label_3.setGeometry(QtCore.QRect(186, 332, 161, 30))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("QLabel{color:green}")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Calc)
        QtCore.QMetaObject.connectSlotsByName(Calc)

    def retranslateUi(self, Calc):
        _translate = QtCore.QCoreApplication.translate
        Calc.setWindowTitle(_translate("Calc", "Calc"))
        self.label.setText(_translate("Calc", "First number:"))
        self.label_2.setText(_translate("Calc", "Second number:"))
        self.lineEdit.setPlaceholderText(_translate("Calc", "Please Enter First Number"))
        self.lineEdit_2.setPlaceholderText(_translate("Calc", "Please Enter Second Number"))
        self.pushButton_2.setText(_translate("Calc", "+"))
        self.pushButton_4.setText(_translate("Calc", "-"))
        self.pushButton_3.setText(_translate("Calc", "*"))
        self.pushButton_5.setText(_translate("Calc", "/"))


    def plus(self):
        num1 = int(self.lineEdit.text())
        num2 = int(self.lineEdit_2.text())
        res = num1 + num2
        self.label_3.setText(str(res))


    def minus(self):
        num1 = int(self.lineEdit.text())
        num2 = int(self.lineEdit_2.text())
        res = num1 - num2
        self.label_3.setText(str(res))

    def umn(self):
        num1 = int(self.lineEdit.text())
        num2 = int(self.lineEdit_2.text())
        res = num1 * num2
        self.label_3.setText(str(res))

    def delu(self):
        num1 = int(self.lineEdit.text())
        num2 = int(self.lineEdit_2.text())
        res = num1 // num2
        self.label_3.setText(str(res))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Calc = QtWidgets.QWidget()
    ui = Ui_Calc()
    ui.setupUi(Calc)
    Calc.show()
    sys.exit(app.exec())