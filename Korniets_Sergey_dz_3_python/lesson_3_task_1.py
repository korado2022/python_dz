# Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на
# русский язык. Например: num_translate("one") "один"  num_translate("eight")  "восемь"
# Если перевод сделать невозможно, вернуть None. Подумайте, как и где лучше хранить
# информацию, необходимую для перевода: какой тип данных выбрать, в теле функции или
# снаружи

dict_translate = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре',
                      'five': 'пять', 'six': 'шесть', 'seven': 'семь', 'eight': 'восемь',
                      'nine': 'девять', 'ten': 'десять', 'zero': 'ноль'}
                      
def num_translate(num_str):
    """
    Переводит числительные от 0 до 10 с английского на русский язык

    :param num_str: string, числительное на английском языке
    :return: string, числительное на русском языке
    """
    if num_str in dict_translate:
        return dict_translate[num_str]
    else:
        return 'None'

print(num_translate('one'))
print(num_translate('eight'))
print(num_translate('num'))
