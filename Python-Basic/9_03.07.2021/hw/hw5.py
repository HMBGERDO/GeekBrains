"""
5. Реализовать класс Stationery (канцелярская принадлежность).
определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationary:
    title = ''

    def draw(self):
        print('Start drawing!')


class Pen(Stationary):
    title = 'Ручка'

    def draw(self):
        print(f'Начинаем рисовать инструментом {self.title}')


class Pencil(Stationary):
    title = 'Карандаш'

    def draw(self):
        print(f'Начинаем рисовать инструментом {self.title}')


class Handle(Stationary):
    title = 'Маркер'

    def draw(self):
        print(f'Начинаем рисовать инструментом {self.title}')


if __name__ == '__main__':
    pencil = Pencil()
    pencil.draw()

    pen = Pen()
    pen.draw()

    handle = Handle()
    handle.draw()
