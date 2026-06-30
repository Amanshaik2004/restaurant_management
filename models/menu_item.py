from sqlalchemy import (
    Column,
    Integer,
    String,
    DECIMAL,
    Boolean,
    ForeignKey
)

from sqlalchemy.orm import relationship

from database import Base


class MenuItem(Base):

    __tablename__ = "menu_items"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    item_name = Column(
        String(100),
        nullable=False
    )

    description = Column(
        String(255)
    )

    price = Column(
        DECIMAL(10,2),
        nullable=False
    )

    image_url = Column(
        String(255)
    )

    is_available = Column(
        Boolean,
        default=True
    )

    category_id = Column(
        Integer,
        ForeignKey("categories.id"),
        nullable=False
    )

    image_url = Column(
    String(255)
    )

    category = relationship("Category")