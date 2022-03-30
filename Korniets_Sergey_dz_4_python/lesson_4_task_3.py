# *(вместо 2) Доработать функцию currency_rates(): теперь она должна возвращать кроме курса
# дату, которая передаётся в ответе сервера. Дата должна быть в виде объекта date. Подумайте,
# И как извлечь дату из ответа, какой тип данных лучше использовать в ответе функции?


# Решение подпункта А)
from requests import get
from decimal import *
from datetime import datetime

getcontext().prec = 4

def currency_rates(curr):
    curr = curr.upper()
    response = get('http://www.cbr.ru/scripts/XML_daily.asp').text

    if curr not in response:
        return None

    rub = response[response.find('<Value>', response.find(curr)) + 7:response.find('</Value>', response.find(curr))]
    date_curr = response[response.find('Date="') + 6:response.find('"', response.find('Date="') + 6)].split('.')
    day, month, year = map(int, date_curr)
    date_sh = datetime(day=day, month=month, year=year)
    return f"1 {curr} = {Decimal(rub.replace(',', '.'))} руб., {datetime.date(date_sh)}"

print(currency_rates('EUR'))
print(currency_rates('USD'))
print(currency_rates('eur'))
print(currency_rates('GBP'))
print(currency_rates('RRR'))
