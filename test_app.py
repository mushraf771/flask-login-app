import pytest
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


# def test_login_page_loads(client):
#     # response = client.get('')
#     assert response.status_code == 200
#     assert b'<title>Login</title>' in response.data


def test_login_post(client):
    response = client.post('/', data={'username': 'testuser', 'password': 'testpass'})
    assert response.status_code == 200
    assert b'Logged in as testuser' in response.data
