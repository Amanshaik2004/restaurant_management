from sqlalchemy import (
    Column,
    Integer,
    Enum,
    ForeignKey
)

from sqlalchemy.orm import relationship

from database import Base


class RestaurantTable(Base):

    __tablename__ = "restaurant_tables"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    table_number = Column(
        Integer,
        unique=True,
        nullable=False
    )

    capacity = Column(
        Integer,
        nullable=False
    )

    status = Column(
        Enum(
            "Available",
            "Reserved",
            "Occupied",
            name="table_status"
        ),
        default="Available"
    )

    restaurant_id = Column(
        Integer,
        ForeignKey("restaurants.id"),
        nullable=False
    )

    restaurant = relationship("Restaurant")