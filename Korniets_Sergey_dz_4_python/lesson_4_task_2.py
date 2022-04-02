# A) Написать функцию currency_rates(), принимающую в качестве аргумента код валюты
# (например, USD, EUR, GBP, ...) и возвращающую курс этой валюты по отношению к рублю.
# Использовать библиотеку requests. В качестве API можно использовать
# http://www.cbr.ru/scripts/XML_daily.asp.
# B) Можно ли, используя только методы класса str, решить поставленную задачу?
# Функция должна возвращать результат числового типа, например float.
# C) Подумайте: есть ли смысл для работы с денежными величинами использовать
# вместо float тип Decimal?
# Если в качестве аргумента передали код валюты, которого нет в ответе, вернуть None.
# Можно ли сделать работу
# функции не зависящей от того, в каком регистре был передан аргумент?
# В качестве примера выведите курсы доллара и евро.
#
#

# Решение подпункта А)
from requests import get
from decimal import *

getcontext().prec = 4

def currency_rates(curr):
    curr = curr.upper()
    response = get('http://www.cbr.ru/scripts/XML_daily.asp').text

    if curr not in response:
        return None

    rub = response[response.find('<Value>', response.find(curr)) + 7:response.find('</Value>', response.find(curr))]
    return f"1 {curr} = {Decimal(rub.replace(',', '.'))} руб."

print(currency_rates('EUR'))
print(currency_rates('USD'))
print(currency_rates('eur'))
print(currency_rates('GBP'))
print(currency_rates('RRR'))

# Решение подпункта B)
# Нет, потому что необходимо делать запросы API

# Решение подпункта С)
# Да для работы с денежными величинами лучше использовать тип Decimal

