import requests
from data import Url
import allure


class Orders:
    @staticmethod
    @allure.step('Создаем заказ')
    def create_order(token=None, ingredients: list = None):

        payload = None
        if ingredients:
            payload = {
                "ingredients": ingredients
            }

        bearer_token = None
        if token:
            bearer_token = f'Bearer {token}'
        headers = {"Authorization": bearer_token}

        response = requests.post(Url.ORDER_URL, headers=headers, data=payload)

        return response

    @staticmethod
    @allure.step('Получаем информацию о заказе')
    def get_order(token=None):

        bearer_token = None
        if token:
            bearer_token = f'Bearer {token}'
        headers = {"Authorization": bearer_token}

        response = requests.get(Url.ORDER_URL, headers=headers)

        return response
