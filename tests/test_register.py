import pytest

from project_requests.register import Register
from pydantic_models.register_reply_model import RegisterSuccessReplyModel, RegisterReplyFailModel
from data import StatusCodes
from helpers import DataGenerator as DG


class TestRegister:

    def test_register_new_random_user_success(self, register_temp_user_then_return_response):
        r = register_temp_user_then_return_response

        response_status = r.status_code
        response_text: RegisterSuccessReplyModel = RegisterSuccessReplyModel.model_validate_json(r.text)
        assert response_status == StatusCodes.OK and response_text.success is True

    def test_register_duplicated_user_fail(self, register_temp_user_then_return_response):
        first_registration = register_temp_user_then_return_response
        first_registration_email = first_registration.json()['user']['email']

        second_registration = Register.register_new_user_using_parameters(email=first_registration_email)

        response_status = second_registration.status_code
        response_text: RegisterReplyFailModel = RegisterReplyFailModel.model_validate_json(second_registration.text)
        assert response_status == StatusCodes.FORBIDDEN and response_text.success is False

    @pytest.mark.parametrize('email, password, name',
                             [
                                 (DG.generate_random_email(), DG.generate_random_string(), None),
                                 (DG.generate_random_email(), None, DG.generate_random_string()),
                                 (None, DG.generate_random_string(), DG.generate_random_string())
                             ])
    def test_register_user_without_parameter_fail(self, email, password, name):
        r = Register.register_new_user_using_parameters(email, password, name)
        response_status = r.status_code
        response_text: RegisterReplyFailModel = RegisterReplyFailModel.model_validate_json(r.text)
        assert response_status == StatusCodes.FORBIDDEN and response_text.success is False
