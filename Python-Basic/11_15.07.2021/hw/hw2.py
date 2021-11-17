"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
Проверьте его работу на данных, вводимых пользователем. При вводе нуля в качестве делителя программа должна корректно
обработать эту ситуацию и не завершиться с ошибкой.
"""


class SimpleZeroDivision(Exception):
    def __init__(self, num1):
        self.txt = num1


try:
    num = 5
    inp = int(input())
    if inp == 0:
        raise SimpleZeroDivision(num)
    print(num / inp)

except SimpleZeroDivision as result:
    print(result)
