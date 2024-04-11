import pytest
from project_requests.register import Register
from pydantic_models.register_reply_model import RegisterSuccessReplyModel, RegisterReplyFailModel
from data import StatusCodes
from helpers import DataGenerator as DG
import allure


class TestRegister:
    @allure.title('Проверка успешного создания уникального пользователя')
    def test_register_new_random_user_success(self, temp_user__return_response_and_payload):
        response, payload = temp_user__return_response_and_payload

        response_status = response.status_code
        response_text: RegisterSuccessReplyModel = RegisterSuccessReplyModel.model_validate_json(response.text)
        with allure.step('Проверяем что в ответе StatusCode:200 и в теле ответа success:True'):
            assert response_status == StatusCodes.OK and response_text.success is True

    @allure.title('Проверка получения ошибки при создании юзера-дубликата')
    def test_register_duplicated_user_fail(self, temp_user__return_response_and_payload):
        first_registration, payload = temp_user__return_response_and_payload
        first_registration_email = first_registration.json()['user']['email']

        second_registration = Register.register_new_user_using_parameters(email=first_registration_email)

        response_status = second_registration.status_code
        response_text: RegisterReplyFailModel = RegisterReplyFailModel.model_validate_json(second_registration.text)
        with allure.step('Проверяем что в ответе StatusCode:403 и в теле ответа success:False'):
            assert response_status == StatusCodes.FORBIDDEN and response_text.success is False

    @pytest.mark.parametrize('email, password, name',
                             [
                                 (DG.generate_random_email(), DG.generate_random_string(), None),
                                 (DG.generate_random_email(), None, DG.generate_random_string()),
                                 (None, DG.generate_random_string(), DG.generate_random_string())
                             ])
    @allure.title('Проверка создания пользователя без заполнения одного из полей. email: {email}, '
                  'password: {password}, name: {name}')
    def test_register_user_without_parameter_fail(self, email, password, name):
        r = Register.register_new_user_using_parameters(email, password, name)
        response_status = r.status_code
        response_text: RegisterReplyFailModel = RegisterReplyFailModel.model_validate_json(r.text)
        with allure.step('Проверяем что в ответе StatusCode:403 и в теле ответа success:False'):
            assert response_status == StatusCodes.FORBIDDEN and response_text.success is False
