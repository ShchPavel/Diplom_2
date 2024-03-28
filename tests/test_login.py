from project_requests.login import Login
from pydantic_models.login_reply_model import LoginSuccessReplyModel, LoginFailReplyModel
from data import StatusCodes


class TestLogin:

    def test_login_success(self, register_temp_user_then_return_response_and_payload):
        response, payload = register_temp_user_then_return_response_and_payload
        r = Login.known_user_correct_login(payload)

        response_status = r.status_code
        response_text: LoginSuccessReplyModel = LoginSuccessReplyModel.model_validate_json(r.text)
        assert response_status == StatusCodes.OK and response_text.success is True

    def test_incorrect_login_fail(self, register_temp_user_then_return_response_and_payload):
        response, payload = register_temp_user_then_return_response_and_payload
        r = Login.known_user_change_credentials_incorrect_login(payload)

        response_status = r.status_code
        response_text: LoginFailReplyModel = LoginFailReplyModel.model_validate_json(r.text)
        assert response_status == StatusCodes.UNAUTHORIZED and response_text.success is False

