"""
4. * (вместо 3) Решить задачу 3 для ситуации, когда объём данных в файлах превышает объём ОЗУ (разумеется, не нужно
реально создавать такие большие файлы, это просто задел на будущее проекта). Также реализовать парсинг данных из файлов
- получить отдельно фамилию, имя и отчество для пользователей и название каждого хобби: преобразовать в какой-нибудь
контейнерный тип (список, кортеж, множество, словарь). Обосновать выбор типа. Подумать, какие могут возникнуть проблемы
при парсинге. В словаре должны храниться данные, полученные в результате парсинга.
"""

import json

fio_list = []
hobby_list = []
output = []

with open('users.txt', 'r', encoding='utf-8') as f:
    for line in f:
        if line[-1] == '\n':
            line = line[:-1]
        fio = line.split(',')
        fio_list.append(fio)

with open('hobby.txt', 'r', encoding='utf-8') as f:
    for line in f:
        if line[-1] == '\n':
            line = line[:-1]
        hobby = line.split(',')
        hobby_list.append(hobby)

if len(hobby_list) > len(fio_list):
    exit(1)

for i in range(len(hobby_list)):
    output.append([*fio_list[i], *hobby_list[i]])
for i in range(len(hobby_list), len(fio_list)):
    output.append([*fio_list[i], None])

with open('hw4output.txt', 'w', encoding='utf-8') as f:
    json.dump(output, f)

with open('hw4output.txt', 'r', encoding='utf-8') as f:
    print(json.load(f))