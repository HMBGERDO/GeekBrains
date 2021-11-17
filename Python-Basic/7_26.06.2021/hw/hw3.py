"""3. Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике).
Написать скрипт, который собирает все шаблоны в одну папку templates, например:
|--my_project
   ...
  |--templates
   |   |--mainapp
   |   |  |--base.html
   |   |  |--index.html
   |   |--authapp
   |      |--base.html
   |      |--index.html
Примечание: исходные файлы необходимо оставить; обратите внимание, что html-файлы расположены в родительских папках
(они играют роль пространств имён); предусмотреть возможные исключительные ситуации; это реальная задача, которая
решена, например, во фреймворке django."""

import os
import shutil

root_dir = 'my_project'
if not(os.path.exists(os.path.join(root_dir, 'templates'))):
    os.mkdir(os.path.join(root_dir, 'templates'))
for root, dirs, files in os.walk(root_dir):
    if root.endswith('templates') and not(root == os.path.join(root_dir, 'templates')):
        for file in files:
            shutil.copy(os.path.join(root, file), os.path.join(root_dir, 'templates', file))
        for dir in dirs:
            if not(os.path.exists(os.path.join(root_dir, 'templates', dir))):
                os.mkdir(os.path.join(root_dir, 'templates', dir))
            for dir_root, dir_dirs, dir_files in os.walk(root):
                for file in dir_files:
                    shutil.copy(os.path.join(dir_root, file), os.path.join(root_dir, 'templates', dir, file))
