from uuid import UUID
from sqlmodel import SQLModel

from src.users.models import Address, User


class UserBaseSchema(SQLModel):
    full_name: str
    email: str
    password: str
    document_number: str
    phone: str
    type: str


class AddressCreateSchema(SQLModel):
    city: str
    state: str
    neighborhood: str
    postal_code: str
    is_main: bool


class UserCreateSchema(UserBaseSchema):
    address: AddressCreateSchema


class UserPartialUpdateSchema(UserBaseSchema):
    full_name: str | None = None
    email: str | None = None
    password: str | None = None
    document_number: str | None = None
    phone: str | None = None
    type: str | None = None


class UserUpdateSchema(UserBaseSchema):
    pass


class ListUserSchema(SQLModel):
    count: int
    items: list[User]


class AddressBaseSchema(SQLModel):
    city: str
    state: str
    neighborhood: str
    postal_code: str
    is_main: bool


class AddressCreateSchema(AddressBaseSchema):
    user_id: UUID


class AddressPartialUpdateSchema(AddressBaseSchema):
    city: str | None = None
    state: str | None = None
    neighborhood: str | None = None
    postal_code: str | None = None
    is_main: bool | None = None


class AddressUpdateSchema(AddressBaseSchema):
    pass


class ListAddressSchema(SQLModel):
    count: int
    items: list[Address]