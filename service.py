import model


def get_user_by_id(id_in: int) -> list:
    return model.read_user(id_in)


def get_user_by_name(name_in: str) -> list:
    return model.get_user_by_name(name_in)


def get_all_user() -> list:
    return model.get_all_users()


def get_exams_by_user_id(id_in: int) -> list:
    return model.get_exams_by_user_id(id_in)


def get_all_doctors() -> list:
    return model.get_all_doctors()


def get_all_procedures() -> list:
    return model.get_all_procedures()
