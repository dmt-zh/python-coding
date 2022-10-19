# Программист создал телеграм-бота, но потерял токен. К старому телеграм аккаунту у него нет доступа, поэтому он
# не может посмотреть токен у BotFather. Помогите программисту найти токен.
# На вход даётся 5 строк. В одной из строк находится токен. Токен может быть написан как на английском, так и на
# русском языке. Слово токен может начинаться с букв разного регистра, остальные буквы всегда в нижнем регистре.
# Выведите на экран номер строки, начало, и конец вхождения подстроки токен в строке.

# Мы ищем именно слово токен, не сам токен. Ведь если мы найдём слово токен, то программист без проблем найдёт сам токен.



import sys
import re

data = list(map(str.strip, sys.stdin.readlines()))

def find_token(arr):
    for idx, segment in enumerate(arr, 1):
        has_token = re.search(r'[Tt]oken|[Тт]окен', segment)
        if has_token:
            print(idx, has_token.start(), has_token.end(), sep=' ')

find_token(data)