# Реализуйте декоратор ignore_exception, который принимает произвольное количество позиционных аргументов — типов исключений,
# и выводит текст: 
#     Исключение <тип исключения> обработано
# если во время выполнения декорируемой функции было возбуждено исключение, принадлежащее одному из переданных типов.

# Если возбужденное исключение не принадлежит ни одному из переданных типов, оно должно быть возбуждено снова.

# Также декоратор должен сохранять имя и строку документации декорируемой функции.

# Примечание. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции,
# а также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.


from functools import wraps

def ignore_exception(*exceptions):
    def call_func(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except (exceptions) as err:
                print(f'Исключение {err.__class__.__name__} обработано')
        return wrapper
    return call_func