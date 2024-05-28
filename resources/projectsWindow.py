from PyQt6.QtWidgets import *
from PyQt6 import uic, QtCore
from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtWidgets import QVBoxLayout, QWidget, QGroupBox

import resources.taskWidget as taskWidget
import resources.configUpdater as configUpdater
import resources.database_helper as db

import sqlite3

import os


class TaskWidget(QtWidgets.QWidget, taskWidget.Ui_TaskWidget):

    delete = pyqtSignal(int)

    def __init__(self, id_task: int, project_title: str) -> None:
        super().__init__()
        self.setupUi(self)
        self.id_task = id_task
        self.project_title = project_title
        self.groupBox.setTitle(str(self.project_title[:-3:]))
        self.pushButtonDelete.clicked.connect(self.DeleteWidget)
        self.markProject.clicked.connect(self.markProjectFunc)

    def DeleteWidget(self):
        self.delete.emit(self.id_task)
        
    def markProjectFunc(self):
        config = configUpdater.Config()
        config.writeCurrentProject(self.project_title)


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
        
        self.cur_ind_proj = 0
        
        self.projectsDir = "projects/"
        
        self.setProjectList()     
            
        
    def setProjectList(self):
        for filename in os.listdir(self.projectsDir):
            self.cur_ind_proj += 1
            self.id_task += 1
            widget = TaskWidget(self.id_task, filename)
            self.projects_layout.addWidget(widget)
            widget.delete.connect(self.DeleteWidget)
            self.task_widgets[self.id_task] = widget
    
    def DeleteWidget(self, id_task: int):
        widget = self.task_widgets.get(id_task)
        project_title = widget.groupBox.title() + '.db'
        
        if widget:
            self.projects_layout.removeWidget(widget)
            widget.deleteLater()

            del self.task_widgets[id_task]
            
            os.remove(f'projects/{project_title}')
            
    def addNewProject(self):
        db.projectInitialization(f"{str(self.cur_ind_proj + 1)}")
        self.setProjectList()
        
    def setWidget(self, widget):
        self.widget = widget
        
    def switchToInboxWindow(self):
        self.widget.setCurrentIndex(3)
    
    def switchToTaskManager(self):
        self.widget.setCurrentIndex(0)
    
    def switchToProfilePage(self):
        self.widget.setCurrentIndex(2)