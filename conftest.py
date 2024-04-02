import pytest

from project_requests.register import Register
from project_requests.user import DeleteUser
from helpers import DataGenerator
from project_requests.orders import Orders
from data import Ingredients


@pytest.fixture
def register_temp_user_then_return_response():
    email = DataGenerator.generate_random_email()
    password = DataGenerator.generate_random_string()
    name = DataGenerator.generate_random_string()
    response = Register.register_new_user_using_parameters(email, password, name)
    yield response
    token = str(response.json()['accessToken']).replace('Bearer ', '')
    DeleteUser.delete_user(token)


@pytest.fixture
def register_temp_user_then_return_response_and_payload():
    payload = {
        'email': DataGenerator.generate_random_email(),
        'password': DataGenerator.generate_random_string(),
        'name': DataGenerator.generate_random_string()
    }
    response = Register.register_new_user_using_payload(payload)
    yield response, payload
    token = str(response.json()['accessToken']).replace('Bearer ', '')
    DeleteUser.delete_user(token)


@pytest.fixture
def register_temp_user_and_order_then_return_response():
    email = DataGenerator.generate_random_email()
    password = DataGenerator.generate_random_string()
    name = DataGenerator.generate_random_string()
    register_response = Register.register_new_user_using_parameters(email, password, name)
    token = str(register_response.json()['accessToken']).replace('Bearer ', '')
    get_order_response = Orders.create_order(token, Ingredients.KNOWN_INGREDIENT)
    yield get_order_response, token
    DeleteUser.delete_user(token)
