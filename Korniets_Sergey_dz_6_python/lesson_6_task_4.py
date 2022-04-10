# *(вместо 3) Решить задачу 3 для ситуации, когда объём данных в файлах превышает объём
# ОЗУ (разумеется, не нужно реально создавать такие большие файлы, это просто задел на
# будущее проекта). Только теперь не нужно создавать словарь с данными. Вместо этого нужно
# сохранить объединенные данные в новый файл (users_hobby.txt). Хобби пишем через
# двоеточие и пробел после ФИО:
# Иванов,Иван,Иванович: скалолазание,охота
# Петров,Петр,Петрович: горные лыжи

from itertools import zip_longest

with open('res_4.txt', 'w', encoding='utf-8') as f_res:
    with open('users.csv', encoding='utf-8') as f_users:
        with open('hobby.csv', encoding='utf-8') as f_hobby:
            count_lines_users = sum(1 for line in f_users)
            count_lines_hobby = sum(1 for line in f_hobby)

            if count_lines_users < count_lines_hobby:
                exit(1)

            f_users.seek(0)
            f_hobby.seek(0)
            for line_user, line_hobby in zip_longest(f_users, f_hobby):
                f_res.write(f'{line_user.strip()}: '
                            f'{line_hobby.strip() if line_hobby is not None else line_hobby}\n')
