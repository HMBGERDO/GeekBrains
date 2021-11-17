"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
| 31 22 |
| 37 43 |
| 51 86 |

| 3 5 32 |
| 2 4 6 |
| -1 64 -8 |

| 3 5 8 3 |
| 8 3 7 1 |
"""


class Matrix:
    def __init__(self, structure):
        self._structure = structure

    def __str__(self):
        return '\n'.join('| ' + ' '.join(str(j) for j in i) + ' |' for i in self._structure)

    def __add__(self, other):
        new_structure = []
        for i in range(len(self._structure)):
            new_structure.append([])
            for j in range(len(self._structure[0])):
                new_structure[i].append(self._structure[i][j] + other._structure[i][j])
        return Matrix(new_structure)


if __name__ == '__main__':
    testmat = Matrix([[1, 2, 3], [4, 5, 6]])
    print(testmat)
    print(testmat + Matrix([[2, 2, 2], [2, 2, 2]]))
