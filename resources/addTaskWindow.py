from PyQt6.QtWidgets import *
from PyQt6 import uic, QtCore
from langchain.schema import HumanMessage, SystemMessage
from langchain.chat_models.gigachat import GigaChat
import time


class AddTaskWindow(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/GenerationTaskWindow.ui', self)
        
        self.generateBtn.clicked.connect(self.AddTitleTask)
        
        
    def AddTitleTask(self):
        taskTitle = self.taskName.text()
        generatedContent = GeneratingPoints(taskTitle)

        animatingContent = ""

        for charIndex in range(0, len(generatedContent)):
            animatingContent += generatedContent[charIndex]
            self.taskContent.setText(animatingContent)
            QtCore.QCoreApplication.processEvents()
            time.sleep(0.05)
            
            
def GeneratingPoints(title_task: str) -> str:
    authorization = "Mjk0MmQ0MmUtNTYyYy00NmY3LTlkYTctYTJhMzIyNmE5MTdhOmJkZTY5ZGE4LTMyZWUtNGNhZC1hNGNmLWIyYTc3NGI4Y2NhMg=="
    giga = GigaChat(
        credentials=authorization, model="GigaChat:latest", verify_ssl_certs=False
    )
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