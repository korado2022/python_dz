# Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
# |--my_project
#   |--settings
#   |--mainapp
#   |--adminapp
#   |--authapp
# Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?);
# как лучше хранить конфигурацию этого стартера, чтобы в будущем можно было менять имена
# папок под конкретный проект;
# можно ли будет при этом расширять конфигурацию и хранить
# данные о вложенных папках и файлах (добавлять детали)?

import os, os.path


dic_dir = {'my_project': ['settings', 'mainapp', 'adminapp', 'authapp']}

for root in dic_dir:
    for folder in dic_dir[root]:
        if not os.path.exists(os.path.join(root, folder)):
            os.makedirs(os.path.join(root, folder))
