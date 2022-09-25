from datetime import datetime

from sqlalchemy import extract
from starlette.exceptions import HTTPException
from starlette.status import HTTP_400_BAD_REQUEST

from ..database.client import DatabaseClient
from ..models import User, Post

DAILY_POST_LIMIT = 5


def count_daily_published_post(user_id: int, *, connection: DatabaseClient = None) -> int:
    today = datetime.today()
    return connection.query(Post).filter(
        Post.USER_ID == user_id,
        extract('month', Post.CREATED_AT) >= today.month,
        extract('year', Post.CREATED_AT) >= today.year,
        extract('day', Post.CREATED_AT) >= today.day
    ).count()


def create_post(user_id: int, content: str, *, connection: DatabaseClient = None) -> dict:
    with DatabaseClient(connection=connection) as connection:
        user = User.search(connection, user_id)
        if not user:
            raise HTTPException(HTTP_400_BAD_REQUEST, f"user with id {user_id} do not exist")

        if count_daily_published_post(user_id, connection=connection) >= DAILY_POST_LIMIT:
            raise HTTPException(HTTP_400_BAD_REQUEST, f"user with id {user_id} reached the publish limit today")

        post = Post(USER_ID=user_id, CONTENT=content)
        connection.add(post)
        connection.commit()

        return post.to_dict()
