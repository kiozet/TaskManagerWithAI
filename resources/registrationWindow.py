from PyQt6.QtWidgets import *
from PyQt6 import uic
from PyQt6.QtGui import QMovie
from PyQt6.QtCore import pyqtSignal, pyqtSlot, QRunnable, QThreadPool
import time
import os

from resources.database_helper import *
import resources.vadlidationFunc


class LineEditData(QRunnable):
    def __init__(self, registrationWindow) -> None:
        super(LineEditData, self).__init__()

        self.threadpool = QThreadPool()
        self.registrationWindow = registrationWindow      

    @pyqtSlot()
    def run(self):
        privUsrName = ""
        privEmail = ""
        privPassword = ""
        gifState = False

        while True:
            usrNameBool = (self.registrationWindow.usr_name_text_reg.text() != "") and (
                self.registrationWindow.usr_name_text_reg.text() != privUsrName
            )
            emailBool = (self.registrationWindow.email_text_reg.text() != "") and (
                self.registrationWindow.email_text_reg.text() != privEmail
            )
            passwordBool = (self.registrationWindow.password_text_reg.text() != "") and (
                self.registrationWindow.password_text_reg.text() != privPassword
            )

            if (
                (usrNameBool == True) or (emailBool == True) or (passwordBool == True)
            ) and (gifState == False):
                self.registrationWindow.gifStateSignalEmit(True)
                gifState = True

                privUsrName = self.registrationWindow.usr_name_text_reg.text()
                privEmail = self.registrationWindow.email_text_reg.text()
                privPassword = self.registrationWindow.password_text_reg.text()

                time.sleep(0.6)

            else:
                gifState = False
                self.registrationWindow.gifStateUpdater(False)


class RegistrationWindow(QFrame):
    gifStateSignal = pyqtSignal(bool)

    def __init__(self) -> None:
        super().__init__()
        
        self.ui = uic.loadUi("ui/registr.ui", self)
        
        self.widget = None
        
        self.movie = QMovie("content/pedro-racoon.gif")
        self.GIF.setMovie(self.movie)

        self.threadpool = QThreadPool()
        self.gifAnimation()
        
        self.confirm_button_reg.clicked.connect(self.regCheck)

        self.gifStateSignal.connect(self.gifStateUpdater)

    def regCheck(self):
        userName = self.usr_name_text_reg.text()
        email = self.email_text_reg.text()
        password = self.password_text_reg.text()
        
        if resources.vadlidationFunc.emailValidation(email):
            userDatabaseInitialization()
            registrationDataInsert(email=email, login=userName, password=password)
            self.widget.setCurrentIndex(2)
            
        
        
    def gifStateSignalEmit(self, state: bool) -> None:
        self.gifStateSignal.emit(state)

    def gifAnimation(self):
        gifAnimation = LineEditData(registrationWindow=self)
        self.threadpool.start(gifAnimation)

    def gifStateUpdater(self, state: bool) -> None:
        if state == True:
            self.movie.start()

        else:
            self.movie.setPaused(True)
    
    def setWidget(self, widget):
        self.widget = widget