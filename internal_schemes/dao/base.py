import uuid

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from settings import app_settings

BaseInternal = declarative_base()
_engine = create_engine(
    url=app_settings.database_url,
    connect_args={"check_same_thread": False},
    echo=True
)


def init_models():
    BaseInternal.metadata.create_all(bind=_engine)


class BaseDao:

    def __init__(self):
        self._SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=_engine)
        self.session = self._SessionLocal()

    @staticmethod
    def generate_id(prefix: str = "") -> str:
        """Common way for ID generation - nake uuid as string"""
        return f"{prefix}-{uuid.uuid4()}"

    def __del__(self):
        self.session.close()
