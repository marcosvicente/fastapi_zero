from http import HTTPStatus


def test_root_give_return_ok_and_hello_whordl(client):
    response = client.get("/")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Hello World!'}


def test_create_user(client):
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


def test_read_users(client):
    response = client.get("/users")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                "username": "test_user",
                "email": "marcos@email.com",
            }
        ]
    }


def test_update_user(client):
    response = client.put(
        "/users",
        json={
            "username": "test_user2",
            "email": "marcos@email.com",
            "password": "initial123",
        }
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                "username": "test_user2",
                "email": "marcos@email.com",
            }
        ]
    }