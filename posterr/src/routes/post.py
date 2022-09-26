from datetime import date

from fastapi import APIRouter, Query

from ..payloads.post import PublishPostBody, Post, RepostPostBody, QuotePostBody, Posts
from ..modules.post import create_post, repost_post, quote_post, list_posts

router = APIRouter(prefix="/post")


@router.post("/list", response_model=Posts)
def _list_posts(user_id: int = None, publish_at: date = None, page: int = 0, limit: int = Query(10, ge=0, le=10)):
    return {"posts": list_posts(user_id, publish_at, page, limit)}


@router.post("/publish", response_model=Post)
def _create_post(body: PublishPostBody):
    return create_post(body.user_id, body.content)


@router.post("/repost", response_model=Post)
def _repost_post(body: RepostPostBody):
    return repost_post(body.user_id, body.post_id)


@router.post("/quote", response_model=Post)
def _quote_post(body: QuotePostBody):
    return quote_post(body.user_id, body.post_id, body.content)
