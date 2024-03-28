import requests

from data import Url


class Orders:
    @staticmethod
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
