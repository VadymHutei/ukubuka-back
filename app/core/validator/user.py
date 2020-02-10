import re


def userID(user_id):
    if isinstance(user_id, str):
        return bool(re.fullmatch(r'[0-9]{1,8}', user_id))
    if isinstance(user_id, int):
        return 1 <= len(str(user_id)) <= 8
    return False


def usersGroupID(users_group_id):
    if isinstance(users_group_id, str):
        return bool(re.fullmatch(r'[0-9]{1}', users_group_id))
    if isinstance(users_group_id, int):
        return len(str(users_group_id)) == 1
    return False


def userName(name):
    if isinstance(name, str):
        return re.fullmatch(r'\w{1,64}', name)
    return False


def usersGroupName(name):
    if isinstance(name, str):
        return re.fullmatch(r'\w{1,64}', name)
    return False
