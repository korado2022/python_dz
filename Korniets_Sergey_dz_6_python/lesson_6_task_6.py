# Реализовать простую систему хранения данных о суммах продаж булочной. Должно быть два
# скрипта с интерфейсом командной строки: для записи данных и для вывода на экран
# записанных данных. При записи передавать из командной строки значение суммы продаж.
# Для чтения данных реализовать в командной строке следующую логику:
# ● просто запуск скрипта — выводить все записи;
# ● запуск скрипта с одним параметром-числом — выводить все записи с номера, равного
# этому числу, до конца;
# ● запуск скрипта с двумя числами — выводить записи, начиная с номера, равного
# первому числу, по номер, равный второму числу, включительно.
# Подумать, как избежать чтения всего файла при реализации второго и третьего случаев.
# Данные хранить в файле bakery.csv в кодировке utf-8. Нумерация записей начинается с 1.
# Примеры запуска скриптов:
# python add_sale.py 5978,5
# python add_sale.py 8914,3
# python add_sale.py 7879,1
# python add_sale.py 1573,7
# python show_sales.py
# 5978,5
# 8914,3
# 7879,1
# 1573,7
# python show_sales.py 3
# 7879,1
# 1573,7
# python show_sales.py 1 3
# 5978,5
# 8914,3
# 7879,1

# add_sale.py
import sys

price = sys.argv[1]

with open('selling.csv', 'a', encoding='utf-8') as f:
    f.write(price + '\n')

# python add_sale.py 5978,5
# python add_sale.py 8914,3
# python add_sale.py 7879,1
# python add_sale.py 1573,7

# show_sales.py
import sys

nums = sys.argv[1:]
with open('selling.csv', encoding='utf-8') as f:
    if len(nums) > 1:
        start_index = int(nums[0])
        end_index = int(nums[1])
    elif len(nums) == 0:
        start_index = 0
        end_index = sum(1 for line in f)
        f.seek(0)
    else:
        start_index = int(nums[0])
        end_index = sum(1 for linr in f)
        f.seek(0)

    for index, line in enumerate(f):
        if start_index <= index + 1 <= end_index:
            print(line.strip())

# python show_sales.py 1 3
