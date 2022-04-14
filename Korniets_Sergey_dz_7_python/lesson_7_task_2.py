# *(вместо 1) Написать скрипт, создающий из config.yaml стартер для проекта со следующей
# структурой:
# |--my_project
#     |--settings
#     |   |--__init__.py
#     |   |--dev.py
#     |   |--prod.py
#     |--mainapp
#     |   |--__init__.py
#     |   |--models.py
#     |   |--views.py
#     |   |--templates
#     |       |--mainapp
#     |           |--base.html
#     |           |--index.html
#     |--authapp
#     |   |--__init__.py
#     |   |--models.py
#     |   |--views.py
#     |   |--templates
#     |       |--authapp
#     |           |--base.html
#     |           |--index.html
# Примечание: структуру файла config.yaml придумайте сами, его можно создать в любом
# текстовом редакторе «руками» (не программно); предусмотреть возможные исключительные
# ситуации, библиотеки использовать нельзя.

# files = {'my_project/settings': ['__init__.py', 'dev.py', 'prod.py'],
#          'my_project/mainapp': ['__init__.py', 'models.py', 'views.py'],
#          'my_project/mainapp/templates/mainapp': ['base.html', 'index.html'],
#          'my_project/authapp': ['__init__.py', 'models.py', 'views.py'],
#          'my_project/authapp/templates/authapp': ['base.html', 'index.html']}

import os
import yaml

dic_files = {'my_project':
                [{'settings': [
                    '__init__.py', 'dev.py', 'prod.py'
                ],
                },
                    {'mainapp': [
                        '__init__.py', 'models.py', 'views.py', {'templates': [{
                            'mainapp': ['base.html', 'index.html']}]
                        }]},
                    {'authapp': ['__init__.py', 'models.py', 'views.py', {'templates': [{
                        'authapp': ['base.html', 'index.html']}]
                    }
                                 ]
                     }
                ]
            }
with open('config.yaml', 'w', encoding='utf-8') as f:
    f.write(yaml.dump(dic_files))

with open('config.yaml', encoding='utf-8') as y_f:
    struct = yaml.safe_load(y_f)

def create_struct(data):
    for dir, struct_item in data.items():
        if not os.path.exists(dir):
            os.mkdir(dir)
        os.chdir(dir)
        for item in struct_item:
            if isinstance(item, dict):
                create_struct(item)
            else:
                if not os.path.exists(item):
                    if '.' in item:
                        open(item, 'w').close()
    else:
        os.chdir('../')

create_struct(struct)
