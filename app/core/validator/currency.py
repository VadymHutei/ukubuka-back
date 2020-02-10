import re


def currencyCode(code):
    if isinstance(code, str):
        return re.fullmatch(r'[a-zA-Z]{3}', code)
    return False


def currencyName(name):
    if isinstance(name, str):
        return re.fullmatch(r'[0-9A-Za-zА-Яа-яЯєЄіІїЇёЁҐґ _-]{1,64}', name)
    return False


def currencySymbol(symbol):
    if isinstance(symbol, str):
        return re.fullmatch(r'.{1,8}', symbol)
    return False
