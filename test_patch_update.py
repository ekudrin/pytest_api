import requests
from faker import Faker

import base_test
from base_test import BASE_URL

fake = Faker()


def test_patch_update_response_body():
    name = fake.name()
    job = fake.job()
    request_body = base_test.generate_user(name, job)
    response = patch_update(request_body)
    assert response.status_code == 200, "Invalid status code"

    data = response.json()
    assert data['name'] == name, "Invalid name value"
    assert data['job'] == job, "Invalid job value"


def patch_update(request_body):
    return requests.patch(BASE_URL + "/api/users/2", json=request_body)
