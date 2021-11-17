"""
1. Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?); как лучше хранить конфигурацию
этого стартера, чтобы в будущем можно было менять имена папок под конкретный проект; можно ли будет при этом расширять
конфигурацию и хранить данные о вложенных папках и файлах (добавлять детали)?
2. * (вместо 1) Написать скрипт, создающий из config.yaml стартер для проекта со следующей структурой:
Примечание: структуру файла config.yaml придумайте сами, его можно создать в любом текстовом редакторе «руками»
(не программно); предусмотреть возможные исключительные ситуации, библиотеки использовать нельзя.
"""

import os

with open('cfg.yaml', 'r') as f:
    structure = []
    way = []
    current = None
    level = 0
    for line in f:
        if line.endswith('\n'):
            line = line[:-1]
        level = line.index('|--') // 3
        if level == 0:
            way = [line[3:]]
            structure.append(os.path.join(*way))
        elif level + 1 > len(way):
            way.append(line[(level+1)*3:])
            structure.append(os.path.join(*way))
        elif level + 1 < len(way):
            way = way[:level]
            way.append(line[(level+1)*3:])
            structure.append(os.path.join(*way))
        elif level + 1 == len(way):
            way = way[:level]
            way.append(line[(level + 1) * 3:])
            structure.append(os.path.join(*way))
        else:
            print(f'error at {line}')
    for el in structure:
        try:
            el.index('.')
            if os.path.exists(el):
                print(f'{el} already exists!')
                continue
            with open(el, 'w') as f:
                f.write(el)
        except ValueError:
            if os.path.exists(el):
                print(f'{el} already exists!')
                continue
            os.mkdir(el)
