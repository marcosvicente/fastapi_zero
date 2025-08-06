from sqlalchemy import select

from fastapi_zero.models import User

def test_create_user():
    new_user = User(username="test", email="marcos@email.com", password="initial123")

    session.add(new_user)
    session.commit()

    user = session.scalar(select(User).where(User.username == 'alice'))

    assert user.username == 'alice'
    assert user.email == "marcos@email.com"
    assert user.password == "initial123"