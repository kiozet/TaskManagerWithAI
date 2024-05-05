from PyQt6.QtWidgets import *
from PyQt6 import uic
import sys
from addTaskWindow import TaskManager


class App(QFrame):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/MainWindowTaskManager1.0.ui', self)
        
        self.addTask.clicked.connect(self.addNewTask)
        
    
    def addNewTask(self):
        taskManagerApp = QApplication(sys.argv)
        taskManagerWindow = TaskManager()
        taskManagerWindow.show()
        sys.exit(taskManagerApp.exec())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    displayFrame = App()
    displayFrame.show()
    sys.exit(app.exec())