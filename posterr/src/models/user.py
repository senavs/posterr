from sqlalchemy import Column, INTEGER, VARCHAR, event, Table
from sqlalchemy.future import Connection

from ..database import DeclarativeBase
from ..models.base import BaseModel


class User(DeclarativeBase, BaseModel):
    __tablename__ = "USER"

    USER_ID = Column(INTEGER, autoincrement=True, nullable=False, primary_key=True, unique=True)
    USERNAME = Column(VARCHAR(14), nullable=False, unique=True, index=True)


@event.listens_for(User.__table__, "after_create")
def populate(target: Table, connection: Connection, **kwargs):
    users = [
        {"USER_ID": 1, "USERNAME": "senavs"}
    ]
    connection.execute(target.insert(), *users)
