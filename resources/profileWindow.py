from PyQt6.QtWidgets import *
from PyQt6 import uic

import resources.configUpdater


class ProfileMainWindow(QFrame):
    def __init__(self) -> None:
        super(ProfileMainWindow, self).__init__()
        self.ui = uic.loadUi("ui/MainWindowProfile.ui", self)
        
        self.widget = None
        self.projectsBtn.clicked.connect(self.switchToProjectsPage)
        self.taskManagerBtn.clicked.connect(self.switchToTaskManager)
        
        self.profileBtn.setStyleSheet('color: blue')
        config = resources.configUpdater.Config()
        
        username, email = config.returnConfigStats()
        
        try:
            self.usernameLabel.setText(username)
            self.email_your_profile(email)
            
        except Exception as ex:
            print(f"Error: {ex}")
        
        
    def setWidget(self, widget):
        self.widget = widget
        
    def switchToInboxWindow(self):
        self.widget.setCurrentIndex(3)
    
    def switchToTaskManager(self):
        self.widget.setCurrentIndex(0)
    
    def switchToProjectsPage(self):
        self.widget.setCurrentIndex(1)