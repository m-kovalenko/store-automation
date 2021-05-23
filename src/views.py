from fastapi import APIRouter
from loguru import logger


router = APIRouter()


@logger.catch
@router.get("/")
def index():
    return {'text': 'hi'}
