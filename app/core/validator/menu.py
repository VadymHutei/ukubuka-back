import re


def menuID(menu_id):
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


def menuItemID(item_id):
    if isinstance(item_id, str):
        pattern = r'[0-9]{1,4}'
        return bool(re.fullmatch(pattern, item_id))
    if isinstance(item_id, int):
        return 1 <= len(str(item_id)) <= 4
    return False


def menuName(name):
    if isinstance(name, str):
        return re.fullmatch(r'\w{1,32}', name)
    return False


def menuItemName(name):
    if isinstance(name, str):
        return re.fullmatch(r'[0-9A-Za-zА-Яа-яЯєЄіІїЇёЁҐґ _-]{1,64}', name)
    return False


def menuItemLink(link):
    if isinstance(link, str):
        return bool(re.fullmatch(r'[\w:./]{1,128}', link))
    return False
