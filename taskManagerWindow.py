from PyQt6.QtWidgets import *
from PyQt6 import uic, QtCore
import sys
from addTaskWindow import TaskManager


class TaskMainWindow(QFrame):
    def __init__(self):
        super().__init__()
        
        self.ui = uic.loadUi("ui/MainWindowTaskManager1.0.ui",self)
        
        self.addTask.clicked.connect(self.addNewTask)
        self.projectsBtn.clicked.connect(self.switchToProjectsPage)
        
        self.taskManagerBtn.setStyleSheet('color: blue')
        
        
    def addNewTask(self):
        self.taskManagerWindow = TaskManager()
        self.taskManagerWindow.show()
        
    def switchToProfileWindow(self):
        pass
    
    def switchToInboxWindow(self):
        pass
    
    def switchToProjectsPage(self):
        pass


if __name__ == '__main__':  
    app = QApplication(sys.argv)
    displayFrame = TaskMainWindow()
    displayFrame.show()
    app.exec()