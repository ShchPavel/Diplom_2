from pydantic import BaseModel


class User(BaseModel):
    email: str
    name: str


class RegisterSuccessReplyModel(BaseModel):
    success: bool
    user: User
    accessToken: str
    refreshToken: str


class RegisterReplyFailModel(BaseModel):
    success: bool
    message: str
