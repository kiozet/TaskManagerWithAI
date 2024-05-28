from PyQt6.QtWidgets import *
from PyQt6 import uic, QtCore
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from langchain.schema import HumanMessage, SystemMessage
from langchain.chat_models.gigachat import GigaChat
import time

import resources.api as api
import resources.database_helper as bd
import os
import subprocess


def GeneratingPoints(title_task: str) -> str:
    print(123)
    authorization = "Mjk0MmQ0MmUtNTYyYy00NmY3LTlkYTctYTJhMzIyNmE5MTdhOmJkZTY5ZGE4LTMyZWUtNGNhZC1hNGNmLWIyYTc3NGI4Y2NhMg=="
    giga = GigaChat(
        credentials=authorization, model="GigaChat:latest", verify_ssl_certs=False
    )
    print(52)
    messages = [
        SystemMessage(
            content="Задача - {title_task}"
            "Разбей данную задачу на подпункты."
            "Без примеров."
            "Пиши пункты друг под другом."
            "Используй нумерацию."
        )
    ]
    messages.append(HumanMessage(content=title_task))
    answer = giga(messages)
    messages.append(answer)

    return answer.content


class AddTaskWindow(QWidget):
    def __init__(self, project):
        super().__init__()
        uic.loadUi("ui/GenerationTaskWindow.ui", self)

        self.current_project = project
        self.generateBtn.clicked.connect(self.AddTitleTask)
        self.threadpool = QThreadPool()
        self.calendarWidget.clicked.connect(self.calendar)
        self.date = ""

    def calendar(self):
        selected_date = self.calendarWidget.selectedDate()  # Получение объекта QDate
        self.date = selected_date.toString()
        print(self.date)

    def AddTitleTask(self):
        title_task = self.taskName.text()
        generatedContent = GeneratingPoints(title_task)

        animatingContent = ""

        for charIndex in range(0, len(generatedContent)):
            animatingContent += generatedContent[charIndex]
            self.taskContent.setText(animatingContent)
            QtCore.QCoreApplication.processEvents()
            time.sleep(0.05)

        bd.taskDataInsert(
            title=title_task,
            desription=generatedContent,
            status="ToDo",
            deadline=f"{str(self.date)}",
            project=self.current_project,
        )
