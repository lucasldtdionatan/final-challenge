from sqlmodel import SQLModel, Field
from uuid import UUID, uuid4
from datetime import datetime, timezone
from pydantic import EmailStr


class Address(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True, unique=True)
    city: str = Field(max_length=128, nullable=False)
    state: str = Field(max_length=128, nullable=False)
    neighborhood: str = Field(max_length=128, nullable=False)
    postal_code: str = Field(max_length=8, nullable=False)
    is_main: bool = Field(default=False, nullable=False)
    user_id: UUID = Field(nullable=False, foreign_key="user.id")
    created_at: datetime = Field(default=datetime.now(timezone.utc), nullable=False)
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc), nullable=False)


class User(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True, unique=True)
    full_name: str = Field(max_length=128, nullable=False)
    email: EmailStr = Field(max_length=55, nullable=False, unique=True)
    password: str = Field(nullable=False)
    document_number: str = Field(max_length=14, nullable=False, unique=True)
    phone: str = Field(max_length=11, nullable=False)
    type: str = Field(max_length=15, nullable=False)
    created_at: datetime = Field(default=datetime.now(timezone.utc), nullable=False)
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc), nullable=False)
