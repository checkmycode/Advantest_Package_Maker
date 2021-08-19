from PyQt5 import QtCore, QtWidgets

class Ui_OtherWindow(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 91)

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 10, 251, 16))
        self.label.setObjectName("label")

        self.cancel_button = QtWidgets.QPushButton(Form)
        self.cancel_button.setGeometry(QtCore.QRect(210, 60, 81, 23))
        self.cancel_button.setObjectName("cancel_button")
        self.cancel_button.clicked.connect(self.click_cancel)

        self.ok_button = QtWidgets.QPushButton(Form)
        self.ok_button.setGeometry(QtCore.QRect(120, 60, 81, 23))
        self.ok_button.setObjectName("ok_button")
        self.ok_button.clicked.connect(self.click_ok)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def click_cancel(self):
        import sys
        sys.exit()

    def click_ok(self):
        import sys
        sys.exit()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Package Complete!"))
        self.label.setText(_translate("Form", r"<html><head/><body><p><span style=\" font-size:10pt;\">Your firmware is now on your desktop!</span></p></body></html>"))
        self.cancel_button.setText(_translate("Form", "Cancel"))
        self.ok_button.setText(_translate("Form", "OK"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OtherWindow = QtWidgets.QMainWindow()
    ui = Ui_OtherWindow()
    ui.setupUi(OtherWindow)
    OtherWindow.show()
    sys.exit(app.exec_())
