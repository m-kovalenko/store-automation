#!/usr/local/bin/python3.9
from fastapi import FastAPI

from src.routes.product_routes import router as product_routes
from src.routes.order_routes import router as order_routes


app = FastAPI()


def setup_routes(app):
    app.include_router(product_routes)
    app.include_router(order_routes)


setup_routes(app)
