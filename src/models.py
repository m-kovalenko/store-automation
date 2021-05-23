import datetime

from sqlalchemy import Column, Integer, DateTime, Index
from sqlalchemy.ext.declarative import declarative_base


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


class User(Base, MainFieldsMixin, DictMethodsMixin):
    __tablename__ = 'user'


Index('posted_articles__id__index', User.id)

