# Реализовать класс "Дата", функция-конструктор которого должна принимать дату
# в виде строки формата "день-месяц-год". В рамках класса реализовать два
# метода. Первый - с декоратором @classmethod. Он должен извлекать число,
# месяц, год и преобразовывать их тип к типу "Число". Второй с декоратором
# @staticmethod, должен проводить валидацию числа, месяца и года (например
# месяц - от 1 до 12). Проверить работу полученной структуры на реальных данных
import re
RE_DATA = re.compile(r'\d{2}-\d{2}-\d{4}')

class DataClass:
    def __init__(self, param):
        self.param = DataClass.check_data(param)


    @classmethod
    def str_to_dig(cls, param):
        return int(param[:2]), int(param[3:5]), int(param[-4:])

    @staticmethod
    def check_data(param):
        pars = re.findall(RE_DATA, param)
        if not pars:
            print('Строка не соответствует формату')
        else:
            data_tup = DataClass.str_to_dig(param)
            if not 0 < data_tup[0] <= 31:
                print('Значение числа месяца выходит за пределы')

            if not 0 < data_tup[1] <= 12:
                print('Значение месяца выходит за пределы')

            if not 0 < data_tup[2] <= 2022:
                print('Значение года выходит за пределы')
        return param


my_d = DataClass('12-11-2022')
print(my_d.str_to_dig('12-11-2022'))
