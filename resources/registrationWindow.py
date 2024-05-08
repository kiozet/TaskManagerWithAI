from PyQt6.QtWidgets import *
from PyQt6 import uic, QtCore
from PyQt6.QtGui import QMovie
from PyQt6.QtCore import QThread, pyqtSignal, pyqtSlot, QRunnable, QThreadPool
import sys
import time


class LineEditData(QRunnable):
    def __init__(self) -> None:
        super(LineEditData, self).__init__()

        self.threadpool = QThreadPool()


    @pyqtSlot()
    def run(self):
        privUsrName = ""
        privEmail = ""
        privPassword = ""
        gifState = False

        while True:
            usrNameBool = (registrationWindow.usr_name_text_reg.text() != "") and (
                registrationWindow.usr_name_text_reg.text() != privUsrName
            )
            emailBool = (registrationWindow.email_text_reg.text() != "") and (
                registrationWindow.email_text_reg.text() != privEmail
            )
            passwordBool = (registrationWindow.password_text_reg.text() != "") and (
                registrationWindow.password_text_reg.text() != privPassword
            )

            if (
                (usrNameBool == True) or (emailBool == True) or (passwordBool == True)
            ) and (gifState == False):
                registrationWindow.gifStateSignalEmit(True)
                gifState = True

                privUsrName = registrationWindow.usr_name_text_reg.text()
                privEmail = registrationWindow.email_text_reg.text()
                privPassword = registrationWindow.password_text_reg.text()

                time.sleep(0.6)

            else:
                gifState = False
                registrationWindow.gifStateUpdater(False)


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

        self.gifStateSignal.connect(self.gifStateUpdater)

    def gifStateSignalEmit(self, state: bool) -> None:
        self.gifStateSignal.emit(state)

    def gifAnimation(self):
        gifAnimation = LineEditData()
        self.threadpool.start(gifAnimation)

    def gifStateUpdater(self, state: bool) -> None:
        if state == True:
            self.movie.start()

        else:
            self.movie.setPaused(True)
    
    def setWidget(self, widget):
        self.widget = widget


if __name__ == "__main__":
    app = QApplication(sys.argv)
    registrationWindow = RegistrationWindow()
    registrationWindow.show()
    app.exec()
