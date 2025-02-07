from uuid import UUID
from fastapi import APIRouter, Response, status

from src.dependencies import DBSession
from src.users.models import Address, User
from src.users import controllers
from src.users.schemas import AddressCreateSchema, AddressPartialUpdateSchema, AddressUpdateSchema, ListAddressSchema, ListUserSchema, UserCreateSchema, UserPartialUpdateSchema, UserUpdateSchema

router = APIRouter(prefix="/users", tags=["user"])


@router.post("/", response_model=User)
async def create_user(data: UserCreateSchema, session: DBSession) -> User:
    user = await controllers.create_user(data=data, session=session)
    return user


@router.get("/{id}", response_model=User)
async def get_user(id: UUID, session: DBSession) -> User:
    user = await controllers.get_user(id=id, session=session)
    return user


@router.get("/", response_model=ListUserSchema)
async def get_users(session: DBSession) -> ListUserSchema:
    users = await controllers.get_users(session=session)
    return ListUserSchema(count=len(users), items=users)


@router.patch("/{id}", response_model=User)
async def partial_update_user(id: UUID, data: UserPartialUpdateSchema, session: DBSession) -> User:
    user = await controllers.update_user(id=id, data=data, session=session)
    return user


@router.put("/{id}", response_model=User)
async def update_user(id: UUID, data: UserUpdateSchema, session: DBSession) -> User:
    user = await controllers.update_user(id=id, data=data, session=session)
    return user


@router.delete("/{id}")
async def delete_user(id: UUID, session: DBSession) -> Response:
    await controllers.remove_user(id=id, session=session)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.post("/address/", response_model=Address)
async def create_address(data: AddressCreateSchema, session: DBSession) -> Address:
    address = await controllers.create_address(data=data, session=session)
    return address


@router.get("/address/{id}", response_model=Address)
async def get_address(id: UUID, session: DBSession) -> Address:
    address = await controllers.get_address(id=id, session=session)
    return address


@router.get("/address/", response_model=ListAddressSchema)
async def get_addresses(session: DBSession) -> ListAddressSchema:
    addresses = await controllers.get_addresses(session=session)
    return ListAddressSchema(count=len(addresses), items=addresses)


@router.patch("/address/{id}", response_model=Address)
async def partial_update_address(id: UUID, data: AddressPartialUpdateSchema, session: DBSession) -> Address:
    address = await controllers.update_address(id=id, data=data, session=session)
    return address


@router.put("/address/{id}", response_model=Address)
async def update_address(id: UUID, data: AddressUpdateSchema, session: DBSession) -> Address:
    address = await controllers.update_address(id=id, data=data, session=session)
    return address


@router.delete("/address/{id}")
async def remove_address(id: UUID, session: DBSession) -> Response:
    await controllers.remove_address(id=id, session=session)
    return Response(status_code=status.HTTP_204_NO_CONTENT)