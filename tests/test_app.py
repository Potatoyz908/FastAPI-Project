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


def test_get_user___exercicio(client):
    response = client.get('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'batatinha123',
        'email': 'test@test.com',
        'id': 1,
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


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'id': 1,
            'username': 'TUBALAO',
            'email': 'tubalao@test.com',
            'password': '123',
        },
    )
    assert response.json() == {
        'id': 1,
        'username': 'TUBALAO',
        'email': 'tubalao@test.com',
    }


def test_update_user_should_return_not_found__exercicio(client):
    response = client.put(
        '/users/666',
        json={
            'username': 'bob',
            'email': 'bob@example.com',
            'password': 'mynewpassword',
        },
    )
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.json() == {'message': 'User deleted successfully'}


def test_delete_user_should_return_not_found__exercicio(client):
    response = client.delete('/users/666')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}
