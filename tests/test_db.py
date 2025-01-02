from fast_zero.models import User


def test_create_user(client):
    user = User(
        username='batatinha123', email='test@test.com', password='password'
    )
    assert user.username == 'batatinha123'
