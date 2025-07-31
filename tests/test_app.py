from http import HTTPStatus

from fastapi.testclient import TestClient

from fastapi_zero.app import app

client = TestClient(app)


def test_root_give_return_ok_and_hello_whordl():
    response = client.get("/")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Hello World!'}


def test_create_user():
    response = client.post(
        "/users",
        json={
            "username": "test_user",
            "email": "marcos@email.com",
            "password": "initial123",
        })

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
            "username": "test_user",
            "email": "marcos@email.com",
        }
