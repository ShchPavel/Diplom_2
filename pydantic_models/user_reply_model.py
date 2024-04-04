from pydantic import BaseModel


class UserModel(BaseModel):
    email: str
    name: str


class UserSuccessReplyModel(BaseModel):
    success: bool
    user: UserModel


class UserFailReplyModel(BaseModel):
    success: bool
    message: str

