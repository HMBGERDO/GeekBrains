"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определите параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры,
уникальные для каждого типа оргтехники.
5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники на склад и передачу
в определённое подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других
данных, можно использовать любую подходящую структуру (например, словарь).
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например,
для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
"""


def is_valid_objects(objects):
    for object in objects:
        object_class = object.__class__
        if not(object_class == Printer or object_class == Copier or object_class == Scanner):
            return False
    return True


class InvalidObjects(Exception):
    def __init__(self):
        self.txt = f'Wrong position!'
        super().__init__(self.txt)


class WrongPosition(Exception):
    def __init__(self):
        self.txt = f'Invalid objects!'
        super().__init__(self.txt)


class Storage:
    def __init__(self, name, objects=None):
        self.name = name
        if objects is None:
            objects = []
        if not(is_valid_objects(objects)):
            raise InvalidObjects()

        self.objects = objects

    def __str__(self):
        result = [f'{self.name}:']
        for i, object in enumerate(self.objects):
            result.append(f'{i + 1}: {object.name} на позиции {object.position}')
        result.append('\n')
        return '\n'.join(result)

    def add(self, objects):
        if objects is None:
            objects = []
        if not(is_valid_objects(objects)):
            raise InvalidObjects()
        for object in objects:
            self.objects.append(object)

    def transport(self, other, keys):
        keys = sorted(keys)
        for key in keys:
            other.objects.append(self.objects[key-1])
        for key in keys[::-1]:
            self.objects.remove(self.objects[key-1])


class Object:
    def __init__(self, name='Object', position=0):
        self.name = name
        self.position = int(position)

    def __mul__(self, other):
        result = []
        for i in range(other):
            result.append(self.__class__(self.position))
        return result


class Printer(Object):
    def __init__(self, position=0):
        super().__init__('Printer', position)


class Scanner(Object):
    def __init__(self, position=0):
        super().__init__('Scanner', position)


class Copier(Object):
    def __init__(self, position=0):
        super().__init__('Copier', position)


if __name__ == '__main__':
    shop = Storage('Магазин', [Printer(1), Printer(1), Copier(2)])
    another_shop = Storage('Склад')
    print(shop, another_shop)
    shop.transport(another_shop, [1, 2])
    print(shop, another_shop)
    shop.add([Printer(2), Scanner(3), Scanner(2)])
    print(shop, another_shop)
    # shop.add(['toy'])
