from sqlalchemy import (
    Column,
    Integer,
    DECIMAL,
    ForeignKey
)

from sqlalchemy.orm import relationship

from database import Base


class OrderItem(Base):

    __tablename__ = "order_items"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    order_id = Column(
        Integer,
        ForeignKey("orders.id"),
        nullable=False
    )

    menu_item_id = Column(
        Integer,
        ForeignKey("menu_items.id"),
        nullable=False
    )

    quantity = Column(
        Integer,
        nullable=False
    )

    price = Column(
        DECIMAL(10,2),
        nullable=False
    )

    order = relationship("Order")

    menu_item = relationship("MenuItem")