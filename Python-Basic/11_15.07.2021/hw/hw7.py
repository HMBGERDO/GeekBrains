"""
7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число».
Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта.
Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""


class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        if self.imag == 0:
            return f'{self.real}'
        elif self.imag > 0:
            return f'{self.real}+{self.imag}i'
        else:
            return f'{self.real}{self.imag}i'

    def __add__(self, other):
        if other.__class__ == Complex:
            return Complex(self.real + other.real, self.imag + other.imag)
        elif other.__class__ == int:
            return Complex(self.real + other, self.imag)
        else:
            raise ValueError

    def __mul__(self, other):
        if other.__class__ == Complex:
            return Complex(self.real * other.real - self.imag * other.imag,
                           self.imag * other.real + self.real * other.imag)
        elif other.__class__ == int:
            return Complex(self.real * other, self.imag * other)
        else:
            raise ValueError


if __name__ == '__main__':
    print(Complex(1, 2) + Complex(-2, 4))
    print(Complex(4, 0) + 3)
    print(Complex(1, 2) * Complex(-2, 4))
    print(Complex(1, -2) * 2)
