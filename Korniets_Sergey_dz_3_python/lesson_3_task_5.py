# А) Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех
# случайных слов, взятых из трёх списков (по одному из каждого):
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
# B) Добавить еще один аргумент — флаг, разрешающий или запрещающий повторы
# слов в шутках (когда каждое слово можно использовать только в одной шутке)
# Сделать аргументы именованными
#


import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

# Решение подпункта А)
def get_jokes(n):
    """
    Генератор шуток из фраз
    :param n: int, количество генерируемых шуток
    :return: list, список шуток
    """
    res = []
    for i in range(n):
        noun = random.choice(nouns)
        adv = random.choice(adverbs)
        adj = random.choice(adjectives)
        res.append(f'{noun} {adv} {adj}')
    return res

print(get_jokes(1))
print(get_jokes(3))

# Решение подпункта B)

def get_jokes_adv(n, repeat=True):
    """
    Генератор шуток из фраз
    :param n: int, количество генерируемых шуток
    :param repeat: bool, разрешение повтора слов
    :return: list, список шуток
    """
    res = []

    if not repeat:
        if n > min(len(nouns), len(adverbs), len(adjectives)):
            return 'Количество шуток указано больше' \
                   ' количества имеющихся слов'
        else:
            random.shuffle(nouns)
            random.shuffle(adverbs)
            random.shuffle(adjectives)
            for i in range(n):
                res.append(f'{nouns[i]} {adverbs[i]} {adjectives[i]}')

    else:
        for i in range(n):
            noun = random.choice(nouns)
            adv = random.choice(adverbs)
            adj = random.choice(adjectives)
            res.append(f'{noun} {adv} {adj}')
    return res

print(get_jokes_adv(2))
print(get_jokes_adv(3, False))
