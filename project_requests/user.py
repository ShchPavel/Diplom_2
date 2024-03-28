import requests
from data import Url


class DeleteUser:
    @staticmethod
    def delete_user(token):
        bearer_token = f'Bearer {token}'
        headers = {"Authorization": bearer_token}
        response = requests.delete(Url.USER_URL, headers=headers)
        return response


class GetUserInfo:
    @staticmethod
    def get_user_info(token):
        bearer_token = f'Bearer {token}'
        headers = {"Authorization": bearer_token}
        response = requests.get(Url.USER_URL, headers=headers)
        return response


class UpdateUser:
    @staticmethod
    def update_user(token, payload):

        name = payload['name']
        email = payload['email']
        password = payload['password']
        payload = {
            "email": email,
            "password": password,
            "name": name
        }
        bearer_token = None

        if token:
            bearer_token = f'Bearer {token}'
        headers = {"Authorization": bearer_token}

        response = requests.patch(Url.USER_URL, headers=headers, data=payload)
        return response
