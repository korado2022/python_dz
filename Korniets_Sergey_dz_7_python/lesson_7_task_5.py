# *(вместо 4) Написать скрипт, который выводит статистику для заданной папки в виде
# словаря, в котором ключи те же, а значения — кортежи вида
# (<files_quantity>, [<files_extensions_list>]), например:
#     {
#       100: (15, ['txt']),
#       1000: (3, ['py', 'txt']),
#       10000: (7, ['html', 'css']),
#       100000: (2, ['png', 'jpg'])
#     }
#
# Сохраните результаты в файл <folder_name>_summary.json в той же папке,
# где запустили скрипт
import json
import os

res = {}
ext = {}
for r, d, f in os.walk('./'):
    for file in f:
        file_path = os.path.join(r, file)
        file_size = os.stat(file_path).st_size
        res.setdefault(10 ** len(str(file_size)), 0)
        res[10 ** len(str(file_size))] += 1
        ext.setdefault(10 ** len(str(file_size)), [])
        ext[10 ** len(str(file_size))].append(file_path.split('.')[-1])

for key in ext:
    ext[key] = list(set(ext[key]))

dic_save = {}
for key in res:
    dic_save[key] = (res[key], ext[key])

print(dic_save)

with open(os.path.basename(os.getcwd()) + '_summary.json', 'w') as f_json:
    json.dump(dic_save, f_json)

