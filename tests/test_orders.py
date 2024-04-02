from project_requests.orders import Orders
from data import Ingredients, StatusCodes

from pydantic_models.orders_reply_model import (AuthorizedOrderWithIngredientsReplyModel, OrderWithoutIngredientsBaseModel,
                                                UnauthorizedOrderWithIngredientsReplyModel, GetOrdersAuthorizedUserModel,
                                                GetOrdersUnauthorizedUserModel)


class TestOrders:

    def test_create_order_authorized_user_with_ingredient(self, register_temp_user_then_return_response):
        token = str(register_temp_user_then_return_response.json()['accessToken']).replace('Bearer ', '')
        r = Orders.create_order(token, [Ingredients.KNOWN_INGREDIENT])

        response_code = r.status_code
        response_text: AuthorizedOrderWithIngredientsReplyModel = AuthorizedOrderWithIngredientsReplyModel.model_validate_json(r.text)
        assert response_code == StatusCodes.OK and response_text.success is True

    def test_create_order_authorized_user_without_ingredient(self, register_temp_user_then_return_response):
        token = str(register_temp_user_then_return_response.json()['accessToken']).replace('Bearer ', '')
        r = Orders.create_order(token)

        response_code = r.status_code
        response_text: OrderWithoutIngredientsBaseModel = OrderWithoutIngredientsBaseModel.model_validate_json(r.text)
        assert response_code == StatusCodes.BAD_REQUEST and response_text.success is False

    def test_create_order_unauthorized_user_with_ingredient(self, register_temp_user_then_return_response):
        r = Orders.create_order(ingredients=[Ingredients.KNOWN_INGREDIENT])

        response_code = r.status_code
        response_text: UnauthorizedOrderWithIngredientsReplyModel = UnauthorizedOrderWithIngredientsReplyModel.model_validate_json(r.text)
        assert response_code == StatusCodes.OK and response_text.success is True

    def test_create_order_unauthorized_user_without_ingredient(self, register_temp_user_then_return_response):
        r = Orders.create_order()

        response_code = r.status_code
        response_text: OrderWithoutIngredientsBaseModel = OrderWithoutIngredientsBaseModel.model_validate_json(r.text)
        assert response_code == StatusCodes.BAD_REQUEST and response_text.success is False

    def test_create_order_incorrect_ingredient(self, register_temp_user_then_return_response):
        r = Orders.create_order(ingredients=Ingredients.INVALID_INGREDIENT)

        response_code = r.status_code
        assert response_code == StatusCodes.INTERNAL_SERVER_ERROR

    def test_get_order_authorized_user_with_orders(self, register_temp_user_and_order_then_return_response):
        response, token = register_temp_user_and_order_then_return_response
        r = Orders.get_order(token)

        response_code = r.status_code
        response_text: GetOrdersAuthorizedUserModel = GetOrdersAuthorizedUserModel.model_validate_json(r.text)
        assert response_code == StatusCodes.OK and response_text.success is True

    def test_get_order_unauthorized_user_with_orders(self):
        r = Orders.get_order(token=None)

        response_code = r.status_code
        response_text: GetOrdersUnauthorizedUserModel = GetOrdersUnauthorizedUserModel.model_validate_json(r.text)
        assert response_code == StatusCodes.UNAUTHORIZED and response_text.success is False