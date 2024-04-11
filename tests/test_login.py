from project_requests.login import Login
from pydantic_models.login_reply_model import LoginSuccessReplyModel, LoginFailReplyModel
from data import StatusCodes
import allure


class TestLogin:

    @allure.title('Проверка логина под существующим пользователем')
    def test_login_success(self, temp_user__return_response_and_payload):
        response, payload = temp_user__return_response_and_payload
        r = Login.known_user_correct_login(payload)

        response_status = r.status_code
        response_text: LoginSuccessReplyModel = LoginSuccessReplyModel.model_validate_json(r.text)
        with allure.step('Проверяем что в ответе StatusCode:200 и в теле ответа success:True'):
            assert response_status == StatusCodes.OK and response_text.success is True

    @allure.title('Проверка логина под НЕсуществующим пользователем')
    def test_incorrect_login_fail(self, temp_user__return_response_and_payload):
        response, payload = temp_user__return_response_and_payload
        r = Login.known_user_change_credentials_incorrect_login(payload)

        response_status = r.status_code
        response_text: LoginFailReplyModel = LoginFailReplyModel.model_validate_json(r.text)
        with allure.step('Проверяем что в ответе StatusCode:401 и в теле ответа success:False'):
            assert response_status == StatusCodes.UNAUTHORIZED and response_text.success is False

