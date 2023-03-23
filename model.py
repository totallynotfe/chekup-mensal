import datetime

import OrmConfig


def createUser(name: str, email: str):
    newUser = OrmConfig.User(name, email)
    OrmConfig.session.add(newUser)
    OrmConfig.session.commit()


def updateUser(name: str = '', fullname: str = ''):
    return


def deleteUser(id: int):
    return


def readUser(name: str = '', fullname: str = ''):
    return


def readAllUsers():
    return


def createExam(date: datetime):
    return
