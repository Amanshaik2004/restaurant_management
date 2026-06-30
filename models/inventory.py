from sqlalchemy import (
    Column,
    Integer,
    String,
    DECIMAL
)

from database import Base


class Inventory(Base):

    __tablename__ = "inventory"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    ingredient_name = Column(
        String(100),
        nullable=False
    )

    quantity = Column(
        DECIMAL(10,2),
        nullable=False
    )

    unit = Column(
        String(20),
        nullable=False
    )

    minimum_stock = Column(
        DECIMAL(10,2),
        nullable=False
    )