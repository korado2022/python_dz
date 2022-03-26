# (вместо задачи 1) Доработать предыдущую функцию в num_translate_adv(): реализовать
# корректную работу с числительными, начинающимися с заглавной буквы — результат тоже
# должен быть с заглавной: num_translate_adv("One") "Один"

dict_translate = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре',
                  'five': 'пять', 'six': 'шесть', 'seven': 'семь', 'eight': 'восемь',
                  'nine': 'девять', 'ten': 'десять', 'zero': 'ноль'}

def num_translate_adv(num_str):
    """
    Переводит числительные от 0 до 10 с английского на русский язык
    :param num_str: string, числительное на английском языке
    :return: string, числительное на русском языке
    """
    upp_str = False
    if num_str[0].isupper():
        upp_str = True
        num_str = num_str.lower()
    if num_str in dict_translate:
        if upp_str:
            return dict_translate[num_str].title()
        else:
            return dict_translate[num_str]
    else:
        return 'None'

print(num_translate_adv('One'))
print(num_translate_adv('two'))
print(num_translate_adv('Five'))
print(num_translate_adv('string'))
