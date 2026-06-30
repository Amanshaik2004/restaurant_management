from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.order import Order
from models.order_item import OrderItem
from models.restaurant import Restaurant
from models.restaurant_table import RestaurantTable
from models.menu_item import MenuItem

from schemas.order import (
    OrderCreate,
    OrderUpdate
)

from schemas.order_item import OrderItemCreate


def create_order(
    order: OrderCreate,
    items: list[OrderItemCreate],
    db: Session
):

    restaurant = db.query(Restaurant).filter(
        Restaurant.id == order.restaurant_id
    ).first()

    if not restaurant:
        raise HTTPException(404, "Restaurant not found")

    table = db.query(RestaurantTable).filter(
        RestaurantTable.id == order.table_id
    ).first()

    if not table:
        raise HTTPException(404, "Table not found")

    db_order = Order(
        **order.model_dump()
    )

    db.add(db_order)

    db.flush()

    for item in items:

        menu = db.query(MenuItem).filter(
            MenuItem.id == item.menu_item_id
        ).first()

        if not menu:
            raise HTTPException(
                404,
                "Menu Item not found"
            )

        order_item = OrderItem(
            order_id=db_order.id,
            menu_item_id=item.menu_item_id,
            quantity=item.quantity,
            price=item.price
        )

        db.add(order_item)

    db.commit()

    db.refresh(db_order)

    return db_order


def get_all_orders(db: Session):

    return db.query(Order).all()


def get_order_by_id(
    order_id: int,
    db: Session
):

    order = (
        db.query(Order)
        .filter(Order.id == order_id)
        .first()
    )

    if not order:
        raise HTTPException(404, "Order not found")

    return order


def update_order_status(
    order_id: int,
    status: OrderStatusUpdate,
    db: Session
):

    order = db.query(Order).filter(
        Order.id == order_id
    ).first()

    if not order:
        raise HTTPException(
            404,
            "Order not found"
        )

    order.order_status = status.order_status

    db.commit()

    db.refresh(order)

    return order


def cancel_order(
    order_id: int,
    db: Session
):

    order = db.query(Order).filter(
        Order.id == order_id
    ).first()

    if not order:
        raise HTTPException(
            404,
            "Order not found"
        )

    order.order_status = "Cancelled"

    db.commit()

    db.refresh(order)

    return {
        "message": "Order cancelled successfully"
    }


def order_history(db: Session):

    return db.query(Order).all()

def get_pending_orders(db: Session):

    return (
        db.query(Order)
        .filter(Order.order_status == "Pending")
        .all()
    )


def get_pending_orders(
    db: Session
):

    pending_orders = db.query(Order).filter(
        Order.order_status == "Pending"
    ).all()

    return pending_orders

def ready_order(
    order_id: int,
    db: Session
):

    order = db.query(Order).filter(
        Order.id == order_id
    ).first()

    if not order:
        raise HTTPException(404, "Order not found")

    order.order_status = "Ready"

    db.commit()

    return {
        "message": "Order Ready for Delivery"
    }


def complete_order(
    order_id: int,
    db: Session
):

    order = db.query(Order).filter(
        Order.id == order_id
    ).first()

    if not order:
        raise HTTPException(404, "Order not found")

    order.order_status = "Completed"

    db.commit()

    return {
        "message": "Order Completed"
    }