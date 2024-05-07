from PyQt6.QtWidgets import *
from PyQt6 import uic, QtCore
import sys
from resources.addTaskWindow import TaskManager


class TaskMainWindow(QFrame):
    def __init__(self) -> None:
        super(TaskMainWindow, self).__init__()
        
        self.ui = uic.loadUi("ui/MainWindowTaskManager1.0.ui", self)
        
        self.widget = None
        self.addTask.clicked.connect(self.addNewTask)
        self.projectsBtn.clicked.connect(self.switchToProjectsPage)
        self.inboxBtn.clicked.connect(self.switchToInboxWindow)
        self.profileBtn.clicked.connect(self.switchToProfileWindow)
        
        
        self.taskManagerBtn.setStyleSheet('color: blue')
        
        
    def setWidget(self, widget):
        self.widget = widget
        
    def addNewTask(self):
        self.taskManagerWindow = TaskManager()
        self.taskManagerWindow.show()
        
    def switchToProfileWindow(self):
        self.widget.setCurrentIndex(2)
    
    def switchToInboxWindow(self):
        self.widget.setCurrentIndex(3)
    
    def switchToProjectsPage(self):
        self.widget.setCurrentIndex(1)