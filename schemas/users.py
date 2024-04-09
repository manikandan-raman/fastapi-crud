import datetime

from pydantic import UUID4, BaseModel


class AdditionalFields(BaseModel):
    id: UUID4
    created_at: datetime.datetime


class AddUser(BaseModel):
    name: str
    age: int
    is_qualified: bool


class UserResponse(AddUser, AdditionalFields): ...
