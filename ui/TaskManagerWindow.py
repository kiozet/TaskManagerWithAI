# Form implementation generated from reading ui file 'MainWindowTaskManager1.0.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.setEnabled(True)
        Frame.resize(941, 669)
        font = QtGui.QFont()
        font.setFamily(".SF Soft Numeric")
        font.setPointSize(19)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        Frame.setFont(font)
        Frame.setMouseTracking(False)
        Frame.setAutoFillBackground(False)
        Frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        Frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(Frame)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.projectsBtn = QtWidgets.QPushButton(parent=Frame)
        self.projectsBtn.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily(".SF Soft Numeric")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferDefault)
        self.projectsBtn.setFont(font)
        self.projectsBtn.setAutoDefault(False)
        self.projectsBtn.setFlat(True)
        self.projectsBtn.setObjectName("projectsBtn")
        self.verticalLayout_6.addWidget(self.projectsBtn)
        self.taskManagerBtn = QtWidgets.QPushButton(parent=Frame)
        self.taskManagerBtn.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily(".SF Soft Numeric")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferDefault)
        self.taskManagerBtn.setFont(font)
        self.taskManagerBtn.setFlat(True)
        self.taskManagerBtn.setObjectName("taskManagerBtn")
        self.verticalLayout_6.addWidget(self.taskManagerBtn)
        self.inboxBtn = QtWidgets.QPushButton(parent=Frame)
        self.inboxBtn.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily(".SF Soft Numeric")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferDefault)
        self.inboxBtn.setFont(font)
        self.inboxBtn.setFlat(True)
        self.inboxBtn.setObjectName("inboxBtn")
        self.verticalLayout_6.addWidget(self.inboxBtn)
        self.profileBtn = QtWidgets.QPushButton(parent=Frame)
        self.profileBtn.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily(".SF Soft Numeric")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferDefault)
        self.profileBtn.setFont(font)
        self.profileBtn.setFlat(True)
        self.profileBtn.setObjectName("profileBtn")
        self.verticalLayout_6.addWidget(self.profileBtn)
        self.horizontalLayout_5.addLayout(self.verticalLayout_6)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.project_name_title = QtWidgets.QLabel(parent=Frame)
        font = QtGui.QFont()
        font.setFamily("The Duke of Prunes")
        font.setPointSize(19)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setKerning(False)
        self.project_name_title.setFont(font)
        self.project_name_title.setMouseTracking(True)
        self.project_name_title.setObjectName("project_name_title")
        self.verticalLayout_5.addWidget(self.project_name_title)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.tasks_info = QtWidgets.QFrame(parent=Frame)
        self.tasks_info.setObjectName("tasks_info")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tasks_info)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(6, -1, 7, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_8 = QtWidgets.QLabel(parent=self.tasks_info)
        font = QtGui.QFont()
        font.setFamily("The Duke of Prunes")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_3.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(parent=self.tasks_info)
        font = QtGui.QFont()
        font.setFamily("The Duke of Prunes")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_3.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(parent=self.tasks_info)
        font = QtGui.QFont()
        font.setFamily("The Duke of Prunes")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_3.addWidget(self.label_10)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(6, 0, 8, -1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.all_tasks_numb = QtWidgets.QLabel(parent=self.tasks_info)
        self.all_tasks_numb.setObjectName("all_tasks_numb")
        self.verticalLayout_4.addWidget(self.all_tasks_numb)
        self.done_tasks_numb = QtWidgets.QLabel(parent=self.tasks_info)
        self.done_tasks_numb.setObjectName("done_tasks_numb")
        self.verticalLayout_4.addWidget(self.done_tasks_numb)
        self.frozen_tasks_numb = QtWidgets.QLabel(parent=self.tasks_info)
        self.frozen_tasks_numb.setObjectName("frozen_tasks_numb")
        self.verticalLayout_4.addWidget(self.frozen_tasks_numb)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.gridLayout.addWidget(self.tasks_info, 0, 2, 1, 1)
        self.pr_description = QtWidgets.QLabel(parent=Frame)
        self.pr_description.setStyleSheet("")
        self.pr_description.setObjectName("pr_description")
        self.gridLayout.addWidget(self.pr_description, 0, 1, 1, 1)
        self.project_info = QtWidgets.QWidget(parent=Frame)
        font = QtGui.QFont()
        font.setFamily(".SF Soft Numeric")
        font.setPointSize(19)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferDefault)
        self.project_info.setFont(font)
        self.project_info.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.NoContextMenu)
        self.project_info.setStyleSheet("")
        self.project_info.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhNone)
        self.project_info.setObjectName("project_info")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.project_info)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(6, -1, 7, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=self.project_info)
        font = QtGui.QFont()
        font.setFamily("The Duke of Prunes")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferDefault)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(parent=self.project_info)
        font = QtGui.QFont()
        font.setFamily("The Duke of Prunes")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferDefault)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(parent=self.project_info)
        font = QtGui.QFont()
        font.setFamily("The Duke of Prunes")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferDefault)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(6, 0, 8, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pr_date_added = QtWidgets.QLabel(parent=self.project_info)
        self.pr_date_added.setObjectName("pr_date_added")
        self.verticalLayout_2.addWidget(self.pr_date_added)
        self.pr_deadline = QtWidgets.QLabel(parent=self.project_info)
        self.pr_deadline.setObjectName("pr_deadline")
        self.verticalLayout_2.addWidget(self.pr_deadline)
        self.pr_participants = QtWidgets.QLabel(parent=self.project_info)
        self.pr_participants.setObjectName("pr_participants")
        self.verticalLayout_2.addWidget(self.pr_participants)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.gridLayout.addWidget(self.project_info, 0, 0, 1, 1)
        self.verticalLayout_5.addLayout(self.gridLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetFixedSize)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(parent=Frame)
        font = QtGui.QFont()
        font.setFamily("The Duke of Prunes")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.addTask = QtWidgets.QToolButton(parent=Frame)
        self.addTask.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../resourses.qrc/plus.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.addTask.setIcon(icon)
        self.addTask.setObjectName("addTask")
        self.horizontalLayout_3.addWidget(self.addTask)
        self.label_5 = QtWidgets.QLabel(parent=Frame)
        font = QtGui.QFont()
        font.setFamily("The Duke of Prunes")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(parent=Frame)
        font = QtGui.QFont()
        font.setFamily("The Duke of Prunes")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-colour: rgba(255, 255, 255, 30)\n"
"")
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(parent=Frame)
        font = QtGui.QFont()
        font.setFamily("The Duke of Prunes")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_14 = QtWidgets.QLabel(parent=Frame)
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_4.addWidget(self.label_14)
        self.label_13 = QtWidgets.QLabel(parent=Frame)
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_4.addWidget(self.label_13)
        self.label_12 = QtWidgets.QLabel(parent=Frame)
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_4.addWidget(self.label_12)
        self.label_11 = QtWidgets.QLabel(parent=Frame)
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_4.addWidget(self.label_11)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5.addLayout(self.verticalLayout_5)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.projectsBtn.setText(_translate("Frame", "Projects"))
        self.taskManagerBtn.setText(_translate("Frame", "Task Manager"))
        self.inboxBtn.setText(_translate("Frame", "Inbox"))
        self.profileBtn.setText(_translate("Frame", "Profile"))
        self.project_name_title.setText(_translate("Frame", "Project name"))
        self.label_8.setText(_translate("Frame", "All tasks:"))
        self.label_9.setText(_translate("Frame", "Done:"))
        self.label_10.setText(_translate("Frame", "Frozen:"))
        self.all_tasks_numb.setText(_translate("Frame", "цифра"))
        self.done_tasks_numb.setText(_translate("Frame", "цифра"))
        self.frozen_tasks_numb.setText(_translate("Frame", "цифра"))
        self.pr_description.setText(_translate("Frame", "описание"))
        self.label.setText(_translate("Frame", "Date added:"))
        self.label_2.setText(_translate("Frame", "Deadline:"))
        self.label_3.setText(_translate("Frame", "Participants:"))
        self.pr_date_added.setText(_translate("Frame", "дата"))
        self.pr_deadline.setText(_translate("Frame", "время"))
        self.pr_participants.setText(_translate("Frame", "твоя семья"))
        self.label_4.setText(_translate("Frame", "To do"))
        self.label_5.setText(_translate("Frame", "In progress"))
        self.label_6.setText(_translate("Frame", "Closed"))
        self.label_7.setText(_translate("Frame", "Frozen"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Frame = QtWidgets.QFrame()
    ui = Ui_Frame()
    ui.setupUi(Frame)
    Frame.show()
    sys.exit(app.exec())