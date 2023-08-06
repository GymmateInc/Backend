from sqlalchemy import Boolean, Column, Integer, String, Float
from internal_schemes.dao.base import BaseInternal


class PostInternal(BaseInternal):
    __tablename__ = "posts"

    id = Column(String, primary_key=True, index=True)

    topic = Column(String, index=True)
    description = Column(String, index=True)
    spendedTime = Column(String, index=True, nullable=True)
    liftedKg = Column(Float, index=True, nullable=True)
    exercises = Column(Integer, index=True, nullable=True)

    selfLike = Column(Boolean, index=True, default=False)
    likes = Column(Integer, index=True, default=0)
    comments = Column(Integer, index=True, default=0)

    # # TODO
    # image = Column(String, index=True)

    owner_id = Column(String, index=True)
