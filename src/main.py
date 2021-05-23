#!/usr/local/bin/python3.9
from fastapi import FastAPI

from src.views import router


app = FastAPI()


def setup_routes(app):
    app.include_router(router)


setup_routes(app)
