import datetime

from sqlalchemy import Column, Integer, DateTime, Index, Enum, ForeignKey, String
from sqlalchemy.ext.declarative import declarative_base

from src.constants import OrderStatus, UserRole

Base = declarative_base()


class MainFieldsMixin:

    id = Column(Integer, primary_key=True, autoincrement=True)
    date_created = Column(DateTime, default=datetime.datetime.now)


class DictMethodsMixin:

    def keys(self):
        return self.__table__.columns.keys()

    def __getitem__(self, key):
        if key in self.__table__.columns.keys():
            return self.__getattribute__(key)
        else:
            raise KeyError(key)


class Product(Base, MainFieldsMixin, DictMethodsMixin):
    __tablename__ = 'product'
    name = Column(String)
    price = Column(Integer)


Index('product__id__index', Product.id)


class User(Base, MainFieldsMixin, DictMethodsMixin):
    __tablename__ = 'user'
    role = Column(Enum(UserRole))


Index('user__id__index', User.id)


class Order(Base, MainFieldsMixin, DictMethodsMixin):
    __tablename__ = 'order'
    status = Column(Enum(OrderStatus))
    product_id = Column(ForeignKey(Product.id))


Index('order__id__index', Order.id)
