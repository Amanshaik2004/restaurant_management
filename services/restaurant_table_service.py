from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.restaurant import Restaurant
from models.restaurant_table import RestaurantTable

from schemas.restaurant_table import (
    RestaurantTableCreate,
    RestaurantTableUpdate
)


def create_table(
    table: RestaurantTableCreate,
    db: Session
):

    if db.query(RestaurantTable).filter(
        RestaurantTable.table_number == table.table_number
    ).first():
        raise HTTPException(400, "Table already exists")

    restaurant = db.query(Restaurant).filter(
        Restaurant.id == table.restaurant_id
    ).first()

    if not restaurant:
        raise HTTPException(404, "Restaurant not found")

    db_table = RestaurantTable(
        **table.model_dump()
    )

    db.add(db_table)
    db.commit()
    db.refresh(db_table)

    return db_table


def get_all_tables(db: Session):

    return db.query(RestaurantTable).all()


def get_table_by_id(
    table_id: int,
    db: Session
):

    table = db.query(RestaurantTable).filter(
        RestaurantTable.id == table_id
    ).first()

    if not table:
        raise HTTPException(404, "Table not found")

    return table


def update_table(
    table_id: int,
    table_data: RestaurantTableUpdate,
    db: Session
):

    table = db.query(RestaurantTable).filter(
        RestaurantTable.id == table_id
    ).first()

    if not table:
        raise HTTPException(404, "Table not found")

    for key, value in table_data.model_dump().items():
        setattr(table, key, value)

    db.commit()
    db.refresh(table)

    return table


def delete_table(
    table_id: int,
    db: Session
):

    table = db.query(RestaurantTable).filter(
        RestaurantTable.id == table_id
    ).first()

    if not table:
        raise HTTPException(404, "Table not found")

    db.delete(table)
    db.commit()

    return {
        "message": "Table deleted successfully"
    }


def reserve_table(
    table_id: int,
    db: Session
):

    table = db.query(RestaurantTable).filter(
        RestaurantTable.id == table_id
    ).first()

    if not table:
        raise HTTPException(404, "Table not found")

    table.status = "Reserved"

    db.commit()

    return {
        "message": "Table reserved successfully"
    }