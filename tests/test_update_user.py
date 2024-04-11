import pytest
from project_requests.user import UpdateUser
from helpers import DataGenerator as DG
from pydantic_models.user_reply_model import UserSuccessReplyModel, UserFailReplyModel
from data import StatusCodes
import allure


class TestUpdateUser:

    @pytest.mark.parametrize('email, password, name', [
        (DG.generate_random_email(), None, None),
        (None, DG.generate_random_string(), None),
        (None, None, DG.generate_random_string())
    ])
    @allure.title('Проверка успешного изменения данных авторизованным пользователем. '
                  'Изменяется email: {email}, password: {password}, name: {name}')
    def test_update_authorized_user_using_any_parameter_success(self, email, password, name, temp_user__return_response_and_payload):
        response, payload = temp_user__return_response_and_payload
        token = str(response.json()['accessToken']).replace('Bearer ', '')
        payload = {
            'email': email,
            'password': password,
            'name': name
        }
        r = UpdateUser.update_user(token, payload)

        response_text: UserSuccessReplyModel = UserSuccessReplyModel.model_validate_json(r.text)
        response_code = r.status_code
        with allure.step('Проверяем что в ответе StatusCode:200 и в теле ответа success:True'):
            assert response_code == StatusCodes.OK and response_text.success is True

    @pytest.mark.parametrize('email, password, name', [
        (DG.generate_random_email(), None, None),
        (None, DG.generate_random_string(), None),
        (None, None, DG.generate_random_string())
    ])
    @allure.title('Проверка НЕуспешногго изменения данных НЕавторизованным пользователем. '
                  'Изменяется email: {email}, password: {password}, name: {name}')
    def test_update_unauthorized_user_using_any_parameter_success(self, email, password, name, temp_user__return_response_and_payload):
        token = None
        payload = {
            'email': email,
            'password': password,
            'name': name
        }
        r = UpdateUser.update_user(token, payload)

        response_text: UserFailReplyModel = UserFailReplyModel.model_validate_json(r.text)
        response_code = r.status_code
        with allure.step('Проверяем что в ответе StatusCode:401 и в теле ответа success:False'):
            assert response_code == StatusCodes.UNAUTHORIZED and response_text.success is False
