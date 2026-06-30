from sqlalchemy import (
    Column,
    Integer,
    String,
    Time,
    DateTime
)

from sqlalchemy.sql import func

from database import Base


class Restaurant(Base):

    __tablename__ = "restaurants"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    restaurant_name = Column(
        String(100),
        nullable=False
    )

    owner_name = Column(
        String(100),
        nullable=False
    )

    email = Column(
        String(100),
        unique=True,
        nullable=False
    )

    phone = Column(
        String(15),
        unique=True,
        nullable=False
    )

    address = Column(
        String(255),
        nullable=False
    )

    opening_time = Column(
        Time,
        nullable=False
    )

    closing_time = Column(
        Time,
        nullable=False
    )

    created_at = Column(
        DateTime,
        server_default=func.now()
    )