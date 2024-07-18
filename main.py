import sys
from time import time

import db_utils
import employee
import generator_employees


"""Основной модуль, который запускает приложение и вызывает функции из других модулей."""


if __name__ == '__main__':
    if sys.argv[1] == '1':
        db_utils.create_table()
        print("Таблица успешно создана.")
    elif sys.argv[1] == '2':
        full_name = sys.argv[2]
        date_of_birth = sys.argv[3]
        gender = sys.argv[4]
        employee = employee.Employee(full_name, date_of_birth, gender)
        employee.create_and_save_employee(employee)
        print(f'Сотрудник {full_name} добавлен в базу данных.')
    elif sys.argv[1] == '3':
        employee.Employee.get_all_employees()
    elif sys.argv[1] == '4':
        result = generator_employees.generate_employees(1, f_surname=True)
        employee.Employee.save_batch_employees(result)
    elif sys.argv[1] == '5':
        start_time = time()
        employees = employee.Employee.get_employees_by_gender_and_surname('Male', 'F')
        end_time = time()
        print(f"Время до оптимизации: {end_time - start_time:.2f} секунд")
    elif sys.argv[1] == '6':
        db_utils.optimize_database()
        start_time = time()
        employees = employee.Employee.get_employees_by_gender_and_surname('Male', 'F')
        end_time = time()
        print(f"Время после оптимизации: {end_time - start_time:.2f} секунд")



