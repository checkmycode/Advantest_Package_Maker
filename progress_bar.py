# importing libraries
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import time

class ProgressBar(QWidget):

    def __init__(self):
        super().__init__()

        # calling initUI method
        self.initUI()

    # method for creating widgets
    def initUI(self):
        # creating progress bar
        self.pbar = QProgressBar(self)

        # setting its geometry
        self.pbar.setGeometry(35, 30, 250, 25)

        # setting window geometry
        self.setGeometry(150, 150, 280, 85)

        # setting window action
        self.setWindowTitle("Progress makes Perfect")

        # creating push button
        self.btn = QPushButton('Start', self)

        # changing its position
        self.btn.move(40, 80)

        # adding action to push button
        self.btn.clicked.connect(self.doAction)

        # showing all the widgets
        self.show()

    # when button is pressed this method is being called
    def doAction(self):
        stop = 0
        while stop != 1:
            if stop == 0:
                self.pbar.setValue(100)
            if self.pbar.setValue == 100:
                stop = 1

if __name__ == '__main__':
    # create pyqt5 app
    App = QApplication(sys.argv)

    # create the instance of our Window
    window = ProgressBar()

    # start the app
    sys.exit(App.exec())