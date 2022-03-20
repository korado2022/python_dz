# Дан список: ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# 1) Необходимо его обработать — обособить каждое целое число (вещественные не трогаем)
# кавычками (добавить кавычку до и кавычку после элемента списка, являющегося числом)
# и дополнить нулём до двух целочисленных разрядов:
# ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура',
# 'воздуха', 'была', '"', '+05', '"', 'градусов']
# 2) Сформировать из обработанного списка строку:
# в "05" часов "17" минут температура воздуха была "+05" градусов
import re

list_str = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

res = []
for item in list_str:
    if re.search('\d+', item):
        if '+' in item:
            item = item.zfill(3)
        else:
            item = item.zfill(2)
        res.extend(['"', item, '"'])
        continue
    res.append(item)
print(res)

# Второй подпункт
message = ' '.join(res)
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
