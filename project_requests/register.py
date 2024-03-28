import requests
from data import Url
from helpers import DataGenerator


class Register:
    @staticmethod
    def register_correct_new_random_user():

        email = DataGenerator.generate_random_email()
        password = DataGenerator.generate_random_string()
        name = DataGenerator.generate_random_string()

        payload = {
            "email": email,
            "password": password,
            "name": name
        }

        response = requests.post(Url.REGISTER_URL, data=payload)

        return response

    @staticmethod
    def register_duplicate_user():

        email = DataGenerator.generate_random_email()
        password = DataGenerator.generate_random_string()
        name = DataGenerator.generate_random_string()

        payload = {
            "email": email,
            "password": password,
            "name": name
        }

        requests.post(Url.REGISTER_URL, data=payload)
        second_registration_response = requests.post(Url.REGISTER_URL, data=payload)

        return second_registration_response

    @staticmethod
    def register_new_random_user_without_email():

        password = DataGenerator.generate_random_string()
        name = DataGenerator.generate_random_string()

        payload = {
            "password": password,
            "name": name
        }

        response = requests.post(Url.REGISTER_URL, data=payload)

        return response
