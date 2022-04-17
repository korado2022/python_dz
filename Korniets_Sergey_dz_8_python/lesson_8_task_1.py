# A) Написать функцию email_parse(<email_address>), которая при помощи регулярного
# выражения извлекает имя пользователя и почтовый домен из email адреса и возвращает их в
# виде словаря. Если адрес не валиден, выбросить исключение ValueError. Пример:
# >>> email_parse('someone@geekbrains.ru')
# {'username': 'someone', 'domain': 'geekbrains.ru'}
# >>> email_parse('someone@geekbrainsru')
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# ...
# raise ValueError(msg)
# ValueError: wrong email: someone@geekbrainsru
# Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном
# выражении;
# B) имеет ли смысл в данном случае использовать функцию re.compile()?
import re

RE_MAIL = re.compile(r"([^@&]+)@([\w_-][\w_\.-]*\.[\w_-]{2,})$")

def email_parse(email):
    parsed = re.findall(RE_MAIL, email)
    if not parsed:
        msg = f"wrong email: {email}"
        raise ValueError(msg)
    return dict(zip(["username", "domain"], parsed[0]))

print(email_parse('someone@geekbrains.info'))
print(email_parse('someone@geekbrainsru'))

# Задание B)
# Функция re.compile() улучшает читаемость программы
