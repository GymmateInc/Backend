from sqlalchemy import Column, String

from internal_schemes.dao.base import BaseInternal


class UserInternal(BaseInternal):
    __tablename__ = "users"

    id = Column(String, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=True)
    name = Column(String, index=True)
