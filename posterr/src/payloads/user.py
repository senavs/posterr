from pydantic import BaseSettings


class User(BaseSettings):
    user_id: int
    username: str
