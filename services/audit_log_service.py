from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.audit_log import AuditLog
from models.user import User


def track_login(
    user_id: int,
    db: Session
):

    user = db.query(User).filter(
        User.id == user_id
    ).first()

    if not user:
        raise HTTPException(404, "User not found")

    log = AuditLog(
        user_id=user_id,
        activity="User Logged In"
    )

    db.add(log)
    db.commit()
    db.refresh(log)

    return log


def order_update(
    user_id: int,
    db: Session
):

    user = db.query(User).filter(
        User.id == user_id
    ).first()

    if not user:
        raise HTTPException(404, "User not found")

    log = AuditLog(
        user_id=user_id,
        activity="Order Updated"
    )

    db.add(log)
    db.commit()
    db.refresh(log)

    return log


def menu_change(
    user_id: int,
    db: Session
):

    user = db.query(User).filter(
        User.id == user_id
    ).first()

    if not user:
        raise HTTPException(404, "User not found")

    log = AuditLog(
        user_id=user_id,
        activity="Menu Changed"
    )

    db.add(log)
    db.commit()
    db.refresh(log)

    return log


def billing_activity(
    user_id: int,
    db: Session
):

    user = db.query(User).filter(
        User.id == user_id
    ).first()

    if not user:
        raise HTTPException(404, "User not found")

    log = AuditLog(
        user_id=user_id,
        activity="Billing Activity"
    )

    db.add(log)
    db.commit()
    db.refresh(log)

    return log