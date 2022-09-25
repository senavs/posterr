from datetime import datetime
from typing import Optional

from pydantic import BaseSettings, Field

from ..payloads.user import User


class Post(BaseSettings):
    post_id: int
    content: str = Field(max_length=777)
    reposted: bool
    quoted: bool
    created_at: datetime
    user: 'User'
    related_post: Optional['Post']

    class Config:
        extra: str = "ignore"


class PublishPostBody(BaseSettings):
    user_id: int
    content: str = Field(max_length=777)
