"""
1. Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield
2. * (вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield.
"""


def gen_odd_numbers(num):
    for i in range(num+1):
        if i % 2 == 1:
            yield i


position = 0
limit = 0


def func_odd_numbers(num=-1):
    global limit
    global position
    if num > 0 and limit == 0:
        limit = num + 1

    for i in range(position + 1, limit):
        if i % 2 == 1:
            position = i
            return i


print('\nfunction')
for i in range(8):
    print(func_odd_numbers(15))
print('\ngenerator')
odd_nums = gen_odd_numbers(15)
for i in range(8):
    print(next(odd_nums))
print('\ngenerator no yield')
for i in (i for i in range(15) if i%2 == 1):
    print(i)
