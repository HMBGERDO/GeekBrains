from abc import ABC, abstractmethod


class Test:
    def __init__(self):
        self._b = '2'

    @property
    def a(self):
        return self._b

    @a.getter
    def a(self):
        return self._b

    @a.setter
    def a(self, val):
        self._b += val

    @a.deleter
    def a(self):
        self._b = 0


test = Test()
print(test.a)
test.a = '123'
print(test.a)
