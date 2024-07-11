import random

import requests
from faker import Faker

import base_test
from base_test import BASE_URL

fake = Faker()


def test_delete_response_body():
    user_id = random.randint(1, 12)
    name = fake.name()
    job = fake.job()
    request_body = base_test.generate_user(name, job)
    response = delete_user(request_body, user_id)
    assert response.status_code == 204, "Invalid status code"


def delete_user(request_body, user_id):
    return requests.delete(BASE_URL + f"/api/users/{user_id}", json=request_body)
