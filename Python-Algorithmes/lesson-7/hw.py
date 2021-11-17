from random import randint
from time import time
test_array = []
for i in range(15):
    test_array.append(randint(0, 200) - 100)


# 1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
# Сортировка должна быть реализована в виде функции. По возможности доработайте алгоритм (сделайте его умнее).
def sort_bubble(array):
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] < array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array


# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
def sort_merge(array):
    if len(array) == 0 or len(array) == 1:
        return array
    left_part, right_part = sort_merge(array[:len(array)//2]), sort_merge(array[len(array)//2:])
    left_i, right_i = 0, 0
    result = []
    while left_i < len(left_part) and right_i < len(right_part):
        if left_part[left_i] < right_part[right_i]:
            result.append(left_part[left_i])
            left_i += 1
        else:
            result.append(right_part[right_i])
            right_i += 1
    while left_i < len(left_part):
        result.append(left_part[left_i])
        left_i += 1
    while right_i < len(right_part):
        result.append(right_part[right_i])
        right_i += 1
    return result


def test(mode=False):
    array = test_array.copy()
    if mode:
        print(array)
    print('sort_bubble')
    time_start = time()
    result = sort_bubble(array)
    if mode:
        print(result)
    print(time() - time_start)
    print()
    array = test_array.copy()
    if mode:
        print(array)
    print('sort_merge')
    time_start = time()
    result = sort_merge(array)
    if mode:
        print(result)
    print(time() - time_start)
    print()
    array = test_array.copy()
    if mode:
        print(array)
    print('sorted python')
    time_start = time()
    result = sorted(array)
    if mode:
        print(result)
    print(time() - time_start)
    print()


# 3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы,
# которые не меньше медианы, в другой – не больше медианы. Задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, то используйте метод сортировки, который не рассматривался на уроках
def average(array):
    avg = 0
    for i in array:
        avg += i
    avg = avg / len(array)
    less = []
    more = []
    for i in array:
        if i == avg:
            continue
        if i < avg:
            less.append(i)
        if i > avg:
            more.append(i)
    if len(less) + len(more) < len(array):
        print(avg)
        return avg
    if len(less) > len(more):
        less = sorted(less)
        print(less[len(array) // 2])
        return less[len(array) // 2]
    else:
        more = sorted(more)
        print(more[len(more) - len(array) // 2 - 1])
        return more[len(more) - len(array) // 2 - 1]
