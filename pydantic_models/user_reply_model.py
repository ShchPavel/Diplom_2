from pydantic import BaseModel


class User(BaseModel):
    email: str
    name: str


class UserSuccessReplyModel(BaseModel):
    success: bool
    user: User


class UserFailReplyModel(BaseModel):
    success: bool
    message: str

