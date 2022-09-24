from sqlalchemy import Column, INTEGER, VARCHAR

from ..database import DeclarativeBase
from ..models.base import BaseModel


class User(DeclarativeBase, BaseModel):
    __tablename__ = 'USER'

    USER_ID = Column(INTEGER, autoincrement=True, nullable=False, primary_key=True, unique=True)
    USERNAME = Column(VARCHAR(14), nullable=False, unique=True, index=True)
