from pydantic import BaseModel
from typing import Optional

from fastapi import APIRouter, HTTPException
from loguru import logger

from src.database import session
from src.models import Product

router = APIRouter()


class ProductOut(BaseModel):
    id: int
    date_created: int
    name: str
    price: int


@logger.catch
@router.get("/api/v1/products")
def get_products(
        skip: Optional[int] = 0,
        limit: Optional[int] = 10,
):
    if limit > 64:
        raise HTTPException(status_code=400, detail='limit is too high')

    products = session.query(Product)\
        .offset(skip)\
        .limit(limit) \
        .all()
    return [
        ProductOut(
            id=p.id,
            date_created=p.date_created.timestamp(),
            name=p.name,
            price=p.price
        ) for p in products
    ]
