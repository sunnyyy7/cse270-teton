import pytest
import requests
from requests.exceptions import HTTPError

@pytest.fixture
def mock_response_401(requests_mock):
    url = 'http://127.0.0.1:8000/users?username=admin&password=admin'
    requests_mock.get(url, status_code=401, text='Unauthorized')

@pytest.fixture
def mock_response_200(requests_mock):
    url = 'http://127.0.0.1:8000/users?username=admin&password=qwerty'
    requests_mock.get(url, status_code=200, text='')

@pytest.mark.integration
def test_empty_response_with_401(mock_response_401):
    url = 'http://127.0.0.1:8000/users?username=admin&password=admin'

    # Make the request
    response = requests.get(url)

    # Verify the response code is 401
    assert response.status_code == 401

    # Verify the response body
    assert response.text == 'Unauthorized'

@pytest.mark.integration
def test_empty_response_with_200(mock_response_200):
    url = 'http://127.0.0.1:8000/users?username=admin&password=qwerty'

    # Make the request
    response = requests.get(url)

    # Verify the response code is 200
    assert response.status_code == 200

    # Verify the response body is empty
    assert response.text == ''
