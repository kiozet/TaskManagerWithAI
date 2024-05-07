from PyQt6.QtWidgets import *
from PyQt6 import uic, QtCore
import sys


class ProjectsMainWindow(QFrame):
    def __init__(self) -> None:
        super(ProjectsMainWindow, self).__init__()
        self.ui = uic.loadUi("ui/MainWindowProjects1.0.ui", self)
        
        self.widget = None
        self.profileBtn.clicked.connect(self.switchToProfilePage)
        self.taskManagerBtn.clicked.connect(self.switchToTaskManager)
        self.inboxBtn.clicked.connect(self.switchToInboxWindow)
        
        self.projectsBtn.setStyleSheet('color: blue')
        
        
    def setWidget(self, widget):
        self.widget = widget
        
    def switchToInboxWindow(self):
        self.widget.setCurrentIndex(3)
    
    def switchToTaskManager(self):
        self.widget.setCurrentIndex(0)
    
    def switchToProfilePage(self):
        self.widget.setCurrentIndex(2)