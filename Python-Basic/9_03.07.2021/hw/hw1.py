"""
1. Создать класс TrafficLight (светофор).
определить у него один атрибут color (цвет) и метод running (запуск);
атрибут реализовать как приватный;
в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный) —
на ваше усмотрение;
переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении выводить соответствующее сообщение и
завершать скрипт.
"""
import time


class TrafficLight:
    __colortab = [
        {
            'color': 'Red',
            'time': 7,
        },
        {
            'color': 'Yellow',
            'time': 2,
        },
        {
            'color': 'Green',
            'time': 7,
        },
    ]
    __color = __colortab[0]

    def running(self):
        while True:
            for tab in self.__colortab:
                self.__color = tab['color']
                print(f'Trafficlight lights {self.__color}')
                time.sleep(tab['time'])
            for tab in self.__colortab[-2:0:-1]:
                self.__color = tab['color']
                print(f'Trafficlight lights {self.__color}')
                time.sleep(tab['time'])


if __name__ == '__main__':
    sometrafficlight = TrafficLight()
    sometrafficlight.running()
