import sqlite3


class CyrillicError(Exception):
    pass


class SpaceButtonError(Exception):
    pass


class LoginError(Exception):
    pass


class SpecialSymbolsError(Exception):
    pass


def password_check(password):
    for i in password:
        if i in "абвгдеёжзийклмнопрстуфхцчшщьыъэюя":
            raise CyrillicError
        elif i in "!@#$%&?*~<>,'":
            raise SpecialSymbolsError
    return True


def login_check(login):
    for i in login:
        if i in "абвгдеёжзийклмнопрстуфхцчшщьыъэюя":
            raise CyrillicError
        elif i == " ":
            raise SpaceButtonError
    return True


with sqlite3.connect("Project.db") as db:
    cur = db.cursor()

    cur.execute(
        """CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        login TEXT NOT NULL CHECK(login_check(login)),
        password TEXT NOT NULL CHECK(password_check(password)),
        name TEXT NOT NULL,
        number_of_friends TEXT DEFAULT 0
        )"""
    )
    cur.execute(
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
