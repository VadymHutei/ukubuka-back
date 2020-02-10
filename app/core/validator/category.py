import re


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