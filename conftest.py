import allure
import pytest

from project_requests.register import Register
from project_requests.user import DeleteUser
from helpers import DataGenerator


@pytest.fixture
def temp_user__return_response_and_payload():
    with allure.step('Создаем нового уникального пользователя'):
        payload = {
            'email': DataGenerator.generate_random_email(),
            'password': DataGenerator.generate_random_string(),
            'name': DataGenerator.generate_random_string()
        }
        response = Register.register_new_user_using_payload(payload)
    yield response, payload
    with allure.step('Удаляем созданного пользователя'):
        token = str(response.json()['accessToken']).replace('Bearer ', '')
        DeleteUser.delete_user(token)

