from PyQt6.QtWidgets import *
from PyQt6 import uic
from resources.addTaskWindow import AddTaskWindow
from PyQt6.QtWidgets import QVBoxLayout, QWidget, QGroupBox
from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt, pyqtSignal

import os

import resources.configUpdater as configUpdater
import resources.tasksWidget as taskWidget
import resources.database_helper as db

class TaskWidget(QtWidgets.QWidget, taskWidget.Ui_TaskWidget):

    delete = pyqtSignal(int)
    choose = pyqtSignal(int)
    transfer = pyqtSignal(int)

    def __init__(self, id_task: int):
        super().__init__()
        self.setupUi(self)
        self.id_task = id_task
        self.groupBox.setTitle(str(id_task))
        self.pushButtonDelete.clicked.connect(self.DeleteWidget)
        self.pushButtonChoose.clicked.connect(self.ChooseWidget)  # priority
        self.pushButtonTransfer.clicked.connect(self.TransferWidget)

    def DeleteWidget(self):
        self.delete.emit(self.id_task)

    def ChooseWidget(self):
        self.choose.emit(self.id_task)

    def TransferWidget(self):
        self.transfer.emit(self.id_task)

class TaskMainWindow(QFrame):
    def __init__(self) -> None:
        super(TaskMainWindow, self).__init__()
        
        self.ui = uic.loadUi("ui/MainWindowTaskManager.ui", self)
        
        self.widget = None
        self.projectsBtn.clicked.connect(self.switchToProjectsPage)
        self.profileBtn.clicked.connect(self.switchToProfileWindow)
        
        self.id_task: int = 0
        self.count_task: int = 0
        self.addTask.clicked.connect(self.AddTaskWidget)
        
        self.taskManagerBtn.setStyleSheet('color: blue')
        
        config = configUpdater.Config()
        
        self.current_project = config.returnConfigProjectName()
        
        if config.returnConfigProjectName() == '':
            self.project_name_title.setText("Выберите проект!")
        
        else:
            
            try:
                self.setCurProject()
                # читаете бдшку и заполняете тасками по статусу
            except:
                pass
            
            
    def setCurProject(self):
        config = configUpdater.Config()
        self.current_project = config.returnConfigProjectName()
        self.project_name_title.setText(config.returnConfigProjectName()[:-3])
        
        db.readTasks(self.current_project)
        
        
        
    def setWidget(self, widget):
        self.widget = widget
        
    def AddTaskWidget(self):
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