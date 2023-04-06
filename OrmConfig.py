import datetime
import pymysql
from sqlalchemy import ForeignKey, MetaData, String, DateTime, create_engine, Column, Integer, Float
from sqlalchemy.orm import DeclarativeBase, sessionmaker


metadata_obj = MetaData()


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "user_register"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String(30))
    cpf = Column("cpf", String(11))
    address = Column("address", String(50))
    birth = Column("birth", DateTime)
    first = Column("first", DateTime)
    last = Column("last", DateTime)

    def __init__(self, name: str, cpf: str, address: str, birth: datetime, first: datetime, last: datetime):
        self.name = name
        self.cpf = cpf
        self.address = address
        self.birth = birth
        self.first = first
        self.last = last

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, cpf={self.cpf!r}, address={self.address!r}, birth={self.birth!r}, first={self.first!r}, last={self.last!r})"


class Doctor(Base):
    __tablename__ = "doctor_register"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    crm = Column("crm", Integer)
    name = Column("name", String(30))
    cpf = Column("cpf", String(11))
    address = Column("address", String(50))
    birth = Column("birth", DateTime)

    def __init__(self, crm: int, name: str, cpf: str, address: str, birth: datetime, first: datetime, last: datetime):
        self.crm = crm
        self.name = name
        self.cpf = cpf
        self.address = address
        self.birth = birth
        self.first = first
        self.last = last

    def __repr__(self) -> str:
        return f"Doctor(id={self.id!r}, crm={self.crm!r}, name={self.name!r}, cpf={self.cpf!r}, address={self.address!r}, birth={self.birth!r}, first={self.first!r}, last={self.last!r})"


class Exams(Base):
    __tablename__ = "user_exams"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    value = Column("value", Float)
    procedure_id = Column("procedure_id", ForeignKey("procedures.id"))
    sessions = Column("sessions", Integer)
    date = Column("date", DateTime)
    user_id = Column("user_id", ForeignKey("user_register.id"))
    doctor_id = Column("doctor_id", ForeignKey("doctor_register.id"))

    def __init__(self, value: float, procedure_id: int, sessions: int, date: datetime, user_id: int, doctor_id: int):
        self.value = value
        self.procedure_id = procedure_id
        self.sessions = sessions
        self.date = date
        self.user_id = user_id
        self.doctor_id = doctor_id

    def __repr__(self) -> str:
        return f"Exam(id={self.id!r}, value={self.value!r}, procedure_id={self.procedure_id!r}, sessions={self.sessions!r}, date(s)={self.date!r}, user_id = {self.user_id}, doctor_id={self.doctor_id!r})"


class Procedure(Base):
    __tablename__ = "procedures"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String(40))

    def __init__(self, name):
        self.name = name


engine = create_engine("mysql+pymysql://root@localhost/controle_dentista", echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()
