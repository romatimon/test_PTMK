import sqlite3

"""Модуль, содержащий функции для работы с базой данных (подключение, создание таблицы, и т.д.)."""


def create_table():
    conn = sqlite3.connect("employees.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS employees
                (full_name TEXT, date_of_birth TEXT, gender TEXT)''')


def get_connection_table():
    return sqlite3.connect("employees.db")


def optimize_database():
    with get_connection_table() as conn:
        cursor = conn.cursor()
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_gender_surname ON employees (gender, full_name)")
        conn.commit()