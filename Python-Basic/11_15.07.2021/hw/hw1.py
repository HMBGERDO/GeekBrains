"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и
года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""


class Date:
    @classmethod
    def convert(cls, date):
        day, month, year = date.split('-')
        return int(day), int(month), int(year)

    @staticmethod
    def is_valid(date):
        day, month, year = Date.convert(date)
        if day < 0 or day > 31 or month < 0 or month > 12 or year < 0:
            return False
        return True


if __name__ == '__main__':
    print(Date.convert('21-05-2021'))
    print(Date.is_valid('2-2-2'))
