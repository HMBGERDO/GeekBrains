# 1. Подсчитать, сколько было выделено памяти под переменные в ранее
# разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной и той же задачи.
# Результаты анализа вставьте в виде комментариев к коду.
# Также укажите в комментариях версию Python и разрядность вашей ОС.
# ОС - Windows 10
# Разрядность - 64 бита

import sys


def func1():
    modes = ('0', '+', '-', '*', '/')
    while True:
        num1 = int(input('Введите первое число: '))
        mode = input('Введите действие: ')
        while True:
            if mode not in modes:
                mode = input('Введен неверный знак. Введите действие: ')
            else:
                break
        if mode == '0':
            break
        num2 = int(input('Введите второе число: '))
        if mode == '/' and num2 == 0:
            print('Нельзя делить на ноль.')
            continue
        result = None
        if mode == '+':
            result = num1 + num2
        elif mode == '-':
            result = num1 - num2
        elif mode == '*':
            result = num1 * num2
        elif mode == '/':
            result = num1 / num2
        print(f'{num1} {mode} {num2} = {result}')
        print(sys.getrefcount(mode))


func1()
