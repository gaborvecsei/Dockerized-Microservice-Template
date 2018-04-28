from sqlalchemy import Column, Integer, String, BigInteger, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.types import DateTime

from database import db


class ApiKey(db.Base):
    __tablename__ = "api_key"

    # Auto incrementing ID
    id = Column(Integer, primary_key=True)
    api_key = Column(String(256), unique=True)
    date_created = Column(DateTime())
    date_last_used = Column(DateTime())
    active = Column(Boolean, default=True)


class User(db.Base):
    __tablename__ = "user"

    # Auto incrementing ID
    id = Column(Integer, primary_key=True)
    first_name = Column(String(256))
    last_name = Column(String(256))
    email = Column(String(256), unique=True)
    date_signed_up = Column(DateTime())
    available_units = Column(BigInteger)
    used_units = Column(BigInteger)

    # Foreign Key
    api_key_id = Column(Integer, ForeignKey(ApiKey.id))
    api_key = relationship(ApiKey)
