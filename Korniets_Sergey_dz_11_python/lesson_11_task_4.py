# Начать работу над проектом "Склад оргтехники". Создать класс, описывающий склад.
# А также класс "Оргтехника", который будет базовым для классов наследников. Эти
# классы - конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе
# определить параметры, общие для приведенных типов. В классах наследниках реализовать
# параметры, уникальные для каждого типа оргтехники


class Warehouse:
    def __init__(self, sample):
        self.sample = sample

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
