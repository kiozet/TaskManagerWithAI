from PyQt6.QtWidgets import *
from PyQt6 import uic, QtCore
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from langchain.schema import HumanMessage, SystemMessage
from langchain.chat_models.gigachat import GigaChat
import time

import os


class Worker(QRunnable):
    def __init__(self, addTaskWindow) -> None:
        super().__init__()
        
        self.addTaskWindow = addTaskWindow
        
    '''
    Worker thread
    '''

    @pyqtSlot()
    def run(self):
        
        taskTitle = self.addTaskWindow.taskName.text()

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
        
        messages.append(HumanMessage(content=taskTitle))
        answer = giga(messages)

        messages.append(answer)

        generatedContent = answer.content
        
        animatingContent = ""

        for charIndex in range(0, len(generatedContent)):
            animatingContent += generatedContent[charIndex]
            self.addTaskWindow.taskContent.setText(animatingContent)
            QtCore.QCoreApplication.processEvents()
            time.sleep(0.05)
        

class AddTaskWindow(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/GenerationTaskWindow.ui', self)
        
        self.generateBtn.clicked.connect(self.AddTitleTask)
        self.threadpool = QThreadPool()
        
     
    def AddTitleTask(self):
            worker = Worker(self)
            self.threadpool.start(worker)
            
class API(QRunnable):  
    @pyqtSlot()        
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