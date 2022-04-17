# A) Написать декоратор для логирования типов позиционных аргументов функции, например:
# def type_logger...
# ...
# @type_logger
# def calc_cube(x):
# return x ** 3
# >>> a = calc_cube(5)
# 5: <class 'int'>
# Примечание: если аргументов несколько - выводить данные о каждом через запятую;
# B) можете ли вы вывести тип значения функции?
# C) Сможете ли решить задачу для именованных аргументов?
# D) Сможете ли вы замаскировать работу декоратора? Сможете ли вывести имя
# функции, например, в виде:
# >>> a = calc_cube(5)
# calc_cube(5: <class 'int'>)

# Решение пункта А) для одного аргумента
def type_logger(func):
    def wrapper(x):
        print(f'{x}: {type(x)}')
    return wrapper

@type_logger
def calc_cube(x):
    return x ** 3

calc_cube(5)

# Решение пункта А) для нескольких аргументов
def type_logger(func):
    def wrapper(*args):
        for i in args:
            print(f'{i}: {type(i)}', end=', ')
    return wrapper

@type_logger
def calc_cube(x, y, z):
    return x ** 3

calc_cube(5, 2.75, 'struct')

# Решение пункта B)
def type_logger(func):
    def wrapper(x):
        print(f'{x}: {type(x)}')
        print(f'Тип значения функции: {type(func(x))}')
    return wrapper

@type_logger
def calc_cube(x):
    return x ** 3

calc_cube(5)

# Решение пункта C)
def type_logger(func):
    def wrapper(**kwargs):
        for key, val in kwargs.items():
            print(f'{val}: {type(val)}', end=', ')
    return wrapper

@type_logger
def calc_cube(x=3, y=1.15, z='rtu'):
    return x ** 3

calc_cube(x=5, y=2.75, z='struct')

# Решение пункта D)
from functools import wraps
def type_logger(func):
    @wraps(func)
    def wrapper(x):
        print(f'{func.__name__}({x}: {type(x)})')
    return wrapper

@type_logger
def calc_cube(x):
    return x ** 3

a = calc_cube(5)
