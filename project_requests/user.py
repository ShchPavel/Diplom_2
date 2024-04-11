import allure
import requests
from data import Url


class DeleteUser:
    @staticmethod
    @allure.step('Удаляем пользователя')
    def delete_user(token):
        bearer_token = f'Bearer {token}'
        headers = {"Authorization": bearer_token}
        response = requests.delete(Url.USER_URL, headers=headers)
        return response


class GetUserInfo:
    @staticmethod
    @allure.step('Получаем информацию о пользователе')
    def get_user_info(token):
        bearer_token = f'Bearer {token}'
        headers = {"Authorization": bearer_token}
        response = requests.get(Url.USER_URL, headers=headers)
        return response


class UpdateUser:
    @staticmethod
    @allure.step('Обновляем информацию о пользователе')
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
