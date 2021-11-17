"""
4. Написать декоратор с аргументом-функцией (callback), позволяющий валидировать входные значения функции и выбрасывать
исключение ValueError, если что-то не так, например:
def val_checker...
    ...


@val_checker(lambda x: x > 0)
def calc_cube(x):
   return x ** 3


a = calc_cube(5)
125
a = calc_cube(-5)
Traceback (most recent call last):
  ...
    raise ValueError(msg)
ValueError: wrong val -5
Примечание: сможете ли вы замаскировать работу декоратора?
"""


def cond_checker(condition):
    def _cond_checker(func):
        def wrapper(*args):
            for arg in args:
                if not(condition(arg)):
                    raise ValueError(f'wrong value {arg}')
            return func(*args)
        return wrapper
    return _cond_checker


@cond_checker(lambda x: x > 0)
def cube_val(arg):
    return arg**3


print(cube_val(5))
print(cube_val(-5))
