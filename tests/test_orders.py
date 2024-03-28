from project_requests.orders import Orders
from data import Ingredients, StatusCodes
from pydantic_models.orders_reply_model import AuthorizedOrderWithIngredientsReplyModel


class TestOrders:

    def test_create_order_authorized_user_with_ingredient(self, register_temp_user_then_return_response):
        token = str(register_temp_user_then_return_response.json()['accessToken']).replace('Bearer ', '')
        r = Orders.create_order(token, [Ingredients.INGREDIENT1])

        response_code = r.status_code
        response_text: AuthorizedOrderWithIngredientsReplyModel = AuthorizedOrderWithIngredientsReplyModel.model_validate_json(r.text)
        assert response_code == StatusCodes.OK and response_text.success is True
