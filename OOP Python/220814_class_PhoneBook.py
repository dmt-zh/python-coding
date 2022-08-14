# Вы создаете телефонную записную книжку. Она определяется классом PhoneBook. Объекты этого класса создаются командой:
# p = PhoneBook()

# А сам класс должен иметь следующий набор методов:
# add_phone(phone) - добавление нового номера телефона (в список);
# remove_phone(indx) - удаление номера телефона по индексу списка;
# get_phone_list() - получение списка из объектов всех телефонных номеров.

# Каждый номер телефона должен быть представлен классом PhoneNumber. Объекты этого класса должны создаваться командой:
# note = PhoneNumber(number, fio)
# где number - номер телефона (число) в формате XXXXXXXXXXX (одиннадцати цифр, X - цифра); fio - Ф.И.О. владельца номера (строка).

# В каждом объекте класса PhoneNumber должны формироваться локальные атрибуты:
# number - номер телефона (число);
# fio - ФИО владельца номера телефона.

# Необходимо объявить два класса PhoneBook и PhoneNumber в соответствии с заданием.



class PhoneNumber:
    def __init__(self, phone, name):
        self.number = self.name = None
        if self.__check_phone(phone):
            self.number = phone
        if self.__check_name(name):
            self.fio = name

    @classmethod
    def __check_phone(cls, phone):
        if type(phone) == int and len(str(phone)) == 11:
            return True
        print('Enter correct phone number.')
        return False

    @classmethod
    def __check_name(cls, name):
        if type(name) == str and len(name) > 0:
            return True
        print('Name should be a string type and its length should be at least 1 symbol.')
        return False


class PhoneBook:
    def __init__(self):
        self.__book = list()

    def add_phone(self, phone):
        self.__book.append(phone)

    def remove_phone(self, indx):
        del self.__book[indx]

    def get_phone_list(self):
        return self.__book