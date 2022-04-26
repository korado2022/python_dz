# Продолжить работу над предыдущим заданием. Разработать методы, которые отвечают
# за прием оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также
# других данных, можно использовать любую подходящую структуру (например словарь)



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
        self.year = year
        self.count = count
        self.size = size
        self.quantity = quantity

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
