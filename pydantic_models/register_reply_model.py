from pydantic import BaseModel


class UserModel(BaseModel):
    email: str
    name: str


class RegisterSuccessReplyModel(BaseModel):
    success: bool
    user: UserModel
    accessToken: str
    refreshToken: str


class RegisterReplyFailModel(BaseModel):
    success: bool
    message: str
