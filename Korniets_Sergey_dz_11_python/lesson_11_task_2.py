# Создать собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверить ево работу на данных, вводимых пользователем. При вводе нуля в качестве
# делителя программа должна корректно обработать эту ситуацию и не завершиться ошибкой


class ZeroDivisionError(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    divident = int(input('Введите делимое: '))
    divisor = int(input('Введите делитель: '))
    if divisor == 0:
        raise ZeroDivisionError('На ноль делить нельзя')
except ValueError:
    print('Вы ввели не число')
except ZeroDivisionError as err:
    print(err)
else:
    print(f'Частное = {divident / divisor}')

