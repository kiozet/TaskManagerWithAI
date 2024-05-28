from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtWidgets import QVBoxLayout, QWidget, QGroupBox
import MainWindowTaskManager
import TaskWidget
import sys


class TaskWidget(QtWidgets.QWidget, TaskWidget.Ui_TaskWidget):

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


class MainWindow(QtWidgets.QFrame, MainWindowTaskManager.Ui_Frame):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.id_task: int = 0
        self.count_task: int = 0
        self.pushButtonAddTask.clicked.connect(self.AddTaskWidget)
        self.task_widgets = {}

    def AddTaskWidget(self):
        self.id_task += 1
        self.count_task += 1
        self.labelAllTask.setText(str(self.count_task))
        widget = TaskWidget(self.id_task)
        self.verticalLayoutToDo.addWidget(widget)
        widget.delete.connect(self.DeleteWidget)
        widget.choose.connect(self.ChooseWidget)  # priority
        widget.transfer.connect(self.TransferWidget)
        self.task_widgets[self.id_task] = widget

    def DeleteWidget(self, id_task: int):
        if id_task in self.task_widgets:
            self.count_task -= 1
            widget = self.task_widgets.get(id_task)
            widget = self.task_widgets.pop(id_task)
            if widget:
                self.verticalLayoutToDo.removeWidget(widget)
                widget.deleteLater()
                self.labelAllTask.setText(str(self.count_task))

    def ChooseWidget(self, id_task: int):  # priority
        widget = self.task_widgets.get(id_task)
        if widget:
            self.verticalLayoutToDo.removeWidget(widget)
            self.verticalLayoutToDo.insertWidget(0, widget)
            widget.groupBox.setTitle(f"{id_task} Priority")

    def TransferWidget(self, id_task: int):
        widget = self.task_widgets.get(id_task)
        if widget:
            self.verticalLayoutToDo.removeWidget(widget)
            self.verticalLayoutToDo.addWidget(widget)
            self.verticalLayoutInProgress.insertWidget(0, widget)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
