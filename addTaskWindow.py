from PyQt6.QtWidgets import *
from PyQt6 import uic
import sys


class TaskManager(QFrame):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/taskManager.ui', self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    displayFrame = TaskManager()
    displayFrame.show()
    sys.exit(app.exec())