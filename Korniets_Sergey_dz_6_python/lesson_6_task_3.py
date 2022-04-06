# Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби.
# Известно, что при хранении данных используется принцип: одна строка — один пользователь,
# разделитель между значениями — запятая. Написать код, загружающий данные из обоих файлов
# и формирующий из них словарь: ключи — ФИО, значения — данные о хобби. Сохранить словарь
# в файл. Проверить сохранённые данные. Если в файле, хранящем данные о хобби, меньше
# записей, чем в файле с ФИО, задаём в словаре значение None. Если наоборот — выходим из
# скрипта с кодом «1». При решении задачи считать, что объём данных в файлах во много раз
# меньше объема ОЗУ.
# Фрагмент файла с данными о пользователях (users.csv):
# Иванов,Иван,Иванович
# Петров,Петр,Петрович
# Фрагмент файла с данными о хобби (hobby.csv):
# скалолазание,охота
# горные лыжи
from itertools import zip_longest
import json

res = {}
with open('users.csv', encoding='utf-8') as f_users:
    with open('hobby.csv', encoding='utf-8') as f_hobby:
        count_lines_user = sum(1 for line in f_users)
        count_lines_hobby = sum(1 for line in f_hobby)

        if count_lines_user < count_lines_hobby:
            exit(1)

        f_users.seek(0)
        f_hobby.seek(0)
        for line_user, line_hobby in zip_longest(f_users, f_hobby):
            res[line_user.strip()] = line_hobby.strip() if line_hobby is not None else line_hobby

with open('res.json', 'w', encoding='utf-8') as f:
    json.dump(res, f, ensure_ascii=False)

print(res)
