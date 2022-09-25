from fastapi import APIRouter

from ..payloads.post import PublishPostBody, Post, RepostPostBody, QuotePostBody
from ..modules.post import create_post, repost_post, quote_post

router = APIRouter(prefix="/post")


@router.post("/publish", response_model=Post)
def _create_post(body: PublishPostBody):
    return create_post(body.user_id, body.content)


@router.post("/repost", response_model=Post)
def _repost_post(body: RepostPostBody):
    return repost_post(body.user_id, body.post_id)


@router.post("/quote", response_model=Post)
def _quote_post(body: QuotePostBody):
    return quote_post(body.user_id, body.post_id, body.content)
