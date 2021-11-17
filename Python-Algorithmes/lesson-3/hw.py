# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
def func1():
    result = []
    for i in range(2, 10):
        result.append((i, 99 // i))
    for i in result:
        print(f'Кратных {i[0]} : {i[1]}')


# 2. Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив надо заполнить значениями
# 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля), т.к. именно в этих позициях
# первого массива стоят четные числа.
def func2(array):
    result = []
    for i in array:
        if i % 2 == 1:
            result.append(i)
    return result


# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
def func3(array):
    elmax = 0
    elmin = 0
    for i, el in enumerate(array):
        if el > array[elmax]:
            elmax = i
        if el < array[elmin]:
            elmin = i
    array[elmax], array[elmin] = array[elmin], array[elmax]
    return array


# 4. Определить, какое число в массиве встречается чаще всего.
def func4(array):
    count = {}
    max = None
    for i in array:
        i = str(i)
        if i not in count:
            count[i] = 1
        else:
            count[i] += 1
        if not max or max and count[i] > count[max]:
            max = i
    return int(max)


# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
def func5(array):
    minel = 0
    for i, el in enumerate(array):
        if array[minel] > el and el < 0:
            minel = i
    print(f'Минимальный элемент: {array[minel]} на позиции {minel}')


# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.
def func6(array):
    elmax = 0
    elmin = 0
    for i, el in enumerate(array):
        if el > array[elmax]:
            elmax = i
        if el < array[elmin]:
            elmin = i
    return abs(elmax - elmin - 1)


# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.
def func7(array):
    least1 = None
    least2 = None
    for i in array:
        if not least1:
            least1 = i
            continue
        if i < least1:
            least2 = least1
            least1 = i
        if not least2:
            least2 = i
            continue
        elif i < least2:
            least2 = i
    return least1, least2


# 8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.
def func8():
    matrix = []
    for i in range(0, 4):
        matrix.append([])
        inp = input(f'Введите {i + 1} строку матрицы через пробел: ')
        sum = 0
        for j, el in enumerate(inp.split(' ')):
            matrix[i].append(el)
            el = int(el)
            sum += el
        matrix[i].append(str(sum))
        # print(' - '.join([' '.join(matrix[i][0:5]), matrix[i][5]]))

    print('\n'.join([' : '.join(['|'.join(i[0:5]), i[5]]) for i in matrix]))


# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
def func9(matrix):
    maxelement = None
    for j in range(len(matrix[0])):
        min = None
        for i in range(len(matrix)):
            if min is None or matrix[i][j] < min:
                min = matrix[i][j]
        if maxelement is None or min > maxelement:
            maxelement = min
    return maxelement
