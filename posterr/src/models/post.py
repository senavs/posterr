from sqlalchemy import Column, INTEGER, ForeignKey, func, BOOLEAN, VARCHAR, TIMESTAMP
from sqlalchemy.orm import relationship, backref

from ..database import DeclarativeBase
from ..models.base import BaseModel


class Post(DeclarativeBase, BaseModel):
    __tablename__ = "POST"

    POST_ID = Column(INTEGER, autoincrement=True, nullable=False, primary_key=True, unique=True)
    USER_ID = Column(INTEGER, ForeignKey("USER.USER_ID", ondelete="CASCADE"), nullable=False, unique=False)
    CONTENT = Column(VARCHAR(777), nullable=False, unique=False)
    CREATED_AT = Column(TIMESTAMP, nullable=False, unique=False, default=func.now(), server_default=func.now())
    REPOSTED = Column(BOOLEAN, nullable=False, unique=False, default="0", server_default="0")
    QUOTED = Column(BOOLEAN, nullable=False, unique=False, default="0", server_default="0")
    RELATED_POST_ID = Column(INTEGER, ForeignKey("POST.POST_ID", ondelete="CASCADE"), nullable=True, unique=False)

    user = relationship("User", backref=backref("posts", cascade="all,delete", lazy="dynamic"))
    related_post = relationship("Post")
