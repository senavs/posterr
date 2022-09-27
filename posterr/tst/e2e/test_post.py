from starlette.testclient import TestClient

from posterr.src import app
from posterr.tst.e2e.utils.post import send_publish_request, send_repost_request, send_quote_request

client = TestClient(app)

USER_ID = 1


def test_list_post_expecting_empty_list():
    # arrange

    # act
    response = client.get("/post/list")
    response_body = response.json()

    # assert
    assert response.status_code == 200
    assert response_body.get("posts") == []


def test_create_post_expecting_success():
    # arrange
    content = "hellow world"

    # act
    response = send_publish_request(client, USER_ID, content)
    response_body = response.json()

    # assert
    assert response.status_code == 200
    assert response_body.get("content") == content


def test_create_6_post_expecting_error():
    # arrange
    content = "hellow world"

    # act
    for _ in range(6):
        response = send_publish_request(client, USER_ID, content)
    response_body = response.json()

    # assert
    assert response.status_code == 400
    assert response_body.get("detail").endswith("reached the publish limit today")


def test_repost_expecting_success():
    # arrange
    content = "hellow world"
    send_publish_request(client, USER_ID, content)

    # act
    response = send_repost_request(client, USER_ID, 1)

    # assert
    assert response.status_code == 200


def test_repost_a_reposted_post_expecting_error():
    # arrange
    content = "hellow world"
    send_publish_request(client, USER_ID, content)
    send_repost_request(client, USER_ID, 1)

    # act
    response = send_repost_request(client, USER_ID, 2)
    response_body = response.json()

    # assert
    assert response.status_code == 400
    assert response_body.get("detail").startswith("you cannot repost a reposted post")


def test_quote_expecting_success():
    # arrange
    content = "hellow world"
    quoted_content = "quoted hello world"
    send_publish_request(client, USER_ID, content)

    # act
    response = send_quote_request(client, USER_ID, 1, quoted_content)

    # assert
    assert response.status_code == 200


def test_quote_a_quoted_post_expecting_error():
    # arrange
    content = "hellow world"
    quoted_content = "quoted hello world"
    send_publish_request(client, USER_ID, content)
    send_quote_request(client, USER_ID, 1, quoted_content)

    # act
    response = send_quote_request(client, USER_ID, 2, quoted_content)
    response_body = response.json()

    # assert
    assert response.status_code == 400
    assert response_body.get("detail").startswith("you cannot quote a quoted post")
