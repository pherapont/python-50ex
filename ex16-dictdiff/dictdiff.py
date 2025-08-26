from typing import Any

def dictdiff(d1: dict[Any, Any], d2: dict[Any, Any]) -> dict[Any, Any]:

    """
    Функция получает на вход 2 словаря и 
    возвращает словарь с несовпад. значениями в виде:
    key: [val1, val2]. 
    Если ключ отсутствует в одном из словарей,
    key: [val1, None] ...
    """
    sd1 = set(d1)
    sd2 = set(d2)
    common_keys = sd1 & sd2
    keys_first = sd1 - sd2
    keys_second = sd2 - sd1
    
    r1 = {k: [d1[k], d2[k]] for k in common_keys
        if d1[k] != d2[k]}
    r2 = {k: [d1[k], None] for k in keys_first}
    r3 = {k: [None, d2[k]] for k in keys_second}

    return r1 | r2 | r3


if __name__ == '__main__':
    d2 = {'a':1, 'b':3, 'c':4}
    d4 = {'a':2, 'b':2, 'd':3}
    res = dictdiff(d2, d4)
    print(res)
