from PyQt6.QtWidgets import *
from PyQt6 import uic, QtCore
from langchain.schema import HumanMessage, SystemMessage
from langchain.chat_models.gigachat import GigaChat
import time


class AddProjectWindow(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/AddProjectWindow.ui', self)
        