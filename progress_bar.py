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
        self.pbar.setGeometry(30, 40, 200, 25)

        # setting window geometry
        self.setGeometry(300, 300, 280, 170)

        # setting window action
        self.setWindowTitle("Progress makes Perfect")

        # showing all the widgets
        self.show()

    # when button is pressed this method is being called
    def doAction(self):
        # setting for loop to set value of progress bar
        for i in range(101):
            # slowing down the loop
            time.sleep(0.05)

            # setting value to progress bar
            self.pbar.setValue(i)