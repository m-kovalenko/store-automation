#!/usr/local/bin/python3.9
from src.database import session
from src.models import Product

session.bulk_save_objects([
    Product(name='Refrigerator', price=400),
    Product(name='TV', price=200),
    Product(name='Computer', price=600),
])
