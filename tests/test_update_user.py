import pytest

from project_requests.user import UpdateUser
from helpers import DataGenerator as DG
from pydantic_models.user_reply_model import UserSuccessReplyModel, UserFailReplyModel
from data import StatusCodes


class TestUpdateUser:

    @pytest.mark.parametrize('email, password, name', [
        (DG.generate_random_email(), None, None),
        (None, DG.generate_random_string(), None),
        (None, None, DG.generate_random_string())
    ])
    def test_update_authorized_user_using_any_parameter_success(self, email, password, name, register_temp_user_then_return_response):
        token = str(register_temp_user_then_return_response.json()['accessToken']).replace('Bearer ', '')
        payload = {
            'email': email,
            'password': password,
            'name': name
        }
        r = UpdateUser.update_user(token, payload)

        response_text: UserSuccessReplyModel = UserSuccessReplyModel.model_validate_json(r.text)
        response_code = r.status_code
        assert response_code == StatusCodes.OK and response_text.success is True

    @pytest.mark.parametrize('email, password, name', [
        (DG.generate_random_email(), None, None),
        (None, DG.generate_random_string(), None),
        (None, None, DG.generate_random_string())
    ])
    def test_update_unauthorized_user_using_any_parameter_success(self, email, password, name, register_temp_user_then_return_response):
        token = None
        payload = {
            'email': email,
            'password': password,
            'name': name
        }
        r = UpdateUser.update_user(token, payload)

        response_text: UserFailReplyModel = UserFailReplyModel.model_validate_json(r.text)
        response_code = r.status_code
        assert response_code == StatusCodes.UNAUTHORIZED and response_text.success is False

