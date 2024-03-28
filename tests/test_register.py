from project_requests.register import Register
from pydantic_schemas.register_schema import RegisterSuccessReply, RegisterReplyFail
from data import StatusCodes

class TestRegister:

    def test_register_new_random_user_success(self):
        r = Register.register_correct_new_random_user()
        response_status = r.status_code
        response_text: RegisterSuccessReply = RegisterSuccessReply.model_validate_json(r.text)
        assert response_status == StatusCodes.OK and response_text.success is True

    def test_register_duplicated_user_fail(self):
        r = Register.register_duplicate_user()
        response_status = r.status_code
        response_text: RegisterReplyFail = RegisterReplyFail.model_validate_json(r.text)
        assert response_status == StatusCodes.FORBIDDEN and response_text.success is False

    def test_register_user_without_email_fail(self):
        r = Register.register_new_random_user_without_email()
        response_status = r.status_code
        response_text: RegisterReplyFail = RegisterReplyFail.model_validate_json(r.text)
        assert response_status == StatusCodes.FORBIDDEN and response_text.success is False
