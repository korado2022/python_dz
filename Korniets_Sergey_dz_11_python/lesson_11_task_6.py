# Продолжить работу над предыдущим заданием. Реализовать механизм валидации вводимых
# пользователем данных. Например, для указания количества принтеров, отправленных на
# склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь реализовать в проекте "Склад оргтехники" максимум возможностей,
# изученных на уроках по ООП



class Warehouse:
    def __init__(self, sample):
        self.sample = sample
        self.contain = {}
        self.depart = {}

    def reception_equip(self, sample):
        self.contain.setdefault(sample.product, 0)
        self.contain[sample.product] = self.contain[sample.quantity]

    def transfer_equip(self, sample):
        self.depart.setdefault(sample.product, 0)
        self.depart[sample.product] = self.contain.pop(sample)


class OfficeEquipment:
    def __init__(self, product, company, model, year, count, size, quantity):
        self.product = product
        self.company = company
        self.model = model
        self.year = None
        self.count = count
        self.size = size
        self.quantity = None
        set_year(year)
        set_quantity(quantity)

    def set_year(self, year):
        if year.isdigit():
            if 1970 < self.year < 2022:
                self.year = year
        else:
            print('Год производства не соответствует формату')

    def set_quantity(self, quantity):
        if quantity.isdigit():
            self.quantity = quantity
        else:
            print('Количество указано не верно')


class Printer(OfficeEquipment):
    def __init__(self, type_jet, color, speed_print):
        super.__init__(product, company, model, year, count, size, quantity)
        self.type_jet = type_jet
        self.color = color
        self.speed_print = speed_print

class Scanner(OfficeEquipment):
    def __init__(self, type_scan, speed_scan):
        super.__init__(product, company, model, year, count, size, quantity)
        self.type_scan = type_scan
        self.speed_scan = speed_scan

class Copier(OfficeEquipment):
    def __init__(self, type_copier, speed_copier):
        super.__init__(product, company, model, year, count, size, quantity)
        self.type_copier = type_copier
        self.speed_copier = speed_copier

