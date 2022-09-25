from fastapi import APIRouter

from ..payloads.post import PublishPostBody, Post
from ..modules.post import create_post

router = APIRouter(prefix="/post")


@router.post("/publish", response_model=Post)
def publish_post(body: PublishPostBody):
    return create_post(body.user_id, body.content)
