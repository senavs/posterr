from datetime import datetime
from typing import Optional

from pydantic import BaseSettings, Field

from ..payloads.user import User


class Post(BaseSettings):
    post_id: int
    content: Optional[str] = Field(max_length=777)
    reposted: bool
    quoted: bool
    created_at: datetime
    user: 'User'
    related_post: Optional['Post']

    class Config:
        extra: str = "ignore"


class Posts(BaseSettings):
    posts: list[Post]


class PublishPostBody(BaseSettings):
    user_id: int
    content: str = Field(max_length=777)


class RepostPostBody(BaseSettings):
    user_id: int
    post_id: int


class QuotePostBody(BaseSettings):
    user_id: int
    post_id: int
    content: str = Field(max_length=777)
