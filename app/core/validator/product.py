import re


def productID(product_id):
    if isinstance(product_id, str):
        return bool(re.fullmatch(r'[0-9]{1,8}', product_id))
    if isinstance(product_id, int):
        return 1 <= len(str(product_id)) <= 8
    return False


def productModel(model):
    if isinstance(model, str):
        return re.fullmatch(r'[0-9A-Za-zА-Яа-яЯєЄіІїЇёЁҐґ _-]{1,64}', model)
    return False


def productName(name):
    if isinstance(name, str):
        return re.fullmatch(r'[0-9A-Za-zА-Яа-яЯєЄіІїЇёЁҐґ _-]{1,128}', name)
    return False


def productDescrioption(description):
    if isinstance(description, str):
        pattern = r'[0-9A-Za-zА-Яа-яЯєЄіІїЇёЁҐґ _-]{1,256}'
        return re.fullmatch(pattern, description)
    return False
