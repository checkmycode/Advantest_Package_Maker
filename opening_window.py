from PyQt5 import QtCore, QtGui, QtWidgets

home_list = [
    "Atlas_Engineering_GOEM_Retail", "Atlas_Engineering_HP", "Atlas_Engineering_Dell", "Atlas_Engineering_Lenovo",
    "Atlas_Engineering_Microsoft", "Atlas_Production_GOEM", "Atlas_Production_HP", "Atlas_Production_Dell",
    "Atlas_Production_Lenovo", "Atlas_Production_Microsoft",
]

class HomeWindow(object):
    def __init__(self):
        super().__init__()

    def open_opening_window(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = HomeWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def open_bot_window(self):
        from bot_window_eng import Ui_OtherWindow
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_OtherWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        MainWindow.hide()

    def open_production_window(self):
        from bot_window_prod import Ui_OtherWindow
        self.bot_window = QtWidgets.QMainWindow()
        self.ui = Ui_OtherWindow()
        self.ui.setupUi(self.bot_window)
        self.bot_window.show()
        MainWindow.hide()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(422, 610)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.home_start_button2 = QtWidgets.QPushButton(self.centralwidget)
        self.home_start_button2.setGeometry(QtCore.QRect(210, 480, 161, 61))
        self.home_start_button2.setObjectName("home_start_button2")
        self.home_start_button2.clicked.connect(self.reset)

        self.home_start_button = QtWidgets.QPushButton(self.centralwidget)
        self.home_start_button.setGeometry(QtCore.QRect(50, 480, 161, 61))
        self.home_start_button.setObjectName("home_start_button")
        self.home_start_button.clicked.connect(self.clicked)

        self.home_listbox = QtWidgets.QListWidget(self.centralwidget)
        self.home_listbox.setGeometry(QtCore.QRect(80, 200, 261, 251))
        self.home_listbox.setObjectName("home_listbox")

        for names in reversed(home_list):
            self.home_listbox.insertItem(0, names)

        self.advantest_logo = QtWidgets.QLabel(self.centralwidget)
        self.advantest_logo.setGeometry(QtCore.QRect(80, 50, 261, 131))
        self.advantest_logo.setText("")
        self.advantest_logo.setPixmap(QtGui.QPixmap("logo.png"))
        self.advantest_logo.setScaledContents(True)
        self.advantest_logo.setObjectName("advantest_logo")
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 422, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Advantest Package Maker", "Advantest Package Maker"))
        self.home_start_button.setText(_translate("MainWindow", "START"))
        self.home_start_button2.setText(_translate("MainWindow", "RESET"))

    def reset(self):
        import os.path
        dir = r'C:\Users\Public'
        os.chdir(dir)
        if os.path.isfile('./log.txt'):
            os.remove("log.txt")
        else:
            print('no file found')

        host_name = os.environ['HOMEPATH']
        os.chdir(fr'C:{host_name}\Desktop')
        if os.path.isdir('CUSTFW'):
            os.rmdir('CUSTFW')
        else:
            print('its not here')

    def clicked(self):
        item = self.home_listbox.currentItem()
        if item == None:
            print('Select an item from the list')
        elif item.text() == "Atlas_Engineering_GOEM_Retail":
            self.open_bot_window()
            f = open(r"C:\Users\Public\log.txt", "a+")
            f.write(f"Base_fw: {home_list[0]}\n")
            f.close()
        elif item.text() == "Atlas_Engineering_HP":
            self.open_bot_window()
            f = open(r"C:\Users\Public\log.txt", "a+")
            f.write(f"Base_fw: {home_list[1]}\n")
            f.close()
            return home_list[1]
        elif item.text() == "Atlas_Engineering_Dell":
            self.open_bot_window()
            f = open(r"C:\Users\Public\log.txt", "a+")
            f.write(f"Base_fw: {home_list[2]}\n")
            f.close()
            return home_list[2]
        elif item.text() == "Atlas_Engineering_Lenovo":
            self.open_bot_window()
            f = open(r"C:\Users\Public\log.txt", "a+")
            f.write(f"Base_fw: {home_list[3]}\n")
            f.close()
        elif item.text() == "Atlas_Engineering_Microsoft":
            self.open_bot_window()
            f = open(r"C:\Users\Public\log.txt", "a+")
            f.write(f"Base_fw: {home_list[4]}\n")
            f.close()
        elif item.text() == "Atlas_Production_GOEM":
            self.open_production_window()
            f = open(r"C:\Users\Public\log.txt", "a+")
            f.write(f"Base_fw: {home_list[5]}\n")
            f.close()
        elif item.text() == "Atlas_Production_HP":
            self.open_production_window()
            f = open(r"C:\Users\Public\log.txt", "a+")
            f.write(f"Base_fw: {home_list[6]}\n")
            f.close()
        elif item.text() == "Atlas_Production_Dell":
            self.open_production_window()
            f = open(r"C:\Users\Public\log.txt", "a+")
            f.write(f"Base_fw: {home_list[7]}\n")
            f.close()
        elif item.text() == "Atlas_Production_Lenovo":
            self.open_production_window()
            f = open(r"C:\Users\Public\log.txt", "a+")
            f.write(f"Base_fw: {home_list[8]}\n")
            f.close()
        elif item.text() == "Atlas_Production_Microsoft":
            self.open_production_window()
            f = open(r"C:\Users\Public\log.txt", "a+")
            f.write(f"Base_fw: {home_list[9]}\n")
            f.close()
        else:
            print('Please restart the program.')


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = HomeWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
