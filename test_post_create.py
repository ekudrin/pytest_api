import requests
from faker import Faker

import base_test
from base_test import BASE_URL

fake = Faker()


def test_post_create_response_body():
    name = fake.name()
    job = fake.job()
    request_body = base_test.generate_user(name, job)

    response = post_update(request_body)
    assert response.status_code == 201, "Status code is not valid"

    data = response.json()
    assert data['name'] == name, "Invalid name value"
    assert data['job'] == job, "Invalid job value"


def post_update(request_body):
    return requests.post(BASE_URL + "/api/users", json=request_body)
