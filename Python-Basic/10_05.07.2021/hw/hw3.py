"""
Осуществить программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс «Клетка».
В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число). В классе должны
быть реализованы методы перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()),
умножение (__mul__()), деление (__floordiv____truediv__()).
Эти методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и округление до целого
числа деления клеток соответственно.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять, только если разность количества ячеек двух клеток больше
нуля, иначе выводить соответствующее сообщение.
Умножение. Создаётся общая клетка из двух. Число ячеек общей клетки — произведение количества ячеек этих двух клеток.
Деление. Создаётся общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества
ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. Этот метод
позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, а количество ячеек в ряду — 5.
В этом случае метод make_order() вернёт строку: *****\n*****\n**.
Или количество ячеек клетки — 15, а количество ячеек в ряду равняется 5.
Тогда метод make_order() вернёт строку: *****\n*****\n*****.
"""


class Cell:
    def __init__(self, num):
        self.count = num

    def __add__(self, other):
        self.count = self.count + other.count

    def __sub__(self, other):
        if self.count - other.count > 0:
            self.count = self.count - other.count
        else:
            print('Невозможное вычитание')

    def __mul__(self, other):
        return Cell(self.count * other.count)

    def __floordiv__(self, other):
        return Cell(int(self.count//other.count))

    def make_order(self, num):
        result = ['*' * num for i in range(0, self.count // num)]
        result.append('*' * (self.count % num))
        return '\n'.join(result)


if __name__ == '__main__':
    test = Cell(32)
    test + Cell(2)
    test = test * Cell(3)
    print(test.make_order(30))
    print(test.make_order(128))