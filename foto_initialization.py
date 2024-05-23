import sqlite3


def convert_to_binary_data(filename):
    with open(filename, "rb") as file:
        blob_data = file.read()
    return blob_data


def insert_blob(emp_id, name, photo, resume_file):
    try:
        sqlite_connection = sqlite3.connect("sqlite_python.db")
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        sqlite_insert_blob_query = """INSERT INTO new_employee
                                  (id, name, photo, resume) VALUES (?, ?, ?, ?)"""

        emp_photo = convert_to_binary_data(photo)
        resume = convert_to_binary_data(resume_file)
        # Преобразование данных в формат кортежа
        data_tuple = (emp_id, name, emp_photo, resume)
        cursor.execute(sqlite_insert_blob_query, data_tuple)
        sqlite_connection.commit()
        print("Изображение и файл успешно вставлены как BLOB в таблиу")
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")
