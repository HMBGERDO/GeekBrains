"""3. Написать декоратор для логирования типов позиционных аргументов функции, например:
def type_logger...
    ...


@type_logger
def calc_cube(x):
   return x ** 3

a = calc_cube(5)
5: <class 'int'>
Примечание: если аргументов несколько - выводить данные о каждом через запятую; можете ли вы вывести тип значения
функции? Сможете ли решить задачу для именованных аргументов? Сможете ли вы замаскировать работу декоратора? Сможете
ли вывести имя функции, например, в виде:
a = calc_cube(5)
calc_cube(5: <class 'int'>)"""


def wrapper(func):
    def arg_info(*args, **kwargs):
        for arg in args:
            print(f'{func.__name__}({arg} : {type(arg)})')
        for kwarg in kwargs:
            print(f'{func.__name__}({kwarg} : {type(kwarg)})')
        func(*args, **kwargs)
    return arg_info


@wrapper
def print_arg(arg):
    print(arg)


print_arg(5)
