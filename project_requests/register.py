import requests
from data import Url
from helpers import DataGenerator


class Register:
    @staticmethod
    def register_new_user_using_parameters(email=None, password=None, name=None):
        payload = {
            "email": email,
            "password": password,
            "name": name
        }

        response = requests.post(Url.REGISTER_URL, data=payload)
        return response

    @staticmethod
    def register_new_user_using_payload(payload):
        response = requests.post(Url.REGISTER_URL, data=payload)
        return response
