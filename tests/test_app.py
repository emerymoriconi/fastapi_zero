from http import HTTPStatus


def test_root_deve_retornar_ola_mundo(client):
    # act
    response = client.get('/')

    # assert
    assert response.json() == {'message': 'Olá mundo!'}
    assert response.status_code == HTTPStatus.OK
