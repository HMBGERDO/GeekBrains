"""
4. Реализуйте базовый класс Car.
у класса должны быть следующие атрибуты: speed, color, name, is_police(булево). А также методы: go, stop,
turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Вызовите
методы и покажите результат.
"""


class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self, speed):
        self.speed = speed
        print(f'{self.color} {self.name} начала движение.')
        self.show_speed()

    def stop(self):
        self.speed = 0
        print(f'{self.color} {self.name} остановилась.')
        self.show_speed()

    def turn(self, direction):
        print(f'{self.color} {self.name} повернула {direction}.')
        self.show_speed()

    def show_speed(self):
        print(f'Скорость {self.color} {self.name} : {self.speed}км/ч .')


class TownCar(Car):
    def show_speed(self):
        print(f'Скорость {self.color} {self.name} : {self.speed}км/ч .')
        if self.speed > 60:
            print('Зафиксировано превышение скорости!')
        print()


class WorkCar(Car):
    def show_speed(self):
        print(f'Скорость {self.color} {self.name} : {self.speed}км/ч .')
        if self.speed > 40:
            print('Зафиксировано превышение скорости!')
        print()


if __name__ == '__main__':
    simple_town_car = TownCar(0, 'Red', 'Ford')
    simple_town_car.go(75)
    simple_town_car.turn('Left')
    simple_town_car.go(45)
    simple_town_car.stop()

    simple_work_car = WorkCar(0, 'White', 'Track')
    simple_work_car.go(35)
    simple_work_car.go(55)
    simple_work_car.turn('Right')
    simple_work_car.stop()
