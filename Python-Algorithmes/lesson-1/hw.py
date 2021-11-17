from random import randint, uniform, choice


def tofixed(num, total):
    return ((num * (10**total))//1)/(10**total)


# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
def func1():
    print('Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.')
    inp = input()
    try:
        inp = int(inp)
    except ValueError:
        print('Введено не число')
        return
    numbers = []
    while inp > 0:
        numbers.append(inp % 10)
        inp = inp // 10
    sum = 0
    mul = 1
    for i in numbers:
        sum = sum + i
        mul = mul * i

    print(f'Сумма цифр: {sum}\nПроизведение цифр: {mul}')

    # sum = 0
    # mul = 1
    # for i in inp:
    #     i = int(i)
    #     sum = sum + i
    #     mul = mul * i
    # print(f'Сумма цифр: {sum}\nПроизведение цифр: {mul}')


# 2. Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
# Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака. Объяснить полученный результат.
def func2():
    print(bin(5))
    print(bin(6))
    print(bin(5) and bin(6))
    print(bin(5) or bin(6))


# 3. По введенным пользователем координатам двух точек вывести уравнение прямой вида y=kx+b, проходящей через эти точки.
def func3():
    x1, y1 = input('Введите координаты точки: "x y": ').split()
    try:
        x1, y1 = float(x1), float(y1)
    except ValueError:
        print('Введены невозможные координаты')
    x2, y2 = input('Введите координаты второй точки: "x y": ').split()
    try:
        x2, y2 = float(x2), float(y2)
    except ValueError:
        print('Введены невозможные координаты')

    if x1 > x2:
        x1, x2, y1, y2 = x2, x1, y2, y1
    k = tofixed((y2 - y1)/(x2 - x1), 2)
    b = tofixed(y1 - k * x1, 2)
    if b:
        if b > 0:
            print(f'y = {k}*x +{b}')
        else:
            print(f'y = {k}*x {b}')
    else:
        print(f'y = {k}*x')


# 4. Написать программу, которая генерирует в указанных пользователем границах:
# случайное целое число;
# случайное вещественное число;
# случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона. Например, если надо получить случайный символ
# от 'a' до 'f', то вводятся эти символы.
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
def func4():
    mode = 0
    try:
        a, b = input('Введите границы: ').split()
    except ValueError:
        print('Неверный интервал')
        return
    try:
        a, b = int(a), int(b)
    except ValueError:
        mode = 1
        try:
            a, b = float(a), float(b)
        except ValueError:
            mode = 2

    if mode == 0:
        print(randint(a, b))
    elif mode == 1:
        print(uniform(a, b))
    else:
        print(choice([chr(s) for s in range(ord(a), ord(b))]))


# 5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.
def func5():
    a, b = input('Введите две буквы: ').split()
    print(int(ord(b)) - int(ord(a)) + 1)


# 6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
def func6():
    a = int(input('Введите номер буквы: '))
    print(chr(int(ord('а')) + a - 1))


# 7. По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника, составленного
# из этих отрезков. Если такой треугольник существует, то определить, является ли он разносторонним, равнобедренным или
# равносторонним.
def func7():
    try:
        a, b, c = input('Введите стороны треугольника: ').split()
        a, b, c = int(a), int(b), int(c)
        if not(a > 0 and b > 0 and c > 0):
            raise(ValueError)
    except ValueError:
        print('Неверные данные')
        return

    if a > b and a > c:
        if b + c <= a:
            print('Такой треугольник невозможен')
            return
        else:
            print('Треугольник существует')
    elif b > c:
        if a + c <= b:
            print('Такой треугольник невозможен')
            return
        else:
            print('Треугольник существует')
    elif a + c <= b:
        print('Такой треугольник невозможен')
        return
    else:
        print('Треугольник существует')

    if a == b == c:
        print('Треугольник равносторонний')
    elif a == b or a == c or b == c:
        print('Треугольник равнобедренный')


# 8. Определить, является ли год, который ввел пользователем, високосным или невисокосным.
def func8():
    year = int(input('Введите год: '))
    if year % 4 == 0:
        print('Год високосный.')
    else:
        print('Год не високосный')


# 9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
def func9():
    try:
        a, b, c = input('Введите числа: ').split()
        a, b, c = int(a), int(b), int(c)
    except ValueError:
        print('Неверный ввод')
        return
    med = (a + b + c) / 3
    dif = abs(a - med)
    res = a
    if abs(b - med) < dif: res = b
    if abs(c - med) < dif: res = c
    print(res)
