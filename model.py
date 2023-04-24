import datetime

import OrmConfig
from sqlalchemy import update


def create_user(name: str, address: str, birth: datetime, cpf: str, first: datetime, last: datetime):
    new_user = OrmConfig.User(name, address, birth, cpf, first, last)
    OrmConfig.session.add(new_user)
    OrmConfig.session.commit()


def update_user(data):
    user = OrmConfig.session.query(OrmConfig.User).filter(OrmConfig.User.id == data.id)
    for k, v in data.items():
        user[k] = v
    OrmConfig.session.commit()


def delete_user(id_in: int):
    user = OrmConfig.session.query(OrmConfig.User).filter(OrmConfig.User.id == id_in)
    OrmConfig.session.delete(user[0])
    OrmConfig.session.commit()


def read_user(id_in: int):
    user = OrmConfig.session.query(OrmConfig.User).filter(OrmConfig.User.id == id_in)
    return user


def get_user_by_name(name_in: str):
    user = OrmConfig.session.query(OrmConfig.User).filter(OrmConfig.User.name.like(f"%{name_in}%"))
    return user


def get_all_users():
    return OrmConfig.session.query(OrmConfig.User).all()


def create_doctor(crm: int, name: str, address: str, birth: datetime, cpf: str, first: datetime, last: datetime):
    new_doctor = OrmConfig.Doctor(crm, name, address, birth, cpf, first, last)
    OrmConfig.session.add(new_doctor)
    OrmConfig.session.commit()


def update_doctor(data):
    doctor = OrmConfig.session.query(OrmConfig.Doctor).filter(OrmConfig.Doctor.id == data.id)
    for k, v in data.items():
        doctor[k] = v
    OrmConfig.session.commit()


def delete_doctor(id_in: int):
    doctor = OrmConfig.session.query(OrmConfig.Doctor).filter(OrmConfig.Doctor.id == id_in)
    OrmConfig.session.delete(doctor[0])
    OrmConfig.session.commit()


def read_doctor(id_in: int):
    doctor = OrmConfig.session.query(OrmConfig.Doctor).filter(OrmConfig.Doctor.id == id_in)
    return doctor


def get_all_doctors():
    return OrmConfig.session.query(OrmConfig.Doctor).all()


def create_procedure(name_in: str):
    new_procedure = OrmConfig.Procedure(name_in)
    OrmConfig.session.add(new_procedure)


def delete_procedure(id_in: int):
    procedure = OrmConfig.session.query(OrmConfig.Procedure).filter(OrmConfig.Procedure.id == id_in)
    OrmConfig.session.delete(procedure[0])
    OrmConfig.session.commit()


def get_all_procedures():
    return OrmConfig.session.query(OrmConfig.Procedure).all()


def create_exam(value_in: float, procedure_id_in: int, sessions_in: int, date_in: datetime, user_id_in: int,
                doctor_id_in: int):
    new_exam = OrmConfig.Exams(value_in, procedure_id_in, sessions_in, date_in, user_id_in, doctor_id_in)
    OrmConfig.session.add(new_exam)
    OrmConfig.session.commit()


def update_exam(data):
    smt = (update(OrmConfig.Exams).where(OrmConfig.Exams.id == data['id']).values(data))
    OrmConfig.session.execute(smt)
    OrmConfig.session.commit()


def delete_exam(id_in: int):
    exam = OrmConfig.session.query(OrmConfig.Exams).filter(OrmConfig.Exams.id == id_in)
    OrmConfig.session.delete(exam[0])
    OrmConfig.session.commit()


def read_exam(id_in: int):
    exam = OrmConfig.session.query(OrmConfig.Exams).filter(OrmConfig.Exams.id == id_in)
    return exam


def get_exams_by_user_id(id_in: int):
    exams = OrmConfig.session.query(OrmConfig.Exams).filter(OrmConfig.Exams.user_id == id_in)
    return exams
