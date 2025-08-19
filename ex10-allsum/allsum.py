def allsum(*args):
    '''
    Функция суммирует произвольное количество аргументов
    различных типов (один тип в наборе): целые числа, числа 
    с плавающей точкой, строки, кортежи, списки. 
    Возвращает один объект тогоже типа.
    '''
    if not args:
        raise ValueError("Function need 1 or more arguments")
    res = args[0]
    for item in args[1:]:
        res += item
    return res
