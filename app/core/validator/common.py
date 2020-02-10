import re


def languageCode(code):
    if isinstance(code, str):
        pattern = r'[a-z]{3}'
        return re.fullmatch(pattern, code)
    return False


def phoneNumber(phone_number):
    if isinstance(phone_number, str):
        return re.fullmatch(r'[0-9+() -]{9,64}', phone_number)
    if isinstance(phone_number, int):
        return 9 <= len(str(phone_number)) <= 32
    return False


def email(email):
    if isinstance(email, str):
        return re.fullmatch(r'[a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+', email)
    return False


def settingsProperty(prop):
    if isinstance(prop, str):
        return re.fullmatch(r'[\w. -]{1,64}', prop)
    return False


def password(prop):
    if isinstance(prop, str):
        return re.fullmatch(r'[\w\W]{3,64}', prop)
    return False


def sessionId(session_id):
    if isinstance(session_id, str):
        return bool(re.fullmatch(r'[0-9a-z]{64}', session_id))
    return False


def price(price):
    if isinstance(price, str):
        return re.fullmatch(r'[0-9 .,]{1,16}', price)
    if isinstance(price, int):
        return 1 <= len(str(price)) <= 6
    if isinstance(price, float):
        return 1 <= len(str(price)) <= 9
    return False


def order(order):
    if isinstance(order, str):
        return re.fullmatch(r'[0-9]{1,4}', order)
    if isinstance(order, int):
        return 1 <= len(str(order)) <= 4
    return False


def orderDirection(order):
    if isinstance(order, str):
        return order.lower() in ('asc', 'desc')
    return False


def active(active):
    if isinstance(active, str):
        return active.lower() in ('y', 'n')
    return False


def tableName(name):
    if isinstance(name, str):
        pattern = r'[0-9a-zA-Z_]{1,64}'
        return bool(re.fullmatch(pattern, name))
    return False
