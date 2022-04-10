# Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или
# «руками» в проводнике). Написать скрипт, который собирает все шаблоны в одну папку
# templates, например:
# |--my_project
# ...
# |--templates
# |     |--mainapp
# |     |   |--base.html
# |     |   |--index.html
# |     |--authapp
# |         |--base.html
# |         |--index.html
# Примечание: исходные файлы необходимо оставить; обратите внимание, что html-файлы
# расположены в родительских папках (они играют роль пространств имён); предусмотреть
# возможные исключительные ситуации; это реальная задача, которая решена, например, во
# фреймворке django

import os
import shutil
new_dir = 'templates'
dir_root = r'my_project'

for r, d, f in os.walk(dir_root):
    for file in f:
        if '.html' in file:
            if not os.path.exists(os.path.join(dir_root, new_dir, os.path.split(r)[-1])):
                os.makedirs(os.path.join(dir_root, new_dir, os.path.split(r)[-1]))
            shutil.copy(os.path.join(r, file), os.path.join(dir_root, new_dir, os.path.split(r)[-1], file))
