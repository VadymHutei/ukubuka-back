import re


# Common

def languageCode(code) -> bool:
    if isinstance(code, str):
        pattern = r'[a-z]{3}'
        return re.fullmatch(pattern, code)
    return False


def phoneNumber(phone_number) -> bool:
    if isinstance(phone_number, str):
        return re.fullmatch(r'[0-9+() -]{9,64}', phone_number)
    if isinstance(phone_number, int):
        return 9 <= len(str(phone_number)) <= 32
    return False


def email(email) -> bool:
    if isinstance(email, str):
        return re.fullmatch(r'[a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+', email)
    return False


def settingsProperty(prop) -> bool:
    if isinstance(prop, str):
        return re.fullmatch(r'[\w. -]{1,64}', prop)
    return False


def password(prop) -> bool:
    if isinstance(prop, str):
        return re.fullmatch(r'[\w\W]{3,64}', prop)
    return False


def sessionId(session_id) -> bool:
    if isinstance(session_id, str):
        return bool(re.fullmatch(r'[0-9a-z]{64}', session_id))
    return False


def price(price) -> bool:
    if isinstance(price, str):
        return re.fullmatch(r'[0-9 .,]{1,16}', price)
    if isinstance(price, int):
        return 1 <= len(str(price)) <= 6
    if isinstance(price, float):
        return 1 <= len(str(price)) <= 9
    return False


def order(order) -> bool:
    if isinstance(order, str):
        return re.fullmatch(r'[0-9]{1,4}', order)
    if isinstance(order, int):
        return 1 <= len(str(order)) <= 4
    return False


def orderDirection(order) -> bool:
    if isinstance(order, str):
        return order.lower() in ('asc', 'desc')
    return False


def active(active) -> bool:
    if isinstance(active, str):
        return active.lower() in ('y', 'n')
    return False


def tableName(name) -> bool:
    if isinstance(name, str):
        pattern = r'[0-9a-zA-Z_]{1,64}'
        return bool(re.fullmatch(pattern, name))
    return False


# Menu

def menuID(menu_id) -> bool:
    if isinstance(menu_id, str):
        pattern = r'[0-9]{1,4}'
        return bool(re.fullmatch(pattern, menu_id))
    if isinstance(menu_id, int):
        return 1 <= len(str(menu_id)) <= 4
    return False


def menuAlias(alias):
    if isinstance(alias, str):
        pattern = r'[a-z_-]{1,64}'
        return re.fullmatch(pattern, alias)
    return False


def menuItemID(item_id) -> bool:
    if isinstance(item_id, str):
        pattern = r'[0-9]{1,4}'
        return bool(re.fullmatch(pattern, item_id))
    if isinstance(item_id, int):
        return 1 <= len(str(item_id)) <= 4
    return False


def menuName(name) -> bool:
    if isinstance(name, str):
        return re.fullmatch(r'\w{1,32}', name)
    return False


def menuItemName(name) -> bool:
    if isinstance(name, str):
        return re.fullmatch(r'[0-9A-Za-zА-Яа-яЯєЄіІїЇёЁҐґ _-]{1,64}', name)
    return False


def menuItemLink(link) -> bool:
    if isinstance(link, str):
        return bool(re.fullmatch(r'[\w:./]{1,128}', link))
    return False


# Currency

def currencyCode(code) -> bool:
    if isinstance(code, str):
        return re.fullmatch(r'[a-zA-Z]{3}', code)
    return False


def currencyName(name) -> bool:
    if isinstance(name, str):
        return re.fullmatch(r'[0-9A-Za-zА-Яа-яЯєЄіІїЇёЁҐґ _-]{1,64}', name)
    return False


def currencySymbol(symbol) -> bool:
    if isinstance(symbol, str):
        return re.fullmatch(r'.{1,8}', symbol)
    return False


# User

def userID(user_id) -> bool:
    if isinstance(user_id, str):
        return bool(re.fullmatch(r'[0-9]{1,8}', user_id))
    if isinstance(user_id, int):
        return 1 <= len(str(user_id)) <= 8
    return False


def usersGroupID(users_group_id) -> bool:
    if isinstance(users_group_id, str):
        return bool(re.fullmatch(r'[0-9]{1}', users_group_id))
    if isinstance(users_group_id, int):
        return len(str(users_group_id)) == 1
    return False


def userName(name) -> bool:
    if isinstance(name, str):
        return re.fullmatch(r'\w{1,64}', name)
    return False


def usersGroupName(name) -> bool:
    if isinstance(name, str):
        return re.fullmatch(r'\w{1,64}', name)
    return False


# Category

def categoryID(category_id) -> bool:
    if isinstance(category_id, str):
        return bool(re.fullmatch(r'[0-9]{1,8}', category_id))
    if isinstance(category_id, int):
        return 1 <= len(str(category_id)) <= 8
    return False


def categoryName(name) -> bool:
    if isinstance(name, str):
        return re.fullmatch(r'\w{1,64}', name)
    return False


# Product

def productID(product_id) -> bool:
    if isinstance(product_id, str):
        return bool(re.fullmatch(r'[0-9]{1,8}', product_id))
    if isinstance(product_id, int):
        return 1 <= len(str(product_id)) <= 8
    return False


def productModel(model) -> bool:
    if isinstance(model, str):
        return re.fullmatch(r'[0-9A-Za-zА-Яа-яЯєЄіІїЇёЁҐґ _-]{1,64}', model)
    return False


def productName(name) -> bool:
    if isinstance(name, str):
        return re.fullmatch(r'[0-9A-Za-zА-Яа-яЯєЄіІїЇёЁҐґ _-]{1,128}', name)
    return False


def productDescrioption(description) -> bool:
    if isinstance(description, str):
        pattern = r'[0-9A-Za-zА-Яа-яЯєЄіІїЇёЁҐґ _-]{1,256}'
        return re.fullmatch(pattern, description)
    return False


# Characteristic

def characteristicID(characteristic_id) -> bool:
    if isinstance(characteristic_id, str):
        return bool(re.fullmatch(r'[0-9]{1,8}', characteristic_id))
    if isinstance(characteristic_id, int):
        return 1 <= len(str(characteristic_id)) <= 8
    return False


def characteristicName(name) -> bool:
    if isinstance(name, str):
        return re.fullmatch(r'[0-9A-Za-zА-Яа-яЯєЄіІїЇёЁҐґ _-]{1,32}', name)
    return False
