from pydantic import BaseModel


class UserModel(BaseModel):
    email: str
    name: str


class LoginSuccessReplyModel(BaseModel):
    success: bool
    accessToken: str
    refreshToken: str
    user: UserModel


class LoginFailReplyModel(BaseModel):
    success: bool
    message: str
