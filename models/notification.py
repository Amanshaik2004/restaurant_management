from sqlalchemy import (
    Column,
    Integer,
    String,
    Enum,
    DateTime
)

from sqlalchemy.sql import func

from database import Base


class Notification(Base):

    __tablename__ = "notifications"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    message = Column(
        String(255),
        nullable=False
    )

    status = Column(
        Enum(
            "Pending",
            "Sent",
            name="notification_status"
        ),
        default="Pending"
    )

    created_at = Column(
        DateTime,
        server_default=func.now()
    )