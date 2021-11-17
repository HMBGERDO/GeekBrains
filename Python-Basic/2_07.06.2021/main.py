name = 'Basil'
age = 35
education = ['school number 2', 'MSU']

print(dir(education))  # просмотреть все методы
education.append('HSE')

# функция - существует сама по себе. Метод - привязан к классу. Оба могут принимать на вход аргументы
print(education)

education_copy = education.copy()  # присвоение новой переменной списка не копирует список, тот же объект
# копировать список нужно как указано выше, либо copy.deepcopy(array)
education.clear()
print(education)
print(education_copy)

education.extend(['test1', 'test2', 'test3'])
print(education)

print(education_copy.count('MSU'))  # количетсво элементов в массиве
print(education_copy.index('HSE'))  # позиция первого найденного элемента

education_copy.insert(2, 'Army')  # добавляет элемент на нужную позицию
print(education_copy)

education_copy.remove('MSU')  # удаляет первый найденный элементс указанным значением
print(education_copy)

education_copy.reverse()  # переворачивает список
print(education_copy)

education_copy.sort()  # сортирует изначально по алфавиту, можно задать свой ключ

additional_courses = ['GeekBrains', 'College']
print(education_copy + additional_courses)
print([1, 2, 3, 4] + [5, 6, 7, 8])

education_copy += additional_courses  # сложение массивов с изменением переменной
# education_copy = education_copy + additional_courses
print(education_copy)

print(len(education_copy))  # количетсво элементов

print([1, 2, 3, 4] > [2, 1, 1, 1, 1, 1])  # изначально поэлементная проверка

crazy_list = ['Hello', 'Dolly!', 42, 'Привет', [10, ['Hi!', 'Bye!']], 12.5]
print(crazy_list[4][1][1])

print(crazy_list[1:3])  #start:end:step
print(crazy_list[1:4:2])

sorted_crazy_list = sorted(education_copy, reverse=True)
print(sorted_crazy_list)

print(*sorted_crazy_list)
str()

tuple_fio = ('Basil', 'Ivanov')
tuple_vaccine = ('CoviVac', 'Influenza')
print(type(tuple_vaccine))
print(dir(tuple_vaccine))
print(tuple_fio + tuple_vaccine)

crazy_tuple = ('Basil', 'Ivanov', ['MSU', 'HSE'])
crazy_tuple[2].append('Army')
print(crazy_tuple)

