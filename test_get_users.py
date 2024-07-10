import random

import requests

BASE_URL = 'https://reqres.in'


def test_get_list_users_status_code():
    page_id = random.randint(1, 2)
    response = get_list_users(page_id)
    print(response)
    assert response.status_code == 200


def test_check_users_id():
    for page_id in range(1, 3):
        response = get_list_users(page_id).json()
        users = response['data']
        assert len(users) == 6
        for user in users:
            if page_id == 1:
                print(user['id'])
                assert user['id'] in [1, 2, 3, 4, 5, 6]
            else:
                print(user['id'])
                assert user['id'] in [7, 8, 9, 10, 11, 12]


def test_get_single_user_status_code():
    user_id = random.randint(1, 12)
    response = get_single_user(user_id)
    assert response.status_code == 200


def test_check_user_id():
    user_id = random.randint(1, 12)
    response = get_single_user(user_id).json()
    assert user_id == response['data']['id']


def test_check_user_not_found():
    user_id = 9999
    response = get_single_user(user_id)
    assert response.status_code == 404


def get_list_users(page_id):
    return requests.get(BASE_URL + f"/api/users?page={page_id}")


def get_single_user(user_id):
    return requests.get(BASE_URL + f"/api/users/{user_id}")
