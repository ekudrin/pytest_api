import requests
from faker import Faker

import base_test
from base_test import BASE_URL

fake = Faker()


def test_post_register_response_body():
    email = "eve.holt@reqres.in"
    password = "pistol"
    request_body = base_test.generate_register_entity(email, password)

    response = post_register(request_body)
    assert response.status_code == 200, "Status code is not valid"

    data = response.json()
    assert data['id'] is not None
    assert data['token'] is not None


def test_post_register_invalid_user():
    email = fake.email()
    password = fake.password()
    request_body = base_test.generate_register_entity(email, password)

    response = post_register(request_body)
    assert response.status_code == 400, "Status code is not valid"

    data = response.json()
    assert data['error'] == "Note: Only defined users succeed registration", "Invalid error message"


def test_post_register_request_without_password():
    request_body = {
        "email": "eve.holt@reqres.in"
    }

    response = post_register(request_body)
    assert response.status_code == 400, "Status code is not valid"

    data = response.json()
    assert data['error'] == "Missing password", "Invalid error message"


def test_post_register_request_without_email():
    request_body = {
        "password": "pistol"
    }

    response = post_register(request_body)
    assert response.status_code == 400, "Status code is not valid"

    data = response.json()
    assert data['error'] == "Missing email or username", "Invalid error message"


def post_register(request_body):
    return requests.post(BASE_URL + "/api/register", json=request_body)
