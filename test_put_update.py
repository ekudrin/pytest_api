import random

import requests
from faker import Faker

from base_test import BASE_URL

fake = Faker()


def test_put_update_response_body():
    user_id = random.randint(1, 12)
    name = fake.name()
    job = fake.job()
    request_body = generate_put_update_request(name, job)
    response = put_update(request_body, user_id)
    data = response.json()
    assert response.status_code == 200
    assert data['name'] == name, "Invalid name value"
    assert data['job'] == job, "Invalid job value"


def generate_put_update_request(name, job):
    return {
        "name": name,
        "job": job
    }


def put_update(request_body, user_id):
    return requests.put(BASE_URL + f"/api/users/{user_id}", json=request_body)
