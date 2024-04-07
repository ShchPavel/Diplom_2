import requests
from data import Url
import allure


class Register:
    @staticmethod
    @allure.step('Регистрируем нового пользователя с определенными параметрами')
    def register_new_user_using_parameters(email=None, password=None, name=None):
        payload = {
            "email": email,
            "password": password,
            "name": name
        }

        response = requests.post(Url.REGISTER_URL, data=payload)
        return response

    @staticmethod
    @allure.step('Регистрируем нового пользователя с определенными параметрами')
    def register_new_user_using_payload(payload):
        response = requests.post(Url.REGISTER_URL, data=payload)
        return response
