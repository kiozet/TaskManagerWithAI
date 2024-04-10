'''The authorization part of a program'''
import sqlite3


def main():
    '''
    This is main function of program
    '''  

    '''Connect with db and create cursor'''
    db = "authorization_test.db"
    connection = sqlite3.connect(db)
    cursor = connection.cursor()
    


if __name__ == "__main__":
    main()