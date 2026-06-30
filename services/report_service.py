from sqlalchemy import func
from sqlalchemy.orm import Session

from models.bill import Bill
from models.order import Order
from models.order_item import OrderItem
from models.menu_item import MenuItem


def daily_sales(db: Session):

    total_sales = (
        db.query(
            func.sum(Bill.total_amount)
        )
        .filter(Bill.payment_status == "Paid")
        .scalar()
    )

    return {
        "daily_sales": total_sales or 0
    }


def revenue_report(db: Session):

    revenue = (
        db.query(
            func.sum(Bill.total_amount)
        )
        .filter(Bill.payment_status == "Paid")
        .scalar()
    )

    return {
        "revenue": revenue or 0
    }


def top_selling_items(db: Session):

    result = (
        db.query(
            MenuItem.item_name,
            func.sum(OrderItem.quantity).label("total_quantity")
        )
        .join(
            OrderItem,
            MenuItem.id == OrderItem.menu_item_id
        )
        .group_by(
            MenuItem.item_name
        )
        .order_by(
            func.sum(OrderItem.quantity).desc()
        )
        .all()
    )

    return result


def order_statistics(db: Session):

    total_orders = db.query(Order).count()

    pending_orders = (
        db.query(Order)
        .filter(Order.order_status == "Pending")
        .count()
    )

    completed_orders = (
        db.query(Order)
        .filter(Order.order_status == "Completed")
        .count()
    )

    cancelled_orders = (
        db.query(Order)
        .filter(Order.order_status == "Cancelled")
        .count()
    )

    return {
        "total_orders": total_orders,
        "pending_orders": pending_orders,
        "completed_orders": completed_orders,
        "cancelled_orders": cancelled_orders
    }