import random
from datetime import date, timedelta, time
from employee import Employee

"""Модуль, содержащий функции для генерации случайных данных (имена, даты рождения, пол)."""


def generate_random_name():
    first_names = ['Alexander', 'Dmitry', 'Anna', 'Sergey', 'Ekaterina', 'Andrew', 'Olga']

    second_names = ['Sidorov', 'Kuznetsov', 'Smirnov', 'Popov', 'Sokolov', 'Lebedev', 'Kozlov',
                    'Novikov', 'Petrov', 'Ivanov', 'Volkov', 'Sorokin', 'Morozov', 'Makarov', 'Fedorov']

    surnames = ['Ivanovich', 'Petrovna', 'Sergeevich', 'Alekseevna', 'Dmitrievich', 'Mikhailovna', 'Andreevich',
                'Viktorovna', 'Nikolaevich', 'Alexandrovna']

    first_name = random.choice(first_names)
    last_name = random.choice(second_names)
    middle_name = random.choice(surnames)

    return f"{last_name} {first_name} {middle_name}"


def generate_random_date_of_birth():
    start_date = date(1960, 1, 1)
    end_date = date(2006, 12, 31)
    # Вычисляем количество дней между начальной и конечной датами
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    # Генерируем случайное количество дней в диапазоне
    random_number_of_days = random.uniform(0, days_between_dates)
    # Вычисляем случайную дату рождения, прибавляя случайное количество дней к начальной дате
    random_date = start_date + timedelta(days=random_number_of_days)
    return random_date.strftime("%Y-%m-%d")


def generate_random_gender():
    return random.choice(['Male', 'Female'])


def generate_employees(count, f_surname=False):
    employees = []
    for _ in range(count):
        full_name = generate_random_name()
        date_of_birth = generate_random_date_of_birth()
        gender = generate_random_gender()
        employees.append(Employee(full_name, date_of_birth, gender))

    if f_surname:
        for _ in range(100):
            full_name = f"F... {generate_random_name().split()[1]} {generate_random_name().split()[2]}"
            date_of_birth = generate_random_date_of_birth()
            gender = 'Male'
            employee = Employee(full_name, date_of_birth, gender)
            employees.append(employee)

    return employees


