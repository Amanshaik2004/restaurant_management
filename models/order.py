from sqlalchemy import (
    Column,
    Integer,
    String,
    Enum,
    DateTime,
    ForeignKey
)
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from database import Base


class Order(Base):

    __tablename__ = "orders"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    customer_name = Column(
        String(100),
        nullable=False
    )

    restaurant_id = Column(
        Integer,
        ForeignKey("restaurants.id"),
        nullable=False
    )

    table_id = Column(
        Integer,
        ForeignKey("restaurant_tables.id"),
        nullable=False
    )

    order_status = Column(
        Enum(
            "Pending",
            "Preparing",
            "Ready",
            "Completed",
            "Cancelled",
            name="order_status"
        ),
        default="Pending"
    )

    order_time = Column(
        DateTime,
        server_default=func.now()
    )

    restaurant = relationship("Restaurant")

    table = relationship("RestaurantTable")