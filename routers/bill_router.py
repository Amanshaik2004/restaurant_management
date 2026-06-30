from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from services.role_service import require_roles

from schemas.bill import (
    BillCreate,
    TaxUpdate,
    DiscountUpdate,
    PaymentStatusUpdate,
    BillResponse
)

from services.bill_service import (
    generate_bill,
    apply_tax,
    apply_discount,
    update_payment_status
)

router = APIRouter(
    prefix="/bills",
    tags=["Billing"]
)


@router.post(
    "/",
    response_model=BillResponse
)
def generate(
    bill: BillCreate,
    db: Session = Depends(get_db),
    current_user=Depends(
    require_roles(
        "Admin",
        "Manager"
    )
)
):
    return generate_bill(
        bill,
        db
    )


@router.put(
    "/{bill_id}/tax",
    response_model=BillResponse
)
def tax(
    bill_id: int,
    tax: TaxUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(
    require_roles(
        "Admin",
        "Manager"
    )
)
):
    return apply_tax(
        bill_id,
        tax,
        db
    )


@router.put(
    "/{bill_id}/discount",
    response_model=BillResponse
)
def discount(
    bill_id: int,
    discount: DiscountUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(
    require_roles(
        "Admin",
        "Manager"
    )
)
):
    return apply_discount(
        bill_id,
        discount,
        db
    )


@router.put(
    "/{bill_id}/payment",
    response_model=BillResponse
)
def payment(
    bill_id: int,
    payment: PaymentStatusUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(
    require_roles(
        "Admin",
        "Manager"
    )
)
):
    return update_payment_status(
        bill_id,
        payment,
        db
    )