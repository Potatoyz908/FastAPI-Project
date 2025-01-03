from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):
    new_user = User(
        username='batatinha123', email='test@test.com', password='password'
    )
    session.add(new_user)
    session.commit()
    user = session.scalar(select(User).where(User.email == 'test@test.com'))

    assert user.username == 'batatinha123'
