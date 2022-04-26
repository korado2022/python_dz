# A) (вместо задачи 3) Написать функцию thesaurus_adv(), принимающую в качестве
# аргументов строки в формате "Имя Фамилия" и возвращающую словарь, в котором
# ключи — первые буквы фамалий, а значения — словари, реализованные по схеме
# предыдущего задания и содержащие записи, в которых фамилия начинается
# с соответствующей буквы. Например
# thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр
# Алексеев", "Илья Иванов", "Анна Савельева")
# {
#   "А": {
#       "П": ["Петр Алексеев"]
#   },
#   "И": {
#       "И": ["Илья Иванов"]
#   },
#   "С": {
#       "И": ["Иван Сергеев", "Инна Серова"],
#       "А": ["Анна Савельева"]
#   }
# }
# B) Как поступить, если потребуется сортировка по ключам?


# Задание A)

def thesaurus_adv(*args):
    res = {}
    for arg in args:
        name, surname = arg.split()
        res.setdefault(surname[0], {})
        res[surname[0]].setdefault(name[0], [])
        res[surname[0]][name[0]].append(arg)
    return res

print(thesaurus_adv("Иван Сергеев", "Мария Астахова", "Петр Алексеев",
                    "Илья Иванов", "Инна Серова", "Анна Савельева"))

# Задание B)
# Сначала словарь преобразуем в список кортежей
# Затем сортировка по первому элементу
# И напоследок преобразование списка кортежей в словарь


dict_name = thesaurus_adv("Иван Сергеев", "Мария Астахова", "Петр Алексеев",
                     "Илья Иванов", "Инна Серова", "Анна Савельева")
print(dict_name)
dict_name_tuple = sorted(dict_name.items(), key=lambda x: x[0])
dict_name_sort = dict(dict_name_tuple)
print(dict_name_sort)