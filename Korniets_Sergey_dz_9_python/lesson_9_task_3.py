# Реализовать базовый класс Worker (работник):
#     ● определить атрибуты: name, surname, position (должность), income (доход);
#     ● последний атрибут должен быть защищённым и ссылаться на словарь, содержащий
#     элементы «оклад» и «премия», например, {"wage": wage, "bonus": bonus};
#     ● создать класс Position (должность) на базе класса Worker;
#     ● в классе Position реализовать методы получения полного имени сотрудника
#     (get_full_name) и дохода с учётом премии (get_total_income);
#     ● проверить работу примера на реальных данных: создать экземпляры класса Position,
#     передать данные, проверить значения атрибутов, вызвать методы экземпляров.

class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income_wage = income["wage"]
        self._income_bonus = income["bonus"]

class Position(Worker):

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self._income_wage + self._income_bonus

posit = Position('Иван', 'Иванов', 'водитель', {"wage": 200, "bonus": 20})
print(posit.name)
print(posit.surname)
print(posit.position)
print(f'Полное имя сотрудника: {posit.get_full_name()}')
print(f'Доход с учетом премии составляет: {posit.get_total_income()} руб.')
