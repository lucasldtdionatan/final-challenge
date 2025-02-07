from uuid import UUID
from sqlmodel import Session, delete, select
from src.catalogs.models import Product
from src.orders import exceptions
from src.orders.models import Order, OrderItems
from src.orders.schemas import OrderCreateSchema, OrderPartialUpdateSchema, OrderUpdateSchema


async def create_order(data: OrderCreateSchema, session: Session) -> Order:
    order = Order(**data.model_dump(exclude={"items"})) 
    session.add(order)
    session.flush()

    order_items = [
        OrderItems(**item.model_dump(), order_id=order.id) for item in data.items
    ]

    products = session.exec(select(Product).where(Product.id.in_([item.product_id for item in order_items]))).all()
    for order_item, product in zip(order_items, products):
        order_item.price = product.price

    session.add_all(order_items)
    session.commit()
    session.refresh(order, ["items"])

    return order


async def get_order(id: UUID, session: Session) -> Order:
    order = session.get(Order, id)
    if not order:
        raise exceptions.OrderNotFound()
    return order


async def get_orders(session: Session) -> list[Order]:
    orders = session.exec(select(Order)).all()
    return orders


async def update_order(id: UUID, data: OrderPartialUpdateSchema | OrderUpdateSchema, session: Session) -> Order:
    order = session.get(Order, id)
    if not order:
        raise exceptions.OrderNotFound()
    
    order.sqlmodel_update(data.model_dump(exclude_unset=True))
    session.add(order)
    session.commit()
    session.refresh(order)
    return order


async def remove_order(id: UUID, session: Session) -> None:
    order = session.get(Order, id)
    if not order:
        raise exceptions.OrderNotFound()
    
    session.exec(delete(OrderItems).where(OrderItems.order_id == order.id))
    session.delete(order)
    session.commit()


async def get_order_item(id: UUID, session: Session) -> OrderItems:
    order_item = session.get(OrderItems, id)
    if not order_item:
        raise exceptions.OrderItemNotFound()
    return order_item


async def get_order_items(session: Session) -> list[OrderItems]:
    order_items = session.exec(select(OrderItems)).all()
    return order_items