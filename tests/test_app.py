from http import HTTPStatus


def test_read_root_deve_retornar_ok_e_ola_mundo(client):
    response = client.get('/')  # Act (ação)

    assert response.status_code == HTTPStatus.OK  # Assert (verificação)
    assert response.json() == {'message': 'Hello, World!'}  # Assert


def test_create_user(client):
    response = client.post(
        '/users',
        json={
            'username': 'batatinha123',
            'password': 'password',
            'email': 'test@test.com',
        },
    )

    # validar o status code da resposta
    assert response.status_code == HTTPStatus.CREATED
    # validar UserPublic
    assert response.json() == {
        'id': 1,
        'username': 'batatinha123',
        'email': 'test@test.com',
    }


def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'id': 1,
                'username': 'batatinha123',
                'email': 'test@test.com',
            }
        ]
    }
