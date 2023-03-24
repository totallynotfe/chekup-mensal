import datetime
from sqlalchemy import ForeignKey, MetaData, String, DateTime, create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


metadata_obj = MetaData()


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "user_account"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(30))
    cpf: Mapped[str] = mapped_column(String)
    address: Mapped[str] = mapped_column(String)
    birth: Mapped[DateTime] = mapped_column(DateTime)
    first: Mapped[DateTime] = mapped_column(DateTime)
    last: Mapped[DateTime] = mapped_column(DateTime)

    def __init__(self, name: str, cpf: str, address: str, birth: datetime, first: datetime, last: datetime):
        self.name = name
        self.cpf = cpf
        self.address = address
        self.birth = birth
        self.first = first
        self.last = last

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r})"


class Exams(Base):
    __tablename__ = "user_exams"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    value: Mapped[float] = mapped_column(float)
    procedure_id: Mapped[int] = mapped_column(ForeignKey("procedures.id"))
    sessions: Mapped[int] = mapped_column(int)
    date: Mapped[DateTime] = mapped_column(DateTime)
    user_id: Mapped[int] = mapped_column(ForeignKey("user_account.id"))

    def __init__(self, value: float, procedure_id: int, sessions: int, date: datetime, user_id: int):
        self.value = value
        self.procedure_id = procedure_id
        self.sessions = sessions
        self.date = date
        self.user_id = user_id

    def __repr__(self) -> str:
        return f"Exam()"


class Procedure(Base):
    __tablename__ = "procedures"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(40))

    def __init__(self, name):
        self.name = name


engine = create_engine("sqlite://", echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()
