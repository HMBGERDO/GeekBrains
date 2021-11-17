"""
Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи — верхняя граница размера
файла (пусть будет кратна 10), а значения — общее количество файлов (в том числе и в подпапках), размер которых не
превышает этой границы, но больше предыдущей (начинаем с 0), например:
    {
      100: 15,
      1000: 3,
      10000: 7,
      100000: 2
    }

Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.
*(вместо 4) Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи те же, а
значения — кортежи вида (<files_quantity>, [<files_extensions_list>]), например:
    {
      100: (15, ['txt']),
      1000: (3, ['py', 'txt']),
      10000: (7, ['html', 'css']),
      100000: (2, ['png', 'jpg'])
    }

Сохраните результаты в файл <folder_name>_summary.json в той же папке, где запустили скрипт.

"""
import os


def get_size_max(size):
    max = 1
    while True:
        if max > size:
            return max
        max = max * 10


def get_file_extension(name):
    name = name[::-1]
    try:
        name = name[:name.index('.')]
        return name[::-1]
    except ValueError:
        return None


root_dir = 'my_project'
result = {}
for root, dir, files in os.walk(root_dir):
    for file in files:
        size = get_size_max(os.stat(os.path.join(root, file)).st_size)
        if not(result.get(size)):
            result[size] = [1, [get_file_extension(file)]]
        else:
            result[size][0] = result[size][0] + 1
            if not get_file_extension(file) in result[size][1]:
                result[size][1].append(get_file_extension(file))
print(result)
