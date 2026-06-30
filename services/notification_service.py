from sqlalchemy.orm import Session

from models.notification import Notification


def order_confirmation(
    db: Session
):

    notification = Notification(
        message="Order Confirmed",
        status="Sent"
    )

    db.add(notification)
    db.commit()
    db.refresh(notification)

    return notification


def order_ready(
    db: Session
):

    notification = Notification(
        message="Order Ready",
        status="Sent"
    )

    db.add(notification)
    db.commit()
    db.refresh(notification)

    return notification


def table_reservation_confirmation(
    db: Session
):

    notification = Notification(
        message="Table Reservation Confirmed",
        status="Sent"
    )

    db.add(notification)
    db.commit()
    db.refresh(notification)

    return notification