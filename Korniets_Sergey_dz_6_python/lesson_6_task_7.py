# *(вместо 6) Добавить возможность редактирования данных при помощи отдельного скрипта:
# передаём ему номер записи и новое значение. При этом файл не должен читаться целиком —
# обязательное требование. Предусмотреть ситуацию, когда пользователь вводит номер записи,
# которой не существует.

import sys

edit_index, new_value = sys.argv[1:]
with open('selling.csv', 'r+', encoding='utf-8') as f:
    tmp_file = open('sel.tmp', 'w+', encoding='utf-8')
    change = False
    for index, line in enumerate(f, 1):
        if index == int(edit_index):
            tmp_file.write(f'{new_value}\n')
            change = True
        else:
            tmp_file.write(line)

    if not change:
        exit('error')

    tmp_file.seek(0)

    f.seek(0)
    f.truncate()
    for line in tmp_file:
        f.write(line)

    tmp_file.close()

# python 21.py 3 342,22
