from datetime import datetime
from typing import Optional

from pydantic import Field, BaseModel

from ..payloads.user import User


class Post(BaseModel):
    post_id: int
    content: Optional[str] = Field(max_length=777)
    reposted: bool
    quoted: bool
    created_at: datetime
    user: 'User'
    related_post: Optional['Post']

    class Config:
        extra: str = "ignore"


class Posts(BaseModel):
    posts: list[Post]


class PublishPostBody(BaseModel):
    user_id: int
    content: str = Field(max_length=777)


class RepostPostBody(BaseModel):
    user_id: int
    post_id: int


class QuotePostBody(BaseModel):
    user_id: int
    post_id: int
    content: str = Field(max_length=777)
