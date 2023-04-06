import datetime

import OrmConfig


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
    OrmConfig.session.delete(user)
    OrmConfig.session.commit()


def read_user(id_in: int):
    user = OrmConfig.session.query(OrmConfig.User).filter(OrmConfig.User.id == id_in)
    return user
