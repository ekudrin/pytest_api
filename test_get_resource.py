import random
import string

import requests

BASE_URL = 'https://reqres.in'


def test_get_list_resource_status_code():
    response = get_list_resource()
    assert response.status_code == 200


def test_get_list_resource_check_response():
    response = get_list_resource().json()
    users = response['data']
    assert len(users) == 6


def test_get_single_resource_status_code():
    resource_id = random.randint(1, 12)
    response = get_single_resource(resource_id)
    assert response.status_code == 200


def test_get_single_resource_check_id():
    resource_id = random.randint(1, 12)
    response = get_single_resource(resource_id).json()
    assert response['data']['id'] == resource_id


def test_get_single_resource_not_found():
    resource_id = 999
    response = get_single_resource(resource_id)
    assert response.status_code == 404


def get_list_resource():
    url = ''.join(random.choices(string.ascii_lowercase, k=5))
    return requests.get(BASE_URL + f"/api/{url}")


def get_single_resource(resource_id):
    url = ''.join(random.choices(string.ascii_lowercase, k=5))
    return requests.get(BASE_URL + f"/api/{url}/{resource_id}")
