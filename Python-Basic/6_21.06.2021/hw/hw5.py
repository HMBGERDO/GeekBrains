"""
5. ** (вместо 4) Решить задачу 4 и реализовать интерфейс командной строки, чтобы можно было задать путь к обоим исходным
файлам и путь к выходному файлу со словарём. Проверить работу скрипта для случая, когда все файлы находятся в разных
папках.
"""

import json, sys

fio_list = []
hobby_list = []
output = []
users_file = sys.argv[1]
hobby_file = sys.argv[2]
output_file = sys.argv[3]

with open(users_file, 'r', encoding='utf-8') as f:
    for line in f:
        if line[-1] == '\n':
            line = line[:-1]
        fio = line.split(',')
        fio_list.append(fio)

with open(hobby_file, 'r', encoding='utf-8') as f:
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

with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(output, f)
