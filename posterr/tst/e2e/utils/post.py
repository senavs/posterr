from requests import Response
from starlette.testclient import TestClient


def send_publish_request(client: TestClient, user_id: int, content: str) -> Response:
    return client.post("/post/publish", json={"user_id": user_id, "content": content})


def send_repost_request(client: TestClient, user_id: int, post_id: int) -> Response:
    return client.post("/post/repost", json={"user_id": user_id, "post_id": post_id})


def send_quote_request(client: TestClient, user_id: int, post_id: int, content: str) -> Response:
    return client.post("/post/quote", json={"user_id": user_id, "post_id": post_id, "content": content})
