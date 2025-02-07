from uuid import UUID
from fastapi import APIRouter, Response, status

from src.dependencies import DBSession
from src.orders import controllers
from src.orders.schemas import ListOrderItemsSchema, ListOrderSchema, OrderCreateSchema, OrderItemResponse, OrderPartialUpdateSchema, OrderResponse, OrderUpdateSchema

router = APIRouter(prefix="/orders", tags=["orders"])


@router.post("/", response_model=OrderResponse)
async def create_order(data: OrderCreateSchema, session: DBSession) -> OrderResponse:
    order = await controllers.create_order(data=data, session=session)
    return order


@router.get("/{id}", response_model=OrderResponse)
async def get_order(id: UUID, session: DBSession) -> OrderResponse:
    return await controllers.get_order(id=id, session=session)


@router.get("/", response_model=ListOrderSchema)
async def get_orders(session: DBSession) -> ListOrderSchema:
    orders = await controllers.get_orders(session=session)
    return ListOrderSchema(count=len(orders), items=orders)


@router.patch("/{id}", response_model=OrderResponse)
async def partial_update_order(id: UUID, order: OrderPartialUpdateSchema, session: DBSession) -> OrderResponse:
    return await controllers.update_order(id=id, data=order, session=session)


@router.put("/{id}", response_model=OrderResponse)
async def update_order(id: UUID, order: OrderUpdateSchema, session: DBSession) -> OrderResponse:
    return await controllers.update_order(id=id, data=order, session=session)


@router.delete("/{id}", response_model=OrderResponse)
async def delete_order(id: UUID, session: DBSession) -> OrderResponse:
    await controllers.remove_order(id=id, session=session)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.get("/items/", response_model=ListOrderItemsSchema)
async def get_order_items(session: DBSession) -> ListOrderItemsSchema:
    order_items = await controllers.get_order_items(session=session)
    return ListOrderItemsSchema(count=len(order_items), items=order_items)

@router.get("/items/{id}", response_model=OrderItemResponse)
async def get_order_item(id: UUID, session: DBSession) -> OrderItemResponse:
    return await controllers.get_order_item(id=id, session=session)