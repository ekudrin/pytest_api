import requests

BASE_URL = 'https://reqres.in'


class TestPostCreate:

    def test_post_create_status_code(self):
        header = {
            'Accept': 'text/plain',
            'Content-type': 'application/json'
        }
        request_body = {
            "name": "morpheus",
            "job": "leader"
        }

        response = requests.post(BASE_URL + "/api/users", headers=header, json=request_body)
        data = response.json()
        assert response.status_code == 201, "Status code is not valid"
        assert data['name'] == "morpheus"
