"""
1. Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt
(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) — получить список
кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:

[
...
('141.138.90.60', 'GET', '/downloads/product_2'),
('141.138.90.60', 'GET', '/downloads/product_2'),
('173.255.199.22', 'GET', '/downloads/product_2'),
...
]

Примечание: код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.

2. * (вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из
предыдущего задания.
Примечания: спамер — это клиент, отправивший больше всех запросов; код должен работать даже с файлами, размер которых
превышает объем ОЗУ компьютера.
"""


def my_parsing(string):
    arr = string.split(' ')
    return (arr[0], arr[5][1:], arr[6])


log = {}

with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    for line in f:
        info = my_parsing(line)
        if not (log.get(info[0])):
            log[info[0]] = [(info[1], info[2])]
        else:
            log[info[0]].append((info[1], info[2]))

log = sorted(log, key=lambda x: len(x), reverse=True)

print(log[0], len(log[0]))
