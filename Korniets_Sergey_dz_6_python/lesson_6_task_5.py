# **(вместо 4) Решить задачу 4 и реализовать интерфейс командной строки, чтобы можно было
# задать имя обоих исходных файлов и имя выходного файла. Проверить работу скрипта.

from itertools import zip_longest
import sys
users, hobby, out = sys.argv[1:]
with open(out, 'w', encoding='utf-8') as f_res:
    with open(users, encoding='utf-8') as f_users:
        with open(hobby, encoding='utf-8') as f_hobby:
            count_lines_users = sum(1 for line in f_users)
            count_lines_hobby = sum(1 for line in f_hobby)

            if count_lines_users < count_lines_hobby:
                exit(1)

            f_users.seek(0)
            f_hobby.seek(0)
            for line_user, line_hobby in zip_longest(f_users, f_hobby):
                f_res.write(f'{line_user.strip()}: '
                            f'{line_hobby.strip() if line_hobby is not None else line_hobby}\n')

# python 24.py "users.csv" "hobby.csv" "res_5.txt"
