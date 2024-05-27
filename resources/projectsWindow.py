from PyQt6.QtWidgets import *
from PyQt6 import uic, QtCore


class ProjectsMainWindow(QFrame):
    def __init__(self) -> None:
        super(ProjectsMainWindow, self).__init__()
        self.ui = uic.loadUi("ui/MainWindowProjects.ui", self)
        
        self.widget = None
        self.profileBtn.clicked.connect(self.switchToProfilePage)
        self.taskManagerBtn.clicked.connect(self.switchToTaskManager)
        self.add_button_projects.clicked.connect(self.addNewProject)
        
        self.projectsBtn.setStyleSheet('color: blue')
        
        
    def addNewProject(self):
        
    def setWidget(self, widget):
        self.widget = widget
        
    def switchToInboxWindow(self):
        self.widget.setCurrentIndex(3)
    
    def switchToTaskManager(self):
        self.widget.setCurrentIndex(0)
    
    def switchToProfilePage(self):
        self.widget.setCurrentIndex(2)