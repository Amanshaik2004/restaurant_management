from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db

from schemas.notification import NotificationResponse

from services.notification_service import (
    order_confirmation,
    order_ready,
    table_reservation_confirmation
)

router = APIRouter(
    prefix="/notifications",
    tags=["Notifications"]
)


@router.post(
    "/order-confirmation",
    response_model=NotificationResponse
)
def confirm_order(
    db: Session = Depends(get_db)
):
    return order_confirmation(db)


@router.post(
    "/order-ready",
    response_model=NotificationResponse
)
def ready_order(
    db: Session = Depends(get_db)
):
    return order_ready(db)


@router.post(
    "/table-reservation",
    response_model=NotificationResponse
)
def reserve_table(
    db: Session = Depends(get_db)
):
    return table_reservation_confirmation(db)