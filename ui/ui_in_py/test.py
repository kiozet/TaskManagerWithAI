from PyQt6.QtWidgets import *
from PyQt6 import uic
import sys


class App(QFrame):
    def __init__(self):
        super().__init__()
        uic.loadUi('MainWindowTaskManager1.0.ui', self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    displayFrame = App()
    displayFrame.show()
    sys.exit(app.exec())