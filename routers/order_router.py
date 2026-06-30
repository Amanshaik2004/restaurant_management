from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db

from services.role_service import require_roles

from schemas.order import (
    OrderCreate,
    OrderUpdate,
    OrderStatusUpdate,
    OrderResponse
)

from schemas.order_item import OrderItemCreate

from services.order_service import (
    create_order,
    get_all_orders,
    get_order_by_id,
    update_order_status,
    cancel_order,
    order_history,
    get_pending_orders
)

router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)


@router.post("/", response_model=OrderResponse)
def create(
    order: OrderCreate,
    items: List[OrderItemCreate],
    db: Session = Depends(get_db),
    current_user=Depends(
        require_roles(
            "Admin",
            "Manager",
            "Waiter"
        )
    )
):
    return create_order(order, items, db)


@router.get("/", response_model=list[OrderResponse])
def get_all(
    db: Session = Depends(get_db)
):
    return get_all_orders(db)


# Put fixed routes BEFORE /{order_id}
@router.get("/history", response_model=list[OrderResponse])
def history(
    db: Session = Depends(get_db)
):
    return order_history(db)


@router.get("/pending", response_model=list[OrderResponse])
def pending(
    db: Session = Depends(get_db)
):
    return get_pending_orders(db)


@router.get("/{order_id}", response_model=OrderResponse)
def get_one(
    order_id: int,
    db: Session = Depends(get_db)
):
    return get_order_by_id(order_id, db)


@router.put("/{order_id}/status", response_model=OrderResponse)
def update_status(
    order_id: int,
    status: OrderStatusUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(
        require_roles(
            "Admin",
            "Manager",
            "Chef",
            "Waiter"
        )
    )
):
    return update_order_status(
        order_id,
        status,
        db
    )


@router.put("/{order_id}/cancel")
def cancel(
    order_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(
        require_roles(
            "Admin",
            "Manager",
            "Waiter"
        )
    )
):
    return cancel_order(order_id, db)