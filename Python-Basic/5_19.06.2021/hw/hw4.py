"""
4. Представлен список чисел. Необходимо вывести те его элементы, значения которых больше предыдущего, например:
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [12, 44, 4, 10, 78, 123]
```

Подсказка: использовать возможности python, изученные на уроке.
"""

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]


def bigger_numbers(arr):
    result = []
    num = arr[0]
    for i in range(1, len(arr)-1):
        if arr[i] > num:
            result.append(arr[i])
        num = arr[i]
    return result


print(bigger_numbers(src))
print([src[i] for i in range(1, len(src)-1) if src[i] > src[i-1]])
