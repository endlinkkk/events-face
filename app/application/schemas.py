from typing import Generic, TypeVar

from pydantic import BaseModel

IT = TypeVar("IT", bound=BaseModel)


class BaseQueryResponseSchema(BaseModel, Generic[IT]):
    count: int
    items: IT


class ErrorSchema(BaseModel):
    error: str
