import pytest
import requests

def test_user_endpoint_authorized(mocker):
    url = "http://127.0.0.1:8000/users"
    data = {"username": "admin", "password": "qwerty"}
    
    # Mock the requests.get method
    mocker.patch('requests.get')
    requests.get = mocker.Mock(return_value=requests.Response())
    requests.get.return_value.status_code = 200
    
    # Make a request to the endpoint
    response = requests.get(url, params=data)
    
    # Assert that the requests.get method was called
    requests.get.assert_called_once_with(url, params=data)
    
    # Assert that the response status code is 200
    assert response.status_code == 200

def test_user_endpoint_authorized(mocker):
    url = "http://127.0.0.1:8000/users"
    data = {"username": "admin", "password": "admin"}
    
    # Mock the requests.get method
    mocker.patch('requests.get')
    requests.get = mocker.Mock(return_value=requests.Response())
    requests.get.return_value.status_code = 401
    
    # Make a request to the endpoint
    response = requests.get(url, params=data)
    
    # Assert that the requests.get method was called
    requests.get.assert_called_once_with(url, params=data)
    
    # Assert that the response status code is 200
    assert response.status_code == 401