from PyQt6.QtWidgets import *
from PyQt6 import uic, QtCore
import sys


class InboxMainWindow(QFrame):
    def __init__(self) -> None:
        super(InboxMainWindow, self).__init__()
        self.ui = uic.loadUi("ui/MainWindowInbox1.0.ui", self)
        
        self.widget = None
        self.projectsBtn.clicked.connect(self.switchToProjectsPage)
        self.taskManagerBtn.clicked.connect(self.switchToTaskManager)
        self.profileBtn.clicked.connect(self.switchToProfileWindow)
        
        self.inboxBtn.setStyleSheet('color: blue')
        
        
    def setWidget(self, widget):
        self.widget = widget
        
    def switchToProfileWindow(self):
        self.widget.setCurrentIndex(2)
    
    def switchToTaskManager(self):
        self.widget.setCurrentIndex(0)
    
    def switchToProjectsPage(self):
        self.widget.setCurrentIndex(1)