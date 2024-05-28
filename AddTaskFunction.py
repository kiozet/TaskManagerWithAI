from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtWidgets import QVBoxLayout, QWidget, QGroupBox
import MainWindowTaskManager
import TaskWidget
import sys


class TaskWidget(QtWidgets.QWidget, TaskWidget.Ui_TaskWidget):

    delete = pyqtSignal(int)
    choose = pyqtSignal(int)

    def __init__(self, id_task: int):
        super().__init__()
        self.setupUi(self)
        self.id_task = id_task
        self.groupBox.setTitle(str(id_task))
        self.pushButtonDelete.clicked.connect(self.DeleteWidget)
        self.pushButtonChoose.clicked.connect(self.ChooseWidget)

    def DeleteWidget(self):
        self.delete.emit(self.id_task)

    def ChooseWidget(self):
        self.choose.emit(self.id_task)


class MainWindow(QtWidgets.QFrame, MainWindowTaskManager.Ui_Frame):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.id_task: int = 0
        self.pushButtonAddTask.clicked.connect(self.AddTaskWidget)
        self.task_widgets = {}

    def AddTaskWidget(self):
        self.id_task += 1
        widget = TaskWidget(self.id_task)
        self.verticalLayoutToDo.addWidget(widget)
        widget.delete.connect(self.DeleteWidget)
        widget.choose.connect(self.ChooseWidget)
        self.task_widgets[self.id_task] = widget

    def DeleteWidget(self, id_task: int):
        widget = self.task_widgets.get(id_task)
        if widget:
            self.verticalLayoutToDo.removeWidget(widget)
            widget.deleteLater()

            del self.task_widgets[id_task]

    def ChooseWidget(self, id_task: int):
        widget = self.task_widgets.get(id_task)
        if widget:
            self.verticalLayoutToDo.removeWidget(widget)
            self.verticalLayoutToDo.insertWidget(0, widget)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
