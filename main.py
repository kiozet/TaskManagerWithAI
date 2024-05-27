from PyQt6.QtWidgets import *
import sys

from resources.projectsWindow import ProjectsMainWindow
from resources.taskManagerWindow import TaskMainWindow
from resources.profileWindow import ProfileMainWindow
from resources.configUpdater import Config
from resources.registrationWindow import RegistrationWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    widget = QStackedWidget()
    
    taskWindow = TaskMainWindow()
    projectsWindow = ProjectsMainWindow()
    profileWindow = ProfileMainWindow()
    registrationWindow = RegistrationWindow()
    config = Config()
    
    widget.addWidget(taskWindow)
    widget.addWidget(projectsWindow)
    widget.addWidget(profileWindow)
    widget.addWidget(registrationWindow)
    
    taskWindow.setWidget(widget)
    profileWindow.setWidget(widget)
    projectsWindow.setWidget(widget)
    registrationWindow.setWidget(widget)
    
    if config.returnDBStatus():
        # task manager window
        widget.show()
        app.exec()
        
    else:
        # reg/auth window
        widget.setCurrentIndex(3)
        widget.show()
        app.exec()


