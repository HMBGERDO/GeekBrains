'''
1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
до минуты: <s> сек;
* до часа: <m> мин <s> сек;
* до суток: <h> час <m> мин <s> сек;
* *до месяца, до года, больше года: по аналогии.
'''

# порядок важен, если что добавлять, то чем больше промежуток, тем выше
durations = [
    {
        'dur': 60 * 60 * 24 * 365,
        'printname': 'год',
    },
    {
        'dur': 60 * 60 * 24 * 30,
        'printname': 'мес',
    },
    {
        'dur': 60 * 60 * 24,
        'printname': 'день',
    },
    {
        'dur': 60 * 60,
        'printname': 'час',
    },
    {
        'dur': 60,
        'printname': 'мин',
    },
    {
        'dur': 1,
        'printname': 'сек',
    },
]


def print_duration(duration):
    try:
        int(duration)
    except:
        print('Неверный ввод\n')
        return False
    duration = int(duration)
    duration_list = []
    current_duration = duration
    duration_string = ''
    for i, v in enumerate(durations):
        duration_list.append({
            'printname': durations[i]['printname'],
            'value': current_duration // durations[i]['dur'],
        })
        if current_duration // durations[i]['dur'] > 0:
            duration_string = duration_string + '{} {} '.format((current_duration // durations[i]['dur']),
                                                                (durations[i]['printname']))
        current_duration = current_duration - duration_list[i]['value'] * durations[i]['dur']
    print(duration_string)
    return duration_list


while(True):
    print_duration(input('duration = '))