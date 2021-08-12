from PyQt5 import QtCore, QtGui, QtWidgets
information = {'ptb': ''}

class Ui_OtherWindow(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(421, 91)
        self.browse_line_edit = QtWidgets.QLineEdit(Form)
        self.browse_line_edit.setGeometry(QtCore.QRect(10, 30, 311, 21))
        self.browse_line_edit.setObjectName("browse_line_edit")
        self.browse_line_edit.editingFinished.connect(self.set_answers)

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 10, 251, 16))
        self.label.setObjectName("label")

        self.browse_push_button = QtWidgets.QPushButton(Form)
        self.browse_push_button.setGeometry(QtCore.QRect(330, 30, 81, 23))
        self.browse_push_button.setObjectName("browse_push_button")
        self.browse_push_button.clicked.connect(self.ptb_browse_button)

        self.cancel_button = QtWidgets.QPushButton(Form)
        self.cancel_button.setGeometry(QtCore.QRect(330, 60, 81, 23))
        self.cancel_button.setObjectName("cancel_button")
        self.cancel_button.clicked.connect(self.click_cancel)

        self.ok_button = QtWidgets.QPushButton(Form)
        self.ok_button.setGeometry(QtCore.QRect(240, 60, 81, 23))
        self.ok_button.setObjectName("ok_button")
        self.ok_button.clicked.connect(self.click_ok)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", r"Must use \\usg-og-fpgcss01.wdc.com)"))
        self.label.setText(_translate("Form", r"<html><head/><body><p><span style=\" font-size:10pt;\">PATHWAY TO BOT FOLDER </span></p></body></html>"))
        self.browse_push_button.setText(_translate("Form", "Browse"))
        self.cancel_button.setText(_translate("Form", "Cancel"))
        self.ok_button.setText(_translate("Form", "OK"))

    def ptb_browse_button(self):
        from PyQt5.QtWidgets import QFileDialog
        file = str(QFileDialog.getExistingDirectory(None, 'Select Folder'))
        ptb = self.browse_line_edit.setText(file)
        information['ptb'] = self.browse_line_edit.text()

    def make_logs(self):
        # import random
        # id = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
        # identifier = ""
        # for num in id:
        #     x = str(random.randint(1, 9))
        #     identifier += x

        f = open(r"C:\Users\Public\log.txt", "a+")
        f.write(f"Pathway to BOT: {information['ptb']}\n")
        f.close()

        with open(r"C:\Users\Public\log.txt", 'r') as file:
            filedata = file.read()

            # Replace the target string
            filedata = filedata.replace('/', '\\')

            # Write the file out again
            with open(r"C:\Users\Public\log.txt", 'w') as file:
                file.write(filedata)

    def get_edit_lines_info(self):
        """Pulls info submitted from edit lines from log.bot"""
        info = []
        lookup = 'Pathway to BOT: '
        lookup2 = 'Base_fw: '

        with open(r'C:\Users\Public\log.txt') as myFile:
            for num, line in enumerate(myFile, 1):
                if lookup in line.strip('\\n'):
                    info.append(line[15:])
                    info_stripped = [x.replace('\n', '') for x in info]
                if lookup2 in line.strip('\\n'):
                    info.append(line[9:])
                    info_stripped = [x.replace('\n', '') for x in info]
            return info_stripped


    def click_ok(self):
        from make_custfw import MakeCustfw
        custfw = MakeCustfw()
        custfw.make_custfw()

    def click_cancel(self):
        sys.exit()

    def set_answers(self):
        information['ptb'] = self.browse_line_edit.text()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OtherWindow = QtWidgets.QMainWindow()
    ui = Ui_OtherWindow()
    ui.setupUi(OtherWindow)
    OtherWindow.show()
    sys.exit(app.exec_())
