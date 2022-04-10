# *(вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла
# логов из предыдущего задания.

res = {}
with open('nginx_logs.txt') as f:
    for line in f:
        remote_addr = line[:line.find(' ')]
        res.setdefault(remote_addr, 0)
        res[remote_addr] += 1

res = sorted(res.items(), key=lambda items: items[1], reverse=True)
print(f'IP адрес спамера = {res[0][0]}, количество запросов = {res[0][1]}')
