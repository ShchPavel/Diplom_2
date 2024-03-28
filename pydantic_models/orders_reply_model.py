from pydantic import BaseModel, Field


class UnauthorizedOrder(BaseModel):
    number: int


class UnauthorizedOrderWithIngredientsReplyModel(BaseModel):
    success: bool
    name: str
    order: UnauthorizedOrder


class AuthorizedOrder(BaseModel):
    ingredients: list
    id: str = Field(alias='_id')
    owner: dict
    status: str
    name: str
    createdAt: str
    updatedAt: str
    number: int
    price: int


class AuthorizedOrderWithIngredientsReplyModel(BaseModel):
    success: bool
    name: str
    order: AuthorizedOrder


class OrderWithoutIngredientsBasicModel(BaseModel):
    success: bool
    message: str
