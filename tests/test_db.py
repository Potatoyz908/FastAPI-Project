from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):
    user = User(
        username='batatinha123', email='test@test.com', password='password'
    )
    session.add(user)
    session.commit()
    result = session.scalar(select(User).where(User.email == 'test@test.com'))

    assert result.username == 'batatinha123'
