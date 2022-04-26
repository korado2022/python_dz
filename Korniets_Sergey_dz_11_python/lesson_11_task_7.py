# Реализовать проект "Операция с комплексными числами". Создать класс "Комплексное число"
# Реализовать перегрузку методов сложения и умножения комплексных чисел. Проверить
# работу проекта. Для этого создать экземпляры класса (комплексные числа), выполнить сложение
# и умножение созданных экземпляров. Проверить корректность полученного результата


class ComplexNum():
    def __init__(self, num_1, num_2):
        self.a = num_1
        self.b = num_2

    def __add__(self, other):
        return complex((self.a + other.a), (self.b + other.b))

    def __str__(self):
        return f'{self.a} + {self.b}j'

    def __mul__(self, other):
        return complex((self.a + other.a - self.b * other.b), (self.b * other.a + self.a * other.b))


d = ComplexNum(2, 3)
f = ComplexNum(1, 0.5)

k = d + f
print(k)
g = d * f
print(g)
