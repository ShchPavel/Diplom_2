from pydantic import BaseModel


class User(BaseModel):
    email: str
    name: str


class RegisterSuccessReply(BaseModel):
    success: bool
    user: User
    accessToken: str
    refreshToken: str


class RegisterReplyFail(BaseModel):
    success: bool
    message: str
