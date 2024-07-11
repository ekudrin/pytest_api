import random
import requests

from base_test import BASE_URL


# Tests for List users, Single user, Single user not found

def test_get_list_users_check_users_id():
    for page_id in range(1, 3):
        response = get_list_users(page_id)
        assert response.status_code == 200, "Invalid status code"
        data = response.json()
        users = data['data']
        assert len(users) == 6
        for user in users:
            if page_id == 1:
                assert user['id'] in [1, 2, 3, 4, 5, 6], "Id is not in valid id list"
            else:
                assert user['id'] in [7, 8, 9, 10, 11, 12], "Id is not in valid id list"


def test_get_single_user_check_user_id():
    user_id = random.randint(1, 12)
    response = get_single_user(user_id)
    assert response.status_code == 200, "Invalid status code"
    data = response.json()
    assert user_id == data['data']['id'], "Invalid user id"


def test_check_user_not_found():
    user_id = 9999
    response = get_single_user(user_id)
    assert response.status_code == 404, "Invalid status code"


def test_delayed_list_users():
    delay = 2
    timeout = 3
    response = get_delayed_list_users(delay, timeout)
    assert response.status_code == 200, "Invalid status code"


def get_list_users(page_id):
    return requests.get(BASE_URL + f"/api/users?page={page_id}")


def get_single_user(user_id):
    return requests.get(BASE_URL + f"/api/users/{user_id}")


def get_delayed_list_users(delay, expected_timeout):
    return requests.get(BASE_URL + f"/api/users?delay={delay}", timeout=expected_timeout)
