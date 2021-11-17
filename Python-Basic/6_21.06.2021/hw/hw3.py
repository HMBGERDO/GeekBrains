"""
3. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби. Известно, что при хранении
данных используется принцип: одна строка — один пользователь, разделитель между значениями — запятая. Написать код,
загружающий данные из обоих файлов и формирующий из них словарь: ключи — ФИО, значения — данные о хобби. Сохранить
словарь в файл. Проверить сохранённые данные. Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО,
задаём в словаре значение None. Если наоборот — выходим из скрипта с кодом «1». При решении задачи считать, что объём
данных в файлах во много раз меньше объема ОЗУ.
"""

import json

fio_list = []
hobby_list = []
output = {}

with open('users.txt', 'r', encoding='utf-8') as f:
    for line in f:
        if line[-1] == '\n':
            line = line[:-1]
        fio = ' '.join(line.split(','))
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
    output[fio_list[i]] = hobby_list[i]
for i in range(len(hobby_list), len(fio_list)):
    output[fio_list[i]] = None

with open('hw3output.txt', 'w', encoding='utf-8') as f:
    json.dump(output, f)

with open('hw3output.txt', 'r', encoding='utf-8') as f:
    print(json.load(f))
