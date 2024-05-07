from PyQt6.QtWidgets import *
from PyQt6 import uic, QtCore
import sys

from projectsWindow import ProjectsMainWindow
from taskManagerWindow import TaskMainWindow
from profileWindow import ProfileMainWindow
from inboxWindow import InboxMainWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    widget = QStackedWidget()
    
    taskWindow = TaskMainWindow()
    projectsWindow = ProjectsMainWindow()
    profileWindow = ProfileMainWindow()
    inboxWindow = InboxMainWindow()
    
    widget.addWidget(taskWindow)
    widget.addWidget(projectsWindow)
    widget.addWidget(profileWindow)
    widget.addWidget(inboxWindow)
    
    taskWindow.setWidget(widget)
    inboxWindow.setWidget(widget)
    profileWindow.setWidget(widget)
    projectsWindow.setWidget(widget)
    
    widget.show()
    app.exec()


