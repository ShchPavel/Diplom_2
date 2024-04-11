from project_requests.orders import Orders
from data import Ingredients, StatusCodes
from pydantic_models.orders_reply_model import (AuthorizedOrderWithIngredientsReplyModel, OrderWithoutIngredientsBaseModel,
                                                UnauthorizedOrderWithIngredientsReplyModel, GetOrdersAuthorizedUserModel,
                                                GetOrdersUnauthorizedUserModel)
import allure


class TestOrders:

    @allure.title('Проверка создания заказа с ингредиентами авторизованным пользователем')
    def test_create_order_authorized_user_with_ingredient(self, temp_user__return_response_and_payload):
        response, payload = temp_user__return_response_and_payload
        token = str(response.json()['accessToken']).replace('Bearer ', '')
        r = Orders.create_order(token, [Ingredients.KNOWN_INGREDIENT])

        response_code = r.status_code
        response_text: AuthorizedOrderWithIngredientsReplyModel = AuthorizedOrderWithIngredientsReplyModel.model_validate_json(r.text)
        with allure.step('Проверяем что в ответе StatusCode:200 и в теле ответа success:True'):
            assert response_code == StatusCodes.OK and response_text.success is True

    @allure.title('Проверка создания заказа без ингредиентов авторизованным пользователем')
    def test_create_order_authorized_user_without_ingredient(self, temp_user__return_response_and_payload):
        response, payload = temp_user__return_response_and_payload
        token = str(response.json()['accessToken']).replace('Bearer ', '')
        r = Orders.create_order(token)

        response_code = r.status_code
        response_text: OrderWithoutIngredientsBaseModel = OrderWithoutIngredientsBaseModel.model_validate_json(r.text)
        with allure.step('Проверяем что в ответе StatusCode:400 и в теле ответа success:False'):
            assert response_code == StatusCodes.BAD_REQUEST and response_text.success is False

    @allure.title('Проверка создания заказа с ингредиентами НЕавторизованным пользователем')
    def test_create_order_unauthorized_user_with_ingredient(self, temp_user__return_response_and_payload):
        r = Orders.create_order(ingredients=[Ingredients.KNOWN_INGREDIENT])

        response_code = r.status_code
        response_text: UnauthorizedOrderWithIngredientsReplyModel = UnauthorizedOrderWithIngredientsReplyModel.model_validate_json(r.text)
        with allure.step('Проверяем что в ответе StatusCode:200 и в теле ответа success:True'):
            assert response_code == StatusCodes.OK and response_text.success is True

    @allure.title('Проверка создания заказа без ингредиентов НЕавторизованным пользователем')
    def test_create_order_unauthorized_user_without_ingredient(self, temp_user__return_response_and_payload):
        r = Orders.create_order()

        response_code = r.status_code
        response_text: OrderWithoutIngredientsBaseModel = OrderWithoutIngredientsBaseModel.model_validate_json(r.text)
        with allure.step('Проверяем что в ответе StatusCode:400 и в теле ответа success:False'):
            assert response_code == StatusCodes.BAD_REQUEST and response_text.success is False

    @allure.title('Проверка создания заказа с некорректным ингредиентом')
    def test_create_order_incorrect_ingredient(self, temp_user__return_response_and_payload):
        r = Orders.create_order(ingredients=Ingredients.INVALID_INGREDIENT)

        response_code = r.status_code
        with allure.step('Проверяем что в ответе StatusCode:500'):
                assert response_code == StatusCodes.INTERNAL_SERVER_ERROR

    @allure.title('Проверка получения заказов от имени авторизованного пользователя')
    def test_get_order_authorized_user_with_orders(self, temp_user__return_response_and_payload):
        response, payload = temp_user__return_response_and_payload
        token = str(response.json()['accessToken']).replace('Bearer ', '')
        Orders.create_order(token)
        r = Orders.get_order(token)

        response_code = r.status_code
        response_text: GetOrdersAuthorizedUserModel = GetOrdersAuthorizedUserModel.model_validate_json(r.text)
        with allure.step('Проверяем что в ответе StatusCode:200 и в теле ответа success:True'):
            assert response_code == StatusCodes.OK and response_text.success is True

    @allure.title('Проверка получения заказов от имени НЕавторизованного пользователя')
    def test_get_order_unauthorized_user_with_orders(self):
        r = Orders.get_order(token=None)

        response_code = r.status_code
        response_text: GetOrdersUnauthorizedUserModel = GetOrdersUnauthorizedUserModel.model_validate_json(r.text)
        with allure.step('Проверяем что в ответе StatusCode:401 и в теле ответа success:False'):
            assert response_code == StatusCodes.UNAUTHORIZED and response_text.success is False
