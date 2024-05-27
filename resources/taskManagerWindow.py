from PyQt6.QtWidgets import *
from PyQt6 import uic
from resources.addTaskWindow import AddTaskWindow

import resources.configUpdater as configUpdater

class TaskMainWindow(QFrame):
    def __init__(self) -> None:
        super(TaskMainWindow, self).__init__()
        
        self.ui = uic.loadUi("ui/MainWindowTaskManager.ui", self)
        
        self.widget = None
        self.addTask.clicked.connect(self.addNewTask)
        self.projectsBtn.clicked.connect(self.switchToProjectsPage)
        self.profileBtn.clicked.connect(self.switchToProfileWindow)
        
        
        
        self.taskManagerBtn.setStyleSheet('color: blue')
        
        config = configUpdater.Config()
        
        self.current_project = config.returnConfigProjectName()
        
        if config.returnConfigProjectName() == '':
            self.project_name_title.setText("Выберите проект!")
        
        else:
            
            try:
                self.project_name_title.setText(config.returnConfigProjectName()[:-3])
                
            except:
                pass
            
            
    def setCurProject(self):
        config = configUpdater.Config()
        self.current_project = config.returnConfigProjectName()
        self.project_name_title.setText(config.returnConfigProjectName()[:-3])
        
    def setWidget(self, widget):
        self.widget = widget
        
    def addNewTask(self):
        self.taskManagerWindow = AddTaskWindow()
        self.taskManagerWindow.show()
        
    def switchToProfileWindow(self):
        self.setCurProject()
        self.widget.setCurrentIndex(2)
    
    def switchToInboxWindow(self):
        self.setCurProject()
        self.widget.setCurrentIndex(3)
    
    def switchToProjectsPage(self):
        self.setCurProject()
        self.widget.setCurrentIndex(1)