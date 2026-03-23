import pytest
from utils.apis import APIS

@pytest.fixture(scope='module')
def api():
    return APIS()

def test_get_user_validation(api):
    response = api.get('users')
    print(response.json())
    assert response.status_code ==200
    assert len(response.json())>0
