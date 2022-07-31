# Объявите класс EmailValidator для проверки корректности email-адреса.
# Необходимо запретить создание объектов этого класса: при создании экземпляров должно возвращаться значение None, например:
# em = EmailValidator() # None

# В самом классе реализовать следующие методы класса (@classmethod):
# check_email(cls, email) - возвращает True, если email записан верно и False - в противном случае;
# get_random_email(cls) - для генерации случайного email-адреса по формату: xxxxxxx...xxx@gmail.com,
# где x - любой допустимый символ в email (латинский буквы, цифры, символ подчеркивания и точка).

# Корректность строки email определяется по следующим критериям:
# - допустимые символы: латинский алфавит, цифры, символы подчеркивания, точки и собачка @ (одна);
# - длина email до символа @ не должна превышать 100 (сто включительно);
# - длина email после символа @ не должна быть больше 50 (включительно);
# - после символа @ обязательно должна идти хотя бы одна точка;
# - не должно быть двух точек подряд.

# Также в классе нужно реализовать приватный статический метод класса:
# is_email_str(email) - для проверки типа переменной email, если строка, то возвращается значение True, иначе - False.

# Метод is_email_str() следует использовать в методе check_email() перед проверкой корректности email.
# Если параметр email не является строкой, то check_email() возвращает False.

# Пример использования класса EmailValidator (эти строчки в программе писать не нужно):
# res = EmailValidator.check_email("sc_lib@list.ru") # True
# res = EmailValidator.check_email("sc_lib@list_ru") # False



import random
from string import ascii_lowercase, digits, ascii_uppercase
import re

class EmailValidator:
    EMAIL_CHARS = ascii_lowercase + ascii_uppercase + digits

    def __new__(cls, *args, **kwargs):
        return None

    @staticmethod
    def __is_email_str(email):
        return type(email) == str

    @classmethod
    def check_email(cls, email):
        if cls.__is_email_str(email):
            pattern = '[0-9a-zA-Z_.]{,100}@[0-9a-zA-Z]*\.{1,}[a-zA-Z]*'
            if re.match(pattern, email) and email.count('..') < 1:
                return True
        return False

    @classmethod
    def get_random_email(cls):
        new_email = ''.join([random.choice(cls.EMAIL_CHARS) for _ in range(random.randint(2, 30))])
        return f'{new_email}@gmail.com'