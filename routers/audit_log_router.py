from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from services.role_service import require_roles

from schemas.audit_log import AuditLogResponse

from services.audit_log_service import (
    track_login,
    order_update,
    menu_change,
    billing_activity
)

router = APIRouter(
    prefix="/audit-logs",
    tags=["Audit Logs"]
)


@router.post(
    "/login/{user_id}",
    response_model=AuditLogResponse
)
def login_log(
    user_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(
    require_roles(
        "Admin"
    )
)
):
    return track_login(
        user_id,
        db
    )


@router.post(
    "/order-update/{user_id}",
    response_model=AuditLogResponse
)
def order_log(
    user_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(
    require_roles(
        "Admin"
    )
)
):
    return order_update(
        user_id,
        db
    )


@router.post(
    "/menu-change/{user_id}",
    response_model=AuditLogResponse
)
def menu_log(
    user_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(
    require_roles(
        "Admin"
    )
)
):
    return menu_change(
        user_id,
        db
    )


@router.post(
    "/billing/{user_id}",
    response_model=AuditLogResponse
)
def billing_log(
    user_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(
    require_roles(
        "Admin"
    )
)
):
    return billing_activity(
        user_id,
        db
    )