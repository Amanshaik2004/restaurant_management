from sqlalchemy import (
    Column,
    Integer,
    DECIMAL,
    Enum,
    ForeignKey
)

from sqlalchemy.orm import relationship

from database import Base


class Bill(Base):

    __tablename__ = "bills"

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

    subtotal = Column(
        DECIMAL(10,2),
        nullable=False
    )

    tax = Column(
        DECIMAL(10,2),
        default=0
    )

    discount = Column(
        DECIMAL(10,2),
        default=0
    )

    total_amount = Column(
        DECIMAL(10,2),
        nullable=False
    )

    payment_status = Column(
        Enum(
            "Pending",
            "Paid",
            name="payment_status"
        ),
        default="Pending"
    )

    order = relationship("Order")