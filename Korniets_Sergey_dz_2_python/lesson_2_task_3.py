# Дан список: ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# 1) Необходимо его обработать — обособить каждое целое число (вещественные не трогаем)
# кавычками (добавить кавычку до и кавычку после элемента списка, являющегося числом)
# и дополнить нулём до двух целочисленных разрядов:
# ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура',
# 'воздуха', 'была', '"', '+05', '"', 'градусов']
# 2) Сформировать из обработанного списка строку:
# в "05" часов "17" минут температура воздуха была "+05" градусов
# 3) Решить задачу 2 не создавая новый список
import re

list_str = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print(list_str)
print(id(list_str))

for item in list_str[:]:
     if re.search('\d+', item):
        index_num = list_str.index(item)
        if '+' in item:
            item = item.zfill(3)
        else:
            item = item.zfill(2)

        list_str.pop(index_num)
        list_str.insert(index_num, '"')
        list_str.insert(index_num + 1, item)
        list_str.insert(index_num + 2, '"')
        continue

print(list_str)

# Второй подпункт
message = ' '.join(list_str)
res_mess = ''
quote = False
for i in range(len(message)):
    if not quote and message[i] == '"':
        quote = True
        res_mess = res_mess + message[i]
        continue
    elif quote and message[i] == ' ':
        continue
    elif quote and message[i] == '"':
        quote = False
        res_mess = res_mess + message[i]
        continue
    else:
        res_mess = res_mess + message[i]

print(res_mess)

# Новый список не создается, а используется первоначальный list_str
print(id(list_str))

# Еще один вариант решения без создания нового списка
list_str = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print(list_str)
print(id(list_str))
len_list = len(list_str)
index_list = 0
for i in range(len_list):
    if re.search('\d+', list_str[index_list]):
        item = list_str[index_list]
        if '+' in item:
            item = item.zfill(3)
        else:
            item = item.zfill(2)

        list_str.pop(index_list)
        list_str.insert(index_list, '"')
        list_str.insert(index_list + 1, item)
        list_str.insert(index_list + 2, '"')
        index_list += 3
        continue
    else:
        index_list += 1

print(list_str)
print(id(list_str))

# Второй подпункт
message = ' '.join(list_str)
res_mess = ''
quote = False
for i in range(len(message)):
    if not quote and message[i] == '"':
        quote = True
        res_mess = res_mess + message[i]
        continue
    elif quote and message[i] == ' ':
        continue
    elif quote and message[i] == '"':
        quote = False
        res_mess = res_mess + message[i]
        continue
    else:
        res_mess = res_mess + message[i]

print(res_mess)

# Новый список не создается, а используется первоначальный list_str
print(id(list_str))
