import sqlite3


# Нужно понять, какое имя базы данных вначале создавать: либо делаем скрипт, который пишет project1, project2 ... , project n, либо как то по-другому
def projectInitialization(cursor: sqlite3.Cursor) -> bool:
    if addTask.clicked is True:
        newDatabase = open("project.db", "w+")
        newDatabase.close()
        connection = sqlite3.connect("project.db")
        try:
            """Create table func, args: connection: sqlite3.Connection, cursor: sqlite3.Cursor from your
            sqlite3 db"""

            cursor.execute(
                """CREATE TABLE IF NOT EXISTS task(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            description TEXT,
            date TEXT
            )"""
            )

            connection.commit()

            return True

        except Exception as ex:
            return False
