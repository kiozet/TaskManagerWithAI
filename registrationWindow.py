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
        privUsrName = ''
        privEmail = ''
        privPassword =''
        gifState = False
        
        while True:
            usrNameBool = (displayFrame.usr_name_text_reg.text() != "") and (displayFrame.usr_name_text_reg.text() != privUsrName)
            emailBool = (displayFrame.email_text_reg.text() != "") and (displayFrame.email_text_reg.text() != privEmail)
            passwordBool = (displayFrame.password_text_reg.text() != "") and (displayFrame.password_text_reg.text() != privPassword)
            
            if  ((usrNameBool == True)or (emailBool == True) or (passwordBool == True)) and (gifState == False):
                displayFrame.gifStateSignalEmit(True)
                gifState = True
                privUsrName = displayFrame.usr_name_text_reg.text()
                privEmail = displayFrame.email_text_reg.text()
                privPassword = displayFrame.password_text_reg.text()
                time.sleep(0.6)
                
            else:
                gifState = False
                displayFrame.gifStateUpdater(False)        
        
    
class RegistrationWindow(QFrame):
    gifStateSignal = pyqtSignal(bool)
    
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi('ui/registr.ui', self)
        
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
              
        
if __name__ == '__main__':  
    app = QApplication(sys.argv)
    displayFrame = RegistrationWindow()
    displayFrame.show()
    app.exec()
