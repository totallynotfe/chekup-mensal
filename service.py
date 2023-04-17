import model


def get_user_by_id(id_in: int) -> list:
    return model.read_user(id_in)


def get_user_by_name(name_in: str) -> list:
    return model.get_user_by_name(name_in)


def get_all_user() -> list:
    return model.get_all_users()
