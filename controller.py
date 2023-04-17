import service


def get_user_by_id(id_in: int):
    user: list = service.get_user_by_id(id_in)
    return user[0]


def get_user_by_name(name_in: str):
    user: list = service.get_user_by_name(name_in)
    return user


def get_all_user():
    return service.get_all_user()
