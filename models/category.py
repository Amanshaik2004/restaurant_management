from sqlalchemy import Column, Integer, String

from database import Base


class Category(Base):

    __tablename__ = "categories"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    category_name = Column(
        String(100),
        unique=True,
        nullable=False
    )

    description = Column(
        String(255)
    )