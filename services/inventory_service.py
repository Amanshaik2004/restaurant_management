from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.inventory import Inventory

from schemas.inventory import (
    InventoryCreate,
    InventoryUpdate,
    StockUpdate
)


def create_inventory(
    inventory: InventoryCreate,
    db: Session
):

    db_inventory = Inventory(
        **inventory.model_dump()
    )

    db.add(db_inventory)
    db.commit()
    db.refresh(db_inventory)

    return db_inventory


def get_all_inventory(
    db: Session
):

    return db.query(Inventory).all()


def get_inventory_by_id(
    inventory_id: int,
    db: Session
):

    inventory = (
        db.query(Inventory)
        .filter(Inventory.id == inventory_id)
        .first()
    )

    if not inventory:
        raise HTTPException(
            status_code=404,
            detail="Ingredient not found"
        )

    return inventory


def update_inventory(
    inventory_id: int,
    inventory_data: InventoryUpdate,
    db: Session
):

    inventory = (
        db.query(Inventory)
        .filter(Inventory.id == inventory_id)
        .first()
    )

    if not inventory:
        raise HTTPException(
            status_code=404,
            detail="Ingredient not found"
        )

    for key, value in inventory_data.model_dump().items():
        setattr(
            inventory,
            key,
            value
        )

    db.commit()
    db.refresh(inventory)

    return inventory


def delete_inventory(
    inventory_id: int,
    db: Session
):

    inventory = (
        db.query(Inventory)
        .filter(Inventory.id == inventory_id)
        .first()
    )

    if not inventory:
        raise HTTPException(
            status_code=404,
            detail="Ingredient not found"
        )

    db.delete(inventory)
    db.commit()

    return {
        "message": "Ingredient deleted successfully"
    }


def stock_in(
    inventory_id: int,
    stock: StockUpdate,
    db: Session
):

    inventory = (
        db.query(Inventory)
        .filter(Inventory.id == inventory_id)
        .first()
    )

    if not inventory:
        raise HTTPException(
            status_code=404,
            detail="Ingredient not found"
        )

    inventory.quantity += stock.quantity

    db.commit()
    db.refresh(inventory)

    return inventory


def stock_out(
    inventory_id: int,
    stock: StockUpdate,
    db: Session
):

    inventory = (
        db.query(Inventory)
        .filter(Inventory.id == inventory_id)
        .first()
    )

    if not inventory:
        raise HTTPException(
            status_code=404,
            detail="Ingredient not found"
        )

    if inventory.quantity < stock.quantity:
        raise HTTPException(
            status_code=400,
            detail="Insufficient Stock"
        )

    inventory.quantity -= stock.quantity

    db.commit()
    db.refresh(inventory)

    return inventory


def low_stock_alert(
    db: Session
):

    return (
        db.query(Inventory)
        .filter(
            Inventory.quantity <= Inventory.minimum_stock
        )
        .all()
    )