from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from fast_zero.models import User, table_registry


def test_create_user(client):
    engine = create_engine('sqlite:///:memory:')

    table_registry.metadata.create_all(engine)

    with Session(engine) as session:
        user = User(
            username='batatinha123', email='test@test.com', password='password'
        )
        session.add(user)
        session.commit()
        result = session.scalar(
            select(User).where(User.email == 'test@test.com')
        )

    assert result.username == 'batatinha123'
