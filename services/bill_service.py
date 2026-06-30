from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.bill import Bill
from models.order import Order

from schemas.bill import (
    BillCreate,
    TaxUpdate,
    DiscountUpdate,
    PaymentStatusUpdate
)


def generate_bill(
    bill: BillCreate,
    db: Session
):

    order = (
        db.query(Order)
        .filter(Order.id == bill.order_id)
        .first()
    )

    if not order:
        raise HTTPException(
            status_code=404,
            detail="Order not found"
        )

    total = (
        bill.subtotal +
        bill.tax -
        bill.discount
    )

    db_bill = Bill(
        order_id=bill.order_id,
        subtotal=bill.subtotal,
        tax=bill.tax,
        discount=bill.discount,
        total_amount=total
    )

    db.add(db_bill)
    db.commit()
    db.refresh(db_bill)

    return db_bill


def apply_tax(
    bill_id: int,
    tax_data: TaxUpdate,
    db: Session
):

    bill = (
        db.query(Bill)
        .filter(Bill.id == bill_id)
        .first()
    )

    if not bill:
        raise HTTPException(
            status_code=404,
            detail="Bill not found"
        )

    bill.tax = tax_data.tax

    bill.total_amount = (
        bill.subtotal +
        bill.tax -
        bill.discount
    )

    db.commit()
    db.refresh(bill)

    return bill


def apply_discount(
    bill_id: int,
    discount_data: DiscountUpdate,
    db: Session
):

    bill = (
        db.query(Bill)
        .filter(Bill.id == bill_id)
        .first()
    )

    if not bill:
        raise HTTPException(
            status_code=404,
            detail="Bill not found"
        )

    bill.discount = discount_data.discount

    bill.total_amount = (
        bill.subtotal +
        bill.tax -
        bill.discount
    )

    db.commit()
    db.refresh(bill)

    return bill


def update_payment_status(
    bill_id: int,
    payment: PaymentStatusUpdate,
    db: Session
):

    bill = (
        db.query(Bill)
        .filter(Bill.id == bill_id)
        .first()
    )

    if not bill:
        raise HTTPException(
            status_code=404,
            detail="Bill not found"
        )

    bill.payment_status = payment.payment_status

    db.commit()
    db.refresh(bill)

    return bill