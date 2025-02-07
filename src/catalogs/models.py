from uuid import UUID
from decimal import Decimal
from datetime import datetime, timezone

from sqlmodel import SQLModel, Field

from src.utils import generate_reference


class Category(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(max_length=128, nullable=False)
    created_at: datetime | None = Field(default=datetime.now(timezone.utc), nullable=False)
    updated_at: datetime | None = Field(default_factory=lambda: datetime.now(timezone.utc), nullable=False)


class Product(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(max_length=128, nullable=False)
    sku: str | None = Field(default_factory=lambda: generate_reference("PR-"), max_length=8)
    price: Decimal = Field(nullable=False)
    stock: int = Field(default=Decimal("0"), nullable=False)
    is_active: bool = Field(default=True, nullable=False)
    seller_id: UUID = Field(nullable=False, foreign_key="user.id")
    category_id: int = Field(nullable=False, foreign_key="category.id")
    created_at: datetime | None = Field(default=datetime.now(timezone.utc), nullable=False)
    updated_at: datetime | None = Field(default_factory=lambda: datetime.now(timezone.utc), nullable=False)
