from starlette.exceptions import HTTPException
from starlette.status import HTTP_400_BAD_REQUEST

from ..database.client import DatabaseClient
from ..models import User, Post


def create_post(user_id: int, content: str) -> dict:
    with DatabaseClient() as connection:
        user = User.search(connection, user_id)
        if not user:
            raise HTTPException(HTTP_400_BAD_REQUEST, f"user with id {user_id} do not exist")

        post = Post(USER_ID=user_id, CONTENT=content)
        connection.add(post)
        connection.commit()

        return post.to_dict()
