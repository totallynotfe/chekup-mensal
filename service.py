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


def create_exam(value, date, doctor_id, procedure_id, user_id):
    model.create_exam(value, procedure_id, 1, date, user_id, doctor_id)


def get_exam_by_id(id_in) -> list:
    return model.read_exam(id_in)


def update_exam(data):
    model.update_exam(data)


def delete_exam(id_in):
    model.delete_exam(id_in)
