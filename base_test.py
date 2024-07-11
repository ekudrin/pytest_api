BASE_URL = 'https://reqres.in'


def generate_user(name, job):
    return {
        "name": name,
        "job": job
    }


def generate_register_entity(email, password):
    return {
        "email": email,
        "password": password
    }
