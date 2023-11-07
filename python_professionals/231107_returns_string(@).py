# Реализуйте декоратор returns_string, который проверяет, что возвращаемое значение декорируемой функции принадлежит типу str.
# Если возвращаемое значение принадлежит какому-либо другому типу, декоратор должен возбуждать исключение TypeError.

# Также декоратор должен сохранять имя и строку документации декорируемой функции.

# Примечание. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции, 
# а также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.


from functools import wraps

def returns_string(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        func_result = func(*args, **kwargs)
        if not isinstance(func_result, str):
            raise TypeError
        return func_result
    return wrapper