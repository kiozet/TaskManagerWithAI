from PyQt6.QtWidgets import *
from PyQt6 import uic


class ProfileMainWindow(QFrame):
    def __init__(self) -> None:
        super(ProfileMainWindow, self).__init__()
        self.ui = uic.loadUi("ui/MainWindowProfile1.0.ui", self)
        
        self.widget = None
        self.projectsBtn.clicked.connect(self.switchToProjectsPage)
        self.taskManagerBtn.clicked.connect(self.switchToTaskManager)
        self.inboxBtn.clicked.connect(self.switchToInboxWindow)
        
        self.profileBtn.setStyleSheet('color: blue')
        
        
    def setWidget(self, widget):
        self.widget = widget
        
    def switchToInboxWindow(self):
        self.widget.setCurrentIndex(3)
    
    def switchToTaskManager(self):
        self.widget.setCurrentIndex(0)
    
    def switchToProjectsPage(self):
        self.widget.setCurrentIndex(1)