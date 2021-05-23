from datetime import datetime

from typing import Optional

from fastapi import APIRouter, HTTPException, Body
from loguru import logger
from pydantic import BaseModel

from src.constants import OrderStatus
from src.database import session
from src.models import Order

router = APIRouter()


class OrderIn(BaseModel):
    product_id: Optional[int]
    status: Optional[OrderStatus]


class OrderOut(BaseModel):
    id: int
    date_created: int
    product_id: int
    status: OrderStatus


@logger.catch
@router.get("/api/v1/orders")
def get_orders(
        status: OrderStatus = None,
        start_timestamp: int = None,
        end_timestamp: int = None,
        skip: int = 0,
        limit: int = 10,
):
    if limit > 64:
        raise HTTPException(status_code=400, detail='limit is too high')

    query = session.query(Order)
    if status:
        query.filter(Order.status == status)
    if start_timestamp is not None and end_timestamp is not None:
        query.filter(Order.date_created.between(datetime.fromtimestamp(start_timestamp),
                                                datetime.fromtimestamp(end_timestamp),))
    orders = query\
        .offset(skip)\
        .limit(limit)\
        .all()
    return [
        OrderOut(
            id=order.id,
            date_created=order.date_created.timestamp(),
            product_id=order.product_id,
            status=order.status,
        ) for order in orders
    ]


@logger.catch
@router.get("/api/v1/order/{order_id}")
def get_order(order_id: int):
    order = session.query(Order).get(order_id)
    return OrderOut(
        id=order.id,
        date_created=order.date_created.timestamp(),
        product_id=order.product_id,
        status=order.status,
    )


@logger.catch
@router.post("/api/v1/order/")
def add_order(order: OrderIn):
    session.add(Order(
        product_id=order.product_id,
        status=OrderStatus.in_progress,
    ))
    return


@logger.catch
@router.put("/api/v1/order/{order_id}")
def update_order(order_id: int, new_order: OrderIn):
    order = session.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404)
    order.status = new_order.status
    return
