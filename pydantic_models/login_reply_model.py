from pydantic import BaseModel


class User(BaseModel):
    email: str
    name: str


class LoginSuccessReplyModel(BaseModel):
    success: bool
    accessToken: str
    refreshToken: str
    user: User


class LoginFailReplyModel(BaseModel):
    success: bool
    message: str
