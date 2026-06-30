from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from services.role_service import require_roles

from database import get_db

from schemas.inventory import (
    InventoryCreate,
    InventoryUpdate,
    InventoryResponse,
    StockUpdate
)

from services.inventory_service import (
    create_inventory,
    get_all_inventory,
    get_inventory_by_id,
    update_inventory,
    delete_inventory,
    stock_in,
    stock_out,
    low_stock_alert
)

router = APIRouter(
    prefix="/inventory",
    tags=["Inventory"]
)


@router.post("/", response_model=InventoryResponse)
def create(
    inventory: InventoryCreate,
    db: Session = Depends(get_db),
    current_user=Depends(
    require_roles(
        "Admin",
        "Manager"
    )
)
):
    return create_inventory(
        inventory,
        db
    )


@router.get("/", response_model=list[InventoryResponse])
def get_all(
    db: Session = Depends(get_db)
):
    return get_all_inventory(db)


@router.get("/{inventory_id}", response_model=InventoryResponse)
def get_one(
    inventory_id: int,
    db: Session = Depends(get_db)
):
    return get_inventory_by_id(
        inventory_id,
        db
    )


@router.put("/{inventory_id}", response_model=InventoryResponse)
def update(
    inventory_id: int,
    inventory: InventoryUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(
    require_roles(
        "Admin",
        "Manager"
    )
)
):
    return update_inventory(
        inventory_id,
        inventory,
        db
    )


@router.delete("/{inventory_id}")
def delete(
    inventory_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(
    require_roles(
        "Admin",
        "Manager"
    )
)
):
    return delete_inventory(
        inventory_id,
        db
    )


@router.put("/{inventory_id}/stock-in", response_model=InventoryResponse)
def add_stock(
    inventory_id: int,
    stock: StockUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(
    require_roles(
        "Admin",
        "Manager"
    )
)
):
    return stock_in(
        inventory_id,
        stock,
        db
    )


@router.put("/{inventory_id}/stock-out", response_model=InventoryResponse)
def remove_stock(
    inventory_id: int,
    stock: StockUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(
    require_roles(
        "Admin",
        "Manager"
    )
)
):
    return stock_out(
        inventory_id,
        stock,
        db
    )


@router.get("/low-stock", response_model=list[InventoryResponse])
def low_stock(
    db: Session = Depends(get_db)
):
    return low_stock_alert(db)