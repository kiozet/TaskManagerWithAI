import sqlite3, os


# Функция, которая создает новую бд для нового таска, а также таблицу для заголовка, описания, дату создания, дедлайн и состояния таска
def projectInitialization(name: str, cursor: sqlite3.Cursor) -> bool:
    newDatabase = open(f"{name}.db", "w+")
    newDatabase.close()
    connection = sqlite3.connect(f"{name}.db")
    try:
        """Create table func, args: connection: sqlite3.Connection, cursor: sqlite3.Cursor from your
        sqlite3 db"""
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS task(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        description TEXT,
        status TEXT,
        dateCreated TEXT,
        deadline TEXT
        )"""
        )
        connection.commit()
        cursor.close()
        return True
    except Exception as ex:
        return False

# allTasks INTEGER DEFAULT 0,
# doneTasks INTEGER DEFAULT 0,
# frozenTasks INTEGER DEFAULT 0

# Функция, которая создаёт бд для юзеров, создает таблицу со значениями:
def userDatabaseInitialization() -> bool:
    connection = sqlite3.connect("content/users.db")
    cursor = connection.cursor()
    
    try:
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS users(
            email TEXT NOT NULL,
            login TEXT NOT NULL,
            password TEXT NOT NULL          
            )"""
        )
        connection.commit()
        cursor.close()
        connection.close()
        return True
    
    except Exception as ex:
        print(f"Rised error: {ex}!")
        return False


# Функция, которая добавляет данные о таски в таблицу, такие как: заголовок, описание, дата создания, статус, дедлайн. По умолчанию состояние таска стоит на "onProggress"
def taskDataInsert(
    title: str, desription: str, dateCreated: str, deadline: str, cursor: sqlite3.Cursor
) -> bool:
    try:
        connection = sqlite3.connect("project.db")
        sqliteInsertWithParam = """INSERT INTO task (title, description, status, dateCreated, deadline) VALUES (?, ?, onProggress, ?, ?)
"""
        dataTuple = (title, desription, dateCreated, deadline)
        cursor.execute(sqliteInsertWithParam, dataTuple)
        connection.commit()
        cursor.close()
        return True
    except Exception as ex:
        return False


# Функция, которая добавляет значения email, login, password в таблицу users при регистрации пользователя
def registrationDataInsert(
    email: str, login: str, password: str
) -> bool:
    connection = sqlite3.connect("content/users.db")
    cursor = connection.cursor()
    try:
        cursor.execute(
                    "INSERT INTO users (email, login, password) VALUES (?, ?, ?)",
                    (
                        email,
                        login,
                        password,
                    ),
                )
        connection.commit()
        connection.close()
        return True
    
    except Exception as ex:
        print(ex)
        return False


# Функция, которая добавляет значения telegrammID, name, surname, photo в таблицу users при указании их в профиле пользователя
def profileDataInsert(
    telegrammID: str, name: str, surname: str, photo: bytes, cursor: sqlite3.Cursor
):
    connection = sqlite3.connect("users.db")
    try:
        sqliteInsertWithParam = """INSERT INTO users (telegrammID, name, surname, photo) VALUES (?, ?, ?, ?)
"""
        dataTuple = (telegrammID, name, surname, photo)
        cursor.execute(sqliteInsertWithParam, dataTuple)
        connection.commit()
        cursor.close()
        return True
    except Exception as ex:
        return False


# Доделать функцию удаления пользователя, при которой будет также удаляться бд таска
# def deleteUser(login):
# Удаление project-а. Не знаю как сделать нормально, сделал пока так.
def deleteTaskDB(title: str) -> bool:
    fileName = f"{title}.db"
    if os.path.exists(fileName):
        os.remove(fileName)
        return True


# Функция, которая удаляет определенную задачу проекта, принимает на вход название таска, чтобы можно было удалить связанную с ним таблицу
def deleteTaskTable(title: str, cursor: sqlite3.Cursor) -> bool:
    connection = sqlite3.connect("project.db")
    sqliteDeleteTable = """DROP TABLE ?"""
    cursor.execute(sqliteDeleteTable, (title,))
    connection.commit()
    cursor.close()


# Функция, которая изменяет статус таска. Принимает на вход название таска, чтобы можно было отследить в бд, название столбца, чтобы можно было изменить статус в бд.
def changeTasksStatus(tasksTitle: str, columnName: str, cursor: sqlite3.Cursor) -> bool:
    connection = sqlite3.connect("project.db")
    if columnName == "Closed":
        sqliteUpdateStatus = (
            """UPDATE task SET doneTasks = doneTasks + 1 WHERE title = ?"""
        )
        cursor.execute(sqliteUpdateStatus, (tasksTitle,))
    else:
        sqliteUpdateStatus = (
            """UPDATE task SET frozenTasks = frozenTasks + 1 WHERE title = ?"""
        )
        cursor.execute(sqliteUpdateStatus, (tasksTitle,))
    try:
        sqliteUpdateWithParam = """UPDATE task SET status = ? WHERE title = ?"""
        dataTuple = (columnName, tasksTitle)
        cursor.execute(sqliteUpdateWithParam, dataTuple)
        connection.commit()
        cursor.close()
        return True
    except Exception as ex:
        return False


