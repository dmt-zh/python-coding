# У Илона есть куча файлов на компьютере. Для запуска ракеты на Марс нужен секретный код, который был утерян.
# Илон написал программу, которая открывает каждый документ по очереди и проходит по каждой его строке (4 строки
# за один проход). Допишите его программу так, чтобы она находила слово "Код" или "код". У Илона больше нет никаких
# секретных кодов на компьютере, поэтому он решил использовать re.search(), т.к. re.search() находит только первое
# вхождение подстроки в строке.

# Мы ищем именно слово код, не сам код. Илон не помнит из каких символов он составлен, а также его длину.
# Найти сам код будет сложно. На вход программе подаются 4 строки. Выведите в консоль номер строки, в которой было
# найдено вхождение, и через пробел начальную позицию этого вхождения.

# Sample Input 1:
# Хочу полететь на Марс(
# Секретный код: Dogecoin
# Батут работает!
# Где ключи от моей Tesla?

# Sample Output 1:
# 2 10



import sys
import re

data = list(map(str.strip, sys.stdin.readlines()))

def find_word_code(arr):
    for idx, segment in enumerate(arr, 1):
        has_code = re.search(r'[Кк]од', segment)
        if has_code:
            print(idx, has_code.start(), sep=' ')

find_word_code(data)