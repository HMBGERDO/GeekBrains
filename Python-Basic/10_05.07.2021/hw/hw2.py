"""
Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта —
одежда, которая может иметь определённое название. К типам одежды в этом проекте относятся пальто и костюм. У этих типов
одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H
соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Выполнить общий подсчёт расхода ткани. Проверить на практике полученные на этом уроке знания. Реализовать абстрактные
классы для основных классов проекта и проверить работу декоратора @property.
"""
from abc import ABC, abstractmethod


class Clothes:
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_cloth_rate(self):
        pass


class Coat(Clothes):
    def __init__(self, name, area):
        super().__init__(name)
        self.area = area

    @property
    def get_cloth_rate(self):
        return self.area*2 + 0.3


class Suit(Clothes):
    def __init__(self, name, length):
        super().__init__(name)
        self.length = length

    @property
    def get_cloth_rate(self):
        return self.length/6.5 + 0.5


test = Coat('A', 15)
print(test.name)
print(test.get_cloth_rate)
