from PyQt6.QtWidgets import *
from PyQt6 import uic
import sys
from addTaskWindow import TaskManager


class TaskMainWindow(QFrame):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/MainWindowTaskManager1.0.ui', self)
        
        self.addTask.clicked.connect(self.addNewTask)
        
    
    def addNewTask(self):
        self.taskManagerWindow = TaskManager()
        self.taskManagerWindow.show()


if __name__ == '__main__':  
    app = QApplication(sys.argv)
    displayFrame = TaskMainWindow()
    displayFrame.show()
    app.exec()