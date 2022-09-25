from starlette.exceptions import HTTPException
from starlette.status import HTTP_400_BAD_REQUEST

from ..database.client import DatabaseClient
from ..models import User


def search_user_or_404(user_id: int, *, connection: DatabaseClient = None) -> User:
    user = User.search(connection, user_id)
    if not user:
        raise HTTPException(HTTP_400_BAD_REQUEST, f"user with id {user_id} do not exist")

    return user
