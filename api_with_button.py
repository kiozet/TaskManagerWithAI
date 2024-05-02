from langchain.schema import HumanMessage, SystemMessage
from langchain.chat_models.gigachat import GigaChat
from PyQt6 import QtWidgets
import MyApp
import sys



class DesignApp(QtWidgets.QMainWindow, MyApp.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.button.clicked.connect(self.AddTitleTask)


    def AddTitleTask(self):
        title_task = self.lineEdit.text()
        self.textBrowser.setText(GeneratingPoints(title_task))


def GeneratingPoints(title_task):
    authorization = 'Mjk0MmQ0MmUtNTYyYy00NmY3LTlkYTctYTJhMzIyNmE5MTdhOmJkZTY5ZGE4LTMyZWUtNGNhZC1hNGNmLWIyYTc3NGI4Y2NhMg=='
    giga = GigaChat(credentials=authorization,
                    model='GigaChat:latest',
                    verify_ssl_certs=False
                    )
    messages = [SystemMessage(content= "Задача - {title_task}"
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


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = DesignApp()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()


