from starlette.testclient import TestClient

from posterr.src import app

client = TestClient(app)


def test_app_root_path():
    response = client.get("/")
    assert response.status_code == 404


def test_swagger():
    response = client.get("/docs")
    assert response.status_code == 200
