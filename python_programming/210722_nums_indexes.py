# Напишите программу, которая считывает список чисел lst из первой строки и число x из второй строки,
# которая выводит все позиции, на которых встречается число x в переданном списке lst.
# Позиции нумеруются с нуля, если число x не встречается в списке,
# вывести строку "Отсутствует" (без кавычек, с большой буквы).
# Позиции должны быть выведены в одну строку, по возрастанию абсолютного значения.
# Sample Input 1:       Sample Output 1:            Sample Input 2:     Sample Output 2:
# 5 8 2 7 8 8 2 4       1 4 5                       5 8 2 7 8 8 2 4     Отсутствует
# 8                                                 10


lst = [int(i) for i in input().split()]
x = int(input())

if x not in lst:
    print('Отсутствует')
else:
    [print(i, end=' ') for i in range(len(lst)) if lst[i] == x]
