import service


def get_user_by_id(id_in: int):
    user: list = service.get_user_by_id(id_in)
    return user[0]


def get_user_by_name(name_in: str):
    user: list = service.get_user_by_name(name_in)
    return user


def get_all_user():
    return service.get_all_user()


def get_exams_by_user_id(id_in) -> list:
    return service.get_exams_by_user_id(id_in)


def get_all_doctors() -> list:
    return service.get_all_doctors()


def get_all_procedures() -> list:
    return service.get_all_procedures()
