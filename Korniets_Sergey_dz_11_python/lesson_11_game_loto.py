"""
== Лото ==
Правила игры в лото.
Игра ведется с помощью специальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.
Количество бочонков — 90 штук (с цифрами от 1 до 90).
Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
    Если цифра есть на карточке - она зачеркивается и игра продолжается.
    Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
    Если цифра есть на карточке - игрок проигрывает и игра завершается.
    Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.
Пример одного хода:
Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11
      16 49    55 88    77
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html

"""

import random
class LotoGame:
    def __init__(self, player_1, player_2):
        self._player_1 = player_1
        self._player_2 = player_2
        self.list_barr = LotoCard.get_list_barr()
        self.number = 0
        self.count = len(self.list_barr)

    def start(self):
        while True:
            self._player_1.print_card()
            self._player_2.print_card()
            self.number = self.list_barr.pop()
            print(f'Новый бочонок: {self.number} (осталось {len(self.list_barr)})')
            ans = input('Зачеркнуть цифру? (y/n)  ')
            fin_num_p_1 = self._player_1.find_num(self.number)
            fin_num_p_2 = self._player_2.find_num(self.number)

            if not fin_num_p_1 and ans == 'y' or fin_num_p_1 and ans == 'n':
                print('Вы проиграли')
                exit(0)
            elif fin_num_p_1 and ans == 'y':
                self._player_1.repl_val(self.number)

            if self._player_1.count_card == 0:
                print('Вы выиграли!')
                exit(0)

            if fin_num_p_2:
                self._player_2.repl_val(self.number)

            if self._player_2.count_card == 0:
                print(f'Выиграл {self._player_2.name}!')
                exit(0)


class LotoCard:
    def __init__(self, name):
        self.name = name
        self.stanc = [[1, 1, 1, 1, 1, 0, 0, 0, 0],
                        [1, 1, 1, 1, 1, 0, 0, 0, 0],
                        [1, 1, 1, 1, 1, 0, 0, 0, 0]]
        self.barr = []
        self.card = []
        self.count_card = 15
        LotoCard.creat_card(self)

    @staticmethod
    def get_list_barr():
        list = [x for x in range(1, 91)]
        random.shuffle(list)
        return list

    def card_random(self):
        for line in self.stanc:
            random.shuffle(line)

    def creat_card(self):
        self.barr = self.get_list_barr()
        self.card_random()
        start_l = 12
        for line in self.stanc:
            barr_line = self.barr[start_l:start_l + 5]
            barr_line.sort()
            num = 0
            res = []
            for x in line:
                if x != 0:
                    res.append(barr_line[num])
                    num += 1
                else:
                    res.append(0)
            self.card.append(res)
            start_l += 7


    def print_card(self):
        print(f'{self.name}:')
        print('-' * 26)

        for line in self.card:
            res = []
            for n in line:

                if n == 0:
                    res.append('  ')
                elif n == '- ':
                    res.append(n)
                else:
                    if len(str(n)) == 1:
                        res.append(f'{n} ')
                    else:
                        res.append(f'{n}')
                res.append(' ')
            print(''.join(res))
        print('-' * 26)

    def find_num(self, number):
        for line in self.card:
            if number in line:
                return True
        return False

    def repl_val(self, number):
        for line in self.card:
            for index, item in enumerate(line):
                if item == number:
                    line[index] = '- '
                    self.count_card -= 1


human_player = LotoCard('Игрок')
computer_player = LotoCard('Компьютер')

game = LotoGame(human_player, computer_player)
game.start()

