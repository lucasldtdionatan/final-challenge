import enum
from typing import List
from uuid import UUID, uuid4
from decimal import Decimal
from datetime import datetime, timezone

from sqlmodel import SQLModel, Field, Relationship

from src.utils import generate_reference


class StatusEnum(str, enum.Enum):
    pending = "pending"
    paid = "paid"
    delivered = "delivered"
    cancelled = "cancelled"


class Order(SQLModel, table=True):
    id: UUID | None = Field(default_factory=uuid4, primary_key=True, unique=True)
    reference: str = Field(default_factory=lambda: generate_reference("O-"), max_length=8, nullable=False)
    buyer_id: UUID = Field(nullable=False, foreign_key="user.id")
    status: StatusEnum = Field(max_length=20, nullable=False, default=StatusEnum.pending.value)
    created_at: datetime | None = Field(default=datetime.now(timezone.utc), nullable=False)
    updated_at: datetime | None = Field(default_factory=lambda: datetime.now(timezone.utc), nullable=False)

    items: list["OrderItems"] = Relationship(back_populates="order")

    @property
    def total_price(self) -> Decimal:
        return sum(item.price * item.quantity for item in self.items)


class OrderItems(SQLModel, table=True):
    id: UUID | None = Field(default_factory=uuid4, primary_key=True, unique=True)
    order_id: UUID = Field(nullable=False, foreign_key="order.id")
    product_id: int = Field(nullable=False, foreign_key="product.id")
    quantity: int = Field(nullable=False)
    price: Decimal = Field(nullable=False)
    delivered_at: datetime = Field(nullable=True)
    
    order: Order | None = Relationship(back_populates="items")