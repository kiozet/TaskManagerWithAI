"""The registration part of a program"""

import sqlite3


def createTable(connection: sqlite3.Connection, cursor: sqlite3.Cursor) -> bool:
    try:
        """Create table func, args: connection: sqlite3.Connection, cursor: sqlite3.Cursor from your
        sqlite3 db"""

        cursor.execute(
            """CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT NOT NULL,
        login TEXT NOT NULL,
        password TEXT NOT NULL,
        name TEXT NOT NULL,
        allTasks INTEGER DEFAULT 0,
        doneTasks INTEGER DEFAULT 0,
        frozenTasks INTEGER DEFAULT 0
        )"""
        )
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS Tasks(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                title TEXT,
                description TEXT,
                status TEXT,
                date_created TEXT,
                deadLine TEXT,
                FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
                )"""
        )

        connection.commit()

        return True

    except Exception as ex:
        return False


def emailValidation(email: str) -> bool:
    """Base emai validation func, returns True if all is ok
    args: email: str"""

    if email.count("@") == 1 and email.count(".") == 1:  # write with fnmatch
        return True

    else:
        return False


def loginExistance(login, cursor: sqlite3.Cursor):
    info = cursor.execute("SELECT EXISTS(SELECT 1 FROM users WHERE login = '{login}')")


def registrationUser(connection: sqlite3.Connection, cursor: sqlite3.Cursor) -> bool:
    """User registration function by validate it and insert it into table.
    args: connection: sqlite3.Connection, cursor: sqlite3.Cursor from your sqlite3 db
    """

    # input email and password, waiting to frontend be done
    login = str(input())
    email = str(input())
    password = str(input())

    if (
        emailValidation(email) == True
        and password != ""
        and loginExistance(login) == False
    ):
        cursor.execute(
            "INSERT INTO Users (login, email, password) VALUES (?, ?, ?)",
            (
                login,
                email,
                password,
            ),
        )
        connection.commit()

        return True

    else:
        print("bad email or password = ''")
        return False


def main():
    """
    This is the main function of program
    """

    db = "Project.db"
    connection = sqlite3.connect(db)
    cursor = connection.cursor()

    createTable(connection, cursor)
    registrationUser(connection, cursor)


if __name__ == "__main__":
    main()
