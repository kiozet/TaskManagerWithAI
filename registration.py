'''The authorization part of a program'''
import sqlite3


def createTable(cursor: sqlite3.Cursor):
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
    email TEXT NOT NULL,
    password TEXT NOT NULL
    )
    ''')


def registrationUser(cursor: sqlite3.Cursor):
    
def main():
    '''
    This is main function of program:
    connect with db
    '''  
    
    db = "authorization_test.db"
    connection = sqlite3.connect(db)
    cursor = connection.cursor()
    
    createTable(cursor)    


if __name__ == "__main__":
    main()