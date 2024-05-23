import sqlite3, api_with_button, datetime


def insertDataProject(cursor: sqlite3.Cursor):
    # По нажатию кнопки, в случае Паши - Enter - я буду считывать информацию с тайтла таска, а затем буду считывать информацию с вкладки ниже
    if buttonEnter.clicked is True:
        currentDate = datetime.datetime.now().strftime('%Y-%m-%d')
        connection = sqlite3.connect("project.db")
        taskTitle = lineEdit.text()
        taskDescription = api_with_button.GeneratingPoints(taskTitle)
        cursor.execute(
            """INSERT INTO task (title, description, date) VALUES ({taskTitle}, {taskDescription}, {currentDate})
"""
        )
