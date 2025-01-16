from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from url_shortener.config import get_settings

engine = create_engine(get_settings().db_uri, connect_args={"check_same_thread": False})  # Check same thread for SQLite to allow multi requests at a time

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
