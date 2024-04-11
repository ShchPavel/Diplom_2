import requests
from helpers import DataGenerator
from data import Url
import allure


class Login:
    @staticmethod
    @allure.step('Логинимся по мейл\пароль, которые использовали для регистрации')
    def known_user_correct_login(payload):
        payload = {
            "email": payload['email'],
            "password": payload['password']
            }
        response = requests.post(Url.LOGIN_URL, data=payload)
        return response

    @staticmethod
    @allure.step('Логинимся, но специально добавляем лишние символы в логин\пароль, которые использовали для регистрации')
    def known_user_change_credentials_incorrect_login(payload):
        payload['email'] += DataGenerator.generate_random_string()
        payload['password'] += DataGenerator.generate_random_string()
        payload = {
            "email": payload['email'],
            "password": payload['password']
        }
        response = requests.post(Url.LOGIN_URL, data=payload)
        return response

