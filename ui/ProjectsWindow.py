# Form implementation generated from reading ui file 'MainWindowProjects.ui'
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
        Frame.resize(1193, 810)
        Frame.setMinimumSize(QtCore.QSize(1193, 810))
        Frame.setMaximumSize(QtCore.QSize(1193, 810))
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
        self.layoutWidget = QtWidgets.QWidget(parent=Frame)
        self.layoutWidget.setEnabled(True)
        self.layoutWidget.setGeometry(QtCore.QRect(-20, 230, 191, 176))
        font = QtGui.QFont()
        font.setFamily(".SF Soft Numeric")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferDefault)
        self.layoutWidget.setFont(font)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.projectsBtn = QtWidgets.QPushButton(parent=self.layoutWidget)
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
        self.taskManagerBtn = QtWidgets.QPushButton(parent=self.layoutWidget)
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
        self.inboxBtn = QtWidgets.QPushButton(parent=self.layoutWidget)
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
        self.profileBtn = QtWidgets.QPushButton(parent=self.layoutWidget)
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
        self.your_projects_label = QtWidgets.QLabel(parent=Frame)
        self.your_projects_label.setGeometry(QtCore.QRect(200, 60, 241, 81))
        self.your_projects_label.setObjectName("your_projects_label")
        self.project_list_widget = QtWidgets.QFrame(parent=Frame)
        self.project_list_widget.setGeometry(QtCore.QRect(210, 150, 771, 631))
        self.project_list_widget.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.project_list_widget.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.project_list_widget.setObjectName("project_list_widget")
        self.frame_2 = QtWidgets.QFrame(parent=self.project_list_widget)
        self.frame_2.setGeometry(QtCore.QRect(30, 40, 711, 80))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.layoutWidget1 = QtWidgets.QWidget(parent=self.frame_2)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 10, 681, 61))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.project_name_label = QtWidgets.QLabel(parent=self.layoutWidget1)
        self.project_name_label.setObjectName("project_name_label")
        self.horizontalLayout.addWidget(self.project_name_label)
        self.time_label = QtWidgets.QLabel(parent=self.layoutWidget1)
        self.time_label.setObjectName("time_label")
        self.horizontalLayout.addWidget(self.time_label)
        self.users_label = QtWidgets.QLabel(parent=self.layoutWidget1)
        self.users_label.setObjectName("users_label")
        self.horizontalLayout.addWidget(self.users_label)
        self.add_button_projects = QtWidgets.QToolButton(parent=Frame)
        self.add_button_projects.setGeometry(QtCore.QRect(390, 90, 23, 20))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../resourses.qrc/plus.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.add_button_projects.setIcon(icon)
        self.add_button_projects.setObjectName("add_button_projects")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.projectsBtn.setText(_translate("Frame", "Projects"))
        self.taskManagerBtn.setText(_translate("Frame", "Task Manager"))
        self.inboxBtn.setText(_translate("Frame", "Inbox"))
        self.profileBtn.setText(_translate("Frame", "Profile"))
        self.your_projects_label.setText(_translate("Frame", "Your projects"))
        self.project_name_label.setText(_translate("Frame", "Project_name"))
        self.time_label.setText(_translate("Frame", "Update_time"))
        self.users_label.setText(_translate("Frame", "Users"))
        self.add_button_projects.setText(_translate("Frame", "..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Frame = QtWidgets.QFrame()
    ui = Ui_Frame()
    ui.setupUi(Frame)
    Frame.show()
    sys.exit(app.exec())