# Функция, которая меняет пароль в бд. На вход подается логин и новый пароль, логин - чтобы отследить в базе данных юзера
def changePassword(login: str, newPassword: str, cursor: sqlite3.Cursor) -> bool:
    try:
        connection = sqlite3.connect("users.db")
        sqliteUpdatePassword = """UPDATE users SET password = ? WHERE login = ?"""
        dataTuple = (newPassword, login)
        cursor.execute(sqliteUpdatePassword, dataTuple)
        connection.commit
        cursor.close()
        return True
    except Exception as ex:
        return False


# Функция, которая меняет логин в бд. На вход подается старый логин и новый логин, старый логин - чтобы отследить в базе данных юзера
def changeLogin(oldLogin: str, newLogin: str, cursor: sqlite3.Cursor) -> bool:
    try:
        connection = sqlite3.connect("users.db")
        existingLogin = """SELECT login FROM users WHERE login = ?"""
        cursor.execute(existingLogin, (newLogin,))
        if cursor.fetchone() is None:
            sqliteUpdateLogin = """UPDATE users SET login = ? WHERE login = ?"""
            dataTuple = (newLogin, oldLogin)
            cursor.execute(sqliteUpdateLogin, dataTuple)
            connection.commit
            cursor.close()
            return True
        else:
            print("Такой логин уже существует")
            return False
    except Exception as ex:
        return False


# Функция, которая меняет почту в бд. На вход подается старая почта и новая почта, старая почта - чтобы отследить в базе данных юзера.
def changeEmail(oldEmail: str, newEmail: str, cursor: sqlite3.Cursor) -> bool:
    try:
        connection = sqlite3.connect("users.db")
        sqliteUpdateEmail = """UPDATE users SET email = ? WHERE email = ?"""
        dataTuple = (newEmail, oldEmail)
        cursor.execute(sqliteUpdateEmail, dataTuple)
        connection.commit
        cursor.close()
        return True
    except Exception as ex:
        return False


# Далее идут три функции, которые изменяют заголовок, описание, дедлайн таска. Все на вход принимают заголовок таска для ориентирования в бд
def updateTitle(oldTitle: str, newTitle: str, cursor: sqlite3.Cursor) -> bool:
    try:
        connection = sqlite3.connect("project.db")
        sqliteUpdateTitle = """UPDATE task SET title = ? WHERE title = ?"""
        dataTuple = (newTitle, oldTitle)
        cursor.execute(sqliteUpdateTitle, dataTuple)
        connection.commit
        cursor.close()
        return True
    except Exception as ex:
        return False


def updateDescription(
    tasksTitle: str, newDescription: str, cursor: sqlite3.Cursor
) -> bool:
    try:
        connection = sqlite3.connect("project.db")
        sqliteUpdateDescription = """UPDATE task SET description = ? WHERE title = ?"""
        dataTuple = (newDescription, tasksTitle)
        cursor.execute(sqliteUpdateDescription, dataTuple)
        connection.commit
        cursor.close()
        return True
    except Exception as ex:
        return False


def updateDeadlineTask(
    tasksTitle: str, newDeadline: str, cursor: sqlite3.Cursor
) -> bool:
    try:
        connection = sqlite3.connect("project.db")
        sqliteUpdateDeadline = """UPDATE task SET deadline = ? WHERE title = ?"""
        dataTuple = (newDeadline, tasksTitle)
        cursor.execute(sqliteUpdateDeadline, dataTuple)
        connection.commit
        cursor.close()
        return True
    except Exception as ex:
        return False


# Далее идут 4 функции, которые обновляют: фото, имя, фамилию, телеграмм айди ползователя. Все на вход получают логин, чтобы ориентироваться в бд
def updatePhoto(login: str, newPhoto: bytes, cursor: sqlite3.Cursor) -> bool:
    try:
        connection = sqlite3.connect("users.db")
        sqliteUpdatePhoto = """UPDATE users SET photo = ? WHERE login = ?"""
        dataTuple = (newPhoto, login)
        cursor.execute(sqliteUpdatePhoto, dataTuple)
        connection.commit
        cursor.close()
        return True
    except Exception as ex:
        return False


def updateName(login: str, newName: str, cursor: sqlite3.Cursor) -> bool:
    try:
        connection = sqlite3.connect("users.db")
        sqliteUpdateName = """UPDATE users SET name = ? WHERE login = ?"""
        dataTuple = (newName, login)
        cursor.execute(sqliteUpdateName, dataTuple)
        connection.commit
        cursor.close()
        return True
    except Exception as ex:
        return False


def updateSurname(login: str, newSurname: str, cursor: sqlite3.Cursor) -> bool:
    try:
        connection = sqlite3.connect("users.db")
        sqliteUpdateSurname = """UPDATE users SET surname = ? WHERE login = ?"""
        dataTuple = (newSurname, login)
        cursor.execute(sqliteUpdateSurname, dataTuple)
        connection.commit
        cursor.close()
        return True
    except Exception as ex:
        return False


def updateTelegrammId(login: str, newId: str, cursor: sqlite3.Cursor) -> bool:
    try:
        connection = sqlite3.connect("users.db")
        sqliteUpdateTelegrammId = """UPDATE users SET telegrammID = ? WHERE login = ?"""
        dataTuple = (newId, login)
        cursor.execute(sqliteUpdateTelegrammId, dataTuple)
        connection.commit
        cursor.close()
        return True
    except Exception as ex:
        return False


def convert_to_binary_data(filename: str) -> bytes:
    with open(filename, "rb") as file:
        blob_data = file.read()
    return blob_data
