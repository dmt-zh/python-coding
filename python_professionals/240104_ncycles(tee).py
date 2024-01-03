# Реализуйте функцию ncycles(), которая принимает два аргумента в следующем порядке:

# iterable — итерируемый объект
# times — натуральное число

# Функция должна возвращать итератор, генерирующий последовательность элементов итерируемого объекта iterable,
# зацикленных times раз.

# Примечание 1. Элементы итерируемого объекта в возвращаемом функцией итераторе должны располагаться в своем исходном порядке.
# Примечание 2. Гарантируется, что итерируемый объект, передаваемый в функцию, не является множеством.


from itertools import tee

def ncycles(sequence, n):
    pairs = tee(sequence, n)
    for pair in pairs:
        yield from pair