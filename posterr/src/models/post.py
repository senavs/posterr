from typing import Optional

from sqlalchemy import Column, INTEGER, ForeignKey, func, BOOLEAN, VARCHAR, TIMESTAMP
from sqlalchemy.orm import relationship, backref

from ..database import DeclarativeBase
from ..models.base import BaseModel


class Post(DeclarativeBase, BaseModel):
    __tablename__ = "POST"

    POST_ID = Column(INTEGER, autoincrement=True, nullable=False, primary_key=True, unique=True)
    USER_ID = Column(INTEGER, ForeignKey("USER.USER_ID", ondelete="CASCADE"), nullable=False, unique=False)
    CONTENT = Column(VARCHAR(777), nullable=True, unique=False)
    CREATED_AT = Column(TIMESTAMP, nullable=False, unique=False, default=func.now(), server_default=func.now())
    REPOSTED = Column(BOOLEAN, nullable=False, unique=False, default=False, server_default="false")
    QUOTED = Column(BOOLEAN, nullable=False, unique=False, default=False, server_default="false")
    RELATED_POST_ID = Column(INTEGER, ForeignKey("POST.POST_ID", ondelete="CASCADE"), nullable=True, unique=False)

    user = relationship("User", backref=backref("posts", cascade="all,delete", lazy="dynamic"))
    related_post = relationship("Post", remote_side=[POST_ID])

    def to_dict(self, *, exclude: Optional[list] = None, **include) -> dict:
        post = super().to_dict(exclude=exclude, **include)

        if post.get('user_id'):
            post.update(user=self.user.to_dict())
            post.pop('user_id')
        if post.get('related_post_id'):
            post.update(related_post=self.related_post.to_dict())
            post.pop('related_post_id')

        return post
