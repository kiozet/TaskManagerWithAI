# Form implementation generated from reading ui file '.\VScode\task_manager\TaskWidget.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_TaskWidget(object):
    def setupUi(self, TaskWidget):
        TaskWidget.setObjectName("TaskWidget")
        TaskWidget.resize(200, 118)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TaskWidget.sizePolicy().hasHeightForWidth())
        TaskWidget.setSizePolicy(sizePolicy)
        TaskWidget.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        TaskWidget.setFont(font)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(TaskWidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(parent=TaskWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 80))
        self.groupBox.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButtonDelete = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButtonDelete.setObjectName("pushButtonDelete")
        self.horizontalLayout.addWidget(self.pushButtonDelete)
        self.pushButtonChoose = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButtonChoose.setObjectName("pushButtonChoose")
        self.horizontalLayout.addWidget(self.pushButtonChoose)
        self.pushButtonData = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButtonData.setObjectName("pushButtonData")
        self.horizontalLayout.addWidget(self.pushButtonData)
        self.pushButtonTransfer = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButtonTransfer.setObjectName("pushButtonTransfer")
        self.horizontalLayout.addWidget(self.pushButtonTransfer)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addWidget(self.groupBox)

        self.retranslateUi(TaskWidget)
        QtCore.QMetaObject.connectSlotsByName(TaskWidget)

    def retranslateUi(self, TaskWidget):
        _translate = QtCore.QCoreApplication.translate
        TaskWidget.setWindowTitle(_translate("TaskWidget", "Form"))
        self.groupBox.setTitle(_translate("TaskWidget", "GroupBox"))
        self.pushButtonDelete.setText(_translate("TaskWidget", "Delete"))
        self.pushButtonChoose.setText(_translate("TaskWidget", "Priortey"))
        self.pushButtonData.setText(_translate("TaskWidget", "Data"))
        self.pushButtonTransfer.setText(_translate("TaskWidget", "Transfer"))