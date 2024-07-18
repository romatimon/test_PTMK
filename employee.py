from datetime import datetime
import db_utils


"""Модуль содержит определение класса Employee и связанные с ним методы."""

class Employee:
    def __init__(self, full_name, date_of_birth, gender):
        self.full_name = full_name
        self.date_of_birth = date_of_birth
        self.gender = gender

    @classmethod
    def calculate_age(cls, date_of_birth):
        today = datetime.now()
        birth_date = datetime.strptime(date_of_birth, "%Y-%m-%d")
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        return age

    @classmethod
    def create_and_save_employee(cls, employee):
        with db_utils.get_connection_table() as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO employees VALUES (?, ?, ?)',
                           (employee.full_name, employee.date_of_birth, employee.gender))
            conn.commit()

    @classmethod
    def get_all_employees(cls):
        with db_utils.get_connection_table() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM employees ORDER BY full_name')
            employees = cursor.fetchall()

        for employee in employees:
            full_name, date_of_birth, gender = employee
            age = cls.calculate_age(date_of_birth)
            print(f"ФИО: {full_name}, Дата рождения: {date_of_birth}, Пол: {gender}, Возраст: {age}")

    @classmethod
    def save_batch_employees(cls, employees):
        with db_utils.get_connection_table() as conn:
            cursor = conn.cursor()
            for employee in employees:
                cursor.execute('INSERT INTO employees (full_name, date_of_birth, gender) VALUES (?, ?, ?)',
                               (employee.full_name, employee.date_of_birth, employee.gender))
            conn.commit()

    @classmethod
    def get_employees_by_gender_and_surname(cls, gender, surname_starts_with):
        with db_utils.get_connection_table() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM employees WHERE gender = ? AND full_name LIKE ?',
                           (gender, f"{surname_starts_with}%"))
            employees = cursor.fetchall()
            for employee in employees:
                full_name, date_of_birth, gender = employee
                age = cls.calculate_age(date_of_birth)
                print(f"ФИО: {full_name}, Дата рождения: {date_of_birth}, Пол: {gender}, Возраст: {age}")

    def __repr__(self):
        return f'{self.full_name, self.date_of_birth, self.gender}'
