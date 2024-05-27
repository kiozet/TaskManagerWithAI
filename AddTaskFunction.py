from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtWidgets import QVBoxLayout, QWidget, QGroupBox
import MainWindow
import TaskWidget
import sys


class TaskWidget(QtWidgets.QWidget, TaskWidget.Ui_TaskWidget):

    delete = pyqtSignal(int)

    def __init__(self, id_task: int):
        super().__init__()
        self.setupUi(self)
        self.id_task = id_task
        self.groupBox.setTitle(str(id_task))
        self.pushButtonDelete.clicked.connect(self.DeleteWidget)

    def DeleteWidget(self):
        self.delete.emit(self.id_task)


class MainWindow(QtWidgets.QMainWindow, MainWindow.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.id_task: int = 0
        self.pushButtonAddTask.clicked.connect(self.AddTaskWidget)
        self.task_widgets = {}

    def AddTaskWidget(self):
        self.id_task += 1
        widget = TaskWidget(self.id_task)
        self.TaskWidgetLayout.addWidget(widget)
        widget.delete.connect(self.DeleteWidget)
        self.task_widgets[self.id_task] = widget

    def DeleteWidget(self, id_task: int):
        widget = self.task_widgets.get(id_task)
        if widget:
            self.TaskWidgetLayout.removeWidget(widget)
            widget.deleteLater()

            del self.task_widgets[id_task]


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
