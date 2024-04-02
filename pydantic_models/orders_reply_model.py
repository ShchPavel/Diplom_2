from pydantic import BaseModel, Field
from typing import List


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


class OrderWithoutIngredientsBaseModel(BaseModel):
    success: bool
    message: str


class Order(BaseModel):
    id: str = Field(alias='_id')
    ingredients: List[str]
    status: str
    name: str
    createdAt: str
    updatedAt: str
    number: int


class GetOrdersAuthorizedUserModel(BaseModel):
    success: bool
    orders: List[Order]
    total: int
    totalToday: int


class GetOrdersUnauthorizedUserModel(BaseModel):
    success: bool
    message: str
