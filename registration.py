"""The authorization part of a program"""

import sqlite3


def createTable(connection: sqlite3.Connection, cursor: sqlite3.Cursor):
    """Create table func, args: connection: sqlite3.Connection, cursor: sqlite3.Cursor from your
    sqlite3 db"""

    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS Users (
    email TEXT NOT NULL,
    password TEXT NOT NULL
    )
    """
    )

    connection.commit()


def emailValidation(email: str) -> bool:
    if email.count("@") == 1 and email.count(".") == 1:  # write with fnmatch
        return True

    else:
        return False


def registrationUser(connection: sqlite3.Connection, cursor: sqlite3.Cursor) -> bool:
    """User registration function by validate it and insert it into table.
    args: connection: sqlite3.Connection, cursor: sqlite3.Cursor from your sqlite3 db
    """

    # input email and password, waiting to frontend be done
    email = str(input())
    password = str(input())

    if emailValidation(email) == True and password != "":
        cursor.execute(
            "INSERT INTO Users (email, password) VALUES (?, ?)",
            (
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

    db = "authorization_test.db"
    connection = sqlite3.connect(db)
    cursor = connection.cursor()

    createTable(connection, cursor)
    registrationUser(connection, cursor)


if __name__ == "__main__":
    main()
