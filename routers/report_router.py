from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from services.role_service import require_roles

from services.report_service import (
    daily_sales,
    revenue_report,
    top_selling_items,
    order_statistics
)

router = APIRouter(
    prefix="/reports",
    tags=["Reports"]
)


@router.get("/daily-sales")
def get_daily_sales(
    db: Session = Depends(get_db),
    current_user=Depends(
    require_roles(
        "Admin"
    )
)
):
    return daily_sales(db)


@router.get("/revenue")
def get_revenue(
    db: Session = Depends(get_db),
    current_user=Depends(
    require_roles(
        "Admin"
    )
)
):
    return revenue_report(db)


@router.get("/top-selling-items")
def get_top_selling_items(
    db: Session = Depends(get_db),
    current_user=Depends(
    require_roles(
        "Admin"
    )
)
):
    return top_selling_items(db)


@router.get("/order-statistics")
def get_order_statistics(
    db: Session = Depends(get_db),
    current_user=Depends(
    require_roles(
        "Admin"
    )
)
):
    return order_statistics(db)