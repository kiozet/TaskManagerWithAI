"""The authorization part of a program"""

import sqlite3


def getEmailAndPassword() -> tuple:
    """
    function that get email and password. than validate them
    returns (email, password) tuple
    """

    email = str(input())
    password = str(input())

    if email.count("@") == 1 and email.count(".") == 1 and password != "":
        return (email, password)

    else:
        raise "Bad email or epmpty password"


def checkEmailAndPassword(cursor) -> bool:
    """
    func that check email and password in db
    return True or False depends on check
    """

    email, password = getEmailAndPassword()

    try:
        cursor.execute("SELECT password FROM users where email = ?", (email,))
        data = cursor.fetchall()[0][0]

        if data == password:
            return True

        else:
            return False

    except Exception as ex:
        print("email doesn't exist")


def main():
    """
    This is main function of program that
    Connect with db and create cursor
    """

    db = "Project.db"
    connection = sqlite3.connect(db)
    cursor = connection.cursor()

    checkEmailAndPassword(cursor)


if __name__ == "__main__":
    main()
