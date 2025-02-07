from uuid import UUID
from sqlmodel import Session, select, delete, update

from src.users.exceptions import AddressNotFound, UserNotFound
from src.users.schemas import AddressCreateSchema, AddressPartialUpdateSchema, AddressUpdateSchema, UserCreateSchema, UserPartialUpdateSchema, UserUpdateSchema
from .models import Address, User


async def create_user(data: UserCreateSchema, session: Session) -> User:
    user = User(**data.model_dump())
    session.add(user)
    session.flush()

    address = Address(**data.address.model_dump(), user_id=user.id)
    session.add(address)
    
    session.commit()
    session.refresh(user)

    return user


async def get_user(id: UUID, session: Session) -> User:
    user = session.get(User, id)
    if not user:
        raise UserNotFound()
    
    return user


async def get_users(session: Session) -> list[User]:
    users = session.exec(select(User)).all()
    return users


async def update_user(id: UUID, data: UserPartialUpdateSchema | UserUpdateSchema, session: Session) -> User:
    user = session.get(User, id)
    if not user:
        raise UserNotFound()
    
    user.sqlmodel_update(data.model_dump(exclude_unset=True))
    session.add(user)
    session.commit()
    session.refresh(user)

    return user


async def remove_user(id: UUID, session: Session) -> None:
    user = session.get(User, id)
    if not user:
        raise UserNotFound()
    
    session.exec(delete(Address).where(Address.user_id == id))
    session.delete(user)
    session.commit()


async def create_address(data: AddressCreateSchema, session: Session) -> Address:
    address = Address(**data.model_dump())
    
    if address.is_main:
        session.exec(update(Address).where(Address.user_id == data.user_id).values(is_main=False))
    
    session.add(address)
    session.commit()
    session.refresh(address)

    return address


async def get_address(id: UUID, session: Session) -> Address:
    address = session.get(Address, id)
    if not address:
        raise AddressNotFound()
    
    return address


async def get_addresses(session: Session) -> list[Address]:
    addresses = session.exec(select(Address)).all()
    return addresses


async def update_address(id: UUID, data: AddressPartialUpdateSchema | AddressUpdateSchema, session: Session) -> Address:
    address = session.get(Address, id)
    if not address:
        raise AddressNotFound()
    
    address.sqlmodel_update(data.model_dump(exclude_unset=True))
    session.add(address)
    session.commit()
    session.refresh(address)

    return address


async def remove_address(id: UUID, session: Session) -> None:
    address = session.get(Address, id)
    if not address:
        raise AddressNotFound()
    
    session.delete(address)
    session.commit()