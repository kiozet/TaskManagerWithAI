from PyQt6.QtWidgets import *
from PyQt6 import uic, QtCore
from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtWidgets import QVBoxLayout, QWidget, QGroupBox
import resources.taskWidget as taskWidget

import os


class TaskWidget(QtWidgets.QWidget, taskWidget.Ui_TaskWidget):

    delete = pyqtSignal(int)

    def __init__(self, id_task: int):
        super().__init__()
        self.setupUi(self)
        self.id_task = id_task
        self.groupBox.setTitle(str(id_task))
        self.pushButtonDelete.clicked.connect(self.DeleteWidget)

    def DeleteWidget(self):
        self.delete.emit(self.id_task)


class ProjectsMainWindow(QFrame):
    def __init__(self) -> None:
        super(ProjectsMainWindow, self).__init__()
        self.ui = uic.loadUi("ui/MainWindowProjects.ui", self)
        
        self.widget = None
        self.profileBtn.clicked.connect(self.switchToProfilePage)
        self.taskManagerBtn.clicked.connect(self.switchToTaskManager)
        self.add_button_projects.clicked.connect(self.addNewProject)
        
        self.projectsBtn.setStyleSheet('color: blue')
        
        self.id_task: int = 0
        self.task_widgets = {}
        
        self.projectsDir = "projects/"
        
        for filename in os.listdir(self.projectsDir):
            self.id_task += 1
            widget = TaskWidget(self.id_task)
            self.TaskWidgetLayout.addWidget(widget)
            widget.delete.connect(self.DeleteWidget)
            self.task_widgets[self.id_task] = widget
            
        
        
    def addNewProject(self):
        print(os.path.basename(self.projectsDir))
        
    def setWidget(self, widget):
        self.widget = widget
        
    def switchToInboxWindow(self):
        self.widget.setCurrentIndex(3)
    
    def switchToTaskManager(self):
        self.widget.setCurrentIndex(0)
    
    def switchToProfilePage(self):
        self.widget.setCurrentIndex(2)