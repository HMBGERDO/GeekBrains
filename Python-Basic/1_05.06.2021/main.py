'''
05.06.2021
-Запрос данных пользователя и хранение в переменных
-ФИО
-Возраст
'''

import datetime

today = datetime.datetime.now()

# названия переменных маленькими буквами без транслита
fio = input('Введите ФИО: ')
print('{} {}'.format(fio, type(fio)))
birthday = input('Введите дату рождения в формате ДД/ММ/ГГГГ: ')
birthday_day, birthday_month, birthday_year = birthday.split('/')
birthday_day, birthday_month, birthday_year = int(birthday_day), int(birthday_month), int(birthday_year)
print(birthday_day, birthday_month, birthday_year)
full_years = datetime.datetime.now().year - birthday_year
if today.month < birthday_month or today.month == birthday_month and today.day < birthday_day:
    full_years += -1
    if today.day == birthday_day:
        print('Happy birthday!')
print(full_years)
