from datetime import datetime
from decimal import Decimal
from uuid import UUID
from sqlmodel import SQLModel

from src.orders.models import StatusEnum


class OrderResponse(SQLModel):
    class OrderItemResponse(SQLModel):
        id: UUID
        product_id: int
        quantity: int
        price: Decimal

    id: UUID
    reference: str
    buyer_id: UUID
    status: str
    created_at: datetime
    updated_at: datetime
    total_price: Decimal
    items: list[OrderItemResponse]


class OrderCreateSchema(SQLModel):
    class OrderItemCreateSchema(SQLModel):
        product_id: int
        quantity: int

    buyer_id: UUID
    items: list[OrderItemCreateSchema]


class OrderPartialUpdateSchema(SQLModel):
    price: Decimal | None = None
    tax: Decimal | None = None
    status: StatusEnum | None = None


class OrderUpdateSchema(SQLModel):
    buyer_id: UUID
    status: StatusEnum


class ListOrderSchema(SQLModel):
    count: int
    items: list[OrderResponse]


class OrderItemResponse(SQLModel):
    id: UUID
    product_id: int
    quantity: int
    price: Decimal
    delivered_at: datetime | None = None
    order_id: UUID


class ListOrderItemsSchema(SQLModel):
    count: int
    items: list[OrderItemResponse]