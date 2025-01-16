from sqlalchemy import Boolean, Column, Integer, String

from url_shortener.database import Base

class URL(Base):
    __tablename__ = "urls"

    id = Column(Integer, primary_key=True)
    short_url_key = Column(String, unique=True, index=True)
    target_url = Column(String, index=True)
    is_active = Column(Boolean, default=True)
    clicks = Column(Integer, default=0)
    secret_key = Column(String, unique=True, index=True)

