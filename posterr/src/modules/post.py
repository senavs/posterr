import logging
from datetime import datetime

from sqlalchemy import extract
from starlette.exceptions import HTTPException
from starlette.status import HTTP_400_BAD_REQUEST

from .user import search_user_or_404
from ..database.client import DatabaseClient
from ..models import Post

DAILY_POST_LIMIT = 5


def count_daily_published_post(user_id: int, *, connection: DatabaseClient = None) -> int:
    today = datetime.today()
    return connection.query(Post).filter(
        Post.USER_ID == user_id,
        extract('month', Post.CREATED_AT) >= today.month,
        extract('year', Post.CREATED_AT) >= today.year,
        extract('day', Post.CREATED_AT) >= today.day
    ).count()


def search_post_or_404(post_id: int, *, connection: DatabaseClient = None) -> Post:
    post = Post.search(connection, post_id)
    if not post:
        raise HTTPException(HTTP_400_BAD_REQUEST, f"post with id {post_id} do not exist")

    return post


def verify_daily_post_limit(user_id: int, *, connection: DatabaseClient = None):
    with DatabaseClient(connection=connection) as connection:
        if count_daily_published_post(user_id, connection=connection) >= DAILY_POST_LIMIT:
            raise HTTPException(HTTP_400_BAD_REQUEST, f"user with id {user_id} reached the publish limit today")


def create_post(user_id: int, content: str, *, connection: DatabaseClient = None) -> dict:
    with DatabaseClient(connection=connection) as connection:
        search_user_or_404(user_id, connection=connection)

        verify_daily_post_limit(user_id)

        post = Post(USER_ID=user_id, CONTENT=content)
        connection.add(post)
        connection.commit()

        return post.to_dict()


def repost_post(user_id: int, post_id: int, *, connection: DatabaseClient = None) -> dict:
    with DatabaseClient(connection=connection) as connection:
        search_user_or_404(user_id, connection=connection)

        verify_daily_post_limit(user_id, connection=connection)

        original_post = search_post_or_404(post_id, connection=connection)

        if original_post.REPOSTED:
            raise HTTPException(HTTP_400_BAD_REQUEST, f"you cannot repost a reposted post. try to repost the original one")

        post = Post(USER_ID=user_id, REPOSTED=True, RELATED_POST_ID=post_id)
        connection.add(post)
        connection.commit()

        return post.to_dict()


def quote_post(user_id: int, post_id: int, content: str, *, connection: DatabaseClient = None) -> dict:
    with DatabaseClient(connection=connection) as connection:
        search_user_or_404(user_id, connection=connection)

        verify_daily_post_limit(user_id, connection=connection)

        original_post = search_post_or_404(post_id, connection=connection)

        if original_post.QUOTED:
            raise HTTPException(HTTP_400_BAD_REQUEST, f"you cannot quote a quoted post. try to quote the original one")

        post = Post(USER_ID=user_id, CONTENT=content, QUOTED=True, RELATED_POST_ID=post_id)
        connection.add(post)
        connection.commit()

        return post.to_dict()
