import re


def characteristicID(characteristic_id):
    if isinstance(characteristic_id, str):
        return bool(re.fullmatch(r'[0-9]{1,8}', characteristic_id))
    if isinstance(characteristic_id, int):
        return 1 <= len(str(characteristic_id)) <= 8
    return False


def characteristicName(name):
    if isinstance(name, str):
        return re.fullmatch(r'[0-9A-Za-zА-Яа-яЯєЄіІїЇёЁҐґ _-]{1,32}', name)
    return False
