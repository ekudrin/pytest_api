import random
import string

import requests

from base_test import BASE_URL


# Tests for List<Resource>, Single<Resource>, Single<Resource>not found


def test_get_list_resource_response_body():
    response = get_list_resource()
    assert response.status_code == 200,"Invalid status code"

    data = response.json()
    users = data['data']
    assert len(users) == 6, "Invalid lenght of user list"


def test_get_single_resource_responce_body():
    resource_id = random.randint(1, 12)
    response = get_single_resource(resource_id)
    assert response.status_code == 200,"Invalid status code"

    data = response.json()
    assert data['data']['id'] == resource_id, "Invalid id in response"


def test_get_single_resource_not_found():
    resource_id = 999
    response = get_single_resource(resource_id)
    assert response.status_code == 404,"Invalid status code"


def get_list_resource():
    url = ''.join(random.choices(string.ascii_lowercase, k=5))
    return requests.get(BASE_URL + f"/api/{url}")


def get_single_resource(resource_id):
    url = ''.join(random.choices(string.ascii_lowercase, k=5))
    return requests.get(BASE_URL + f"/api/{url}/{resource_id}")
