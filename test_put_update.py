import requests

BASE_URL = 'https://reqres.in'


class TestPutUpdate:

    def test_put_update_status_code(self):
        payload = {
            "name": "morpheus",
            "job": "zion resident"

        }
        response = requests.put(BASE_URL + "/api/users/2", json=payload)
        assert response.status_code == 200
