from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db

from schemas.restaurant_table import (
    RestaurantTableCreate,
    RestaurantTableUpdate,
    RestaurantTableResponse
)
from services.role_service import require_roles
from services.restaurant_table_service import (
    create_table,
    get_all_tables,
    get_table_by_id,
    update_table,
    delete_table,
    reserve_table
)

router = APIRouter(
    prefix="/tables",
    tags=["Restaurant Tables"]
)


@router.post("/", response_model=RestaurantTableResponse)
def create(
    table: RestaurantTableCreate,
    db: Session = Depends(get_db),
    current_user=Depends(
    require_roles(
        "Admin",
        "Manager",
        "Waiter"
    )
)
):
    return create_table(table, db)


@router.get("/", response_model=list[RestaurantTableResponse])
def get_all(
    db: Session = Depends(get_db)
):
    return get_all_tables(db)


@router.get("/{table_id}", response_model=RestaurantTableResponse)
def get_one(
    table_id: int,
    db: Session = Depends(get_db)
):
    return get_table_by_id(table_id, db)


@router.put("/{table_id}", response_model=RestaurantTableResponse)
def update(
    table_id: int,
    table: RestaurantTableUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(
    require_roles(
        "Admin",
        "Manager",
        "Waiter"
    )
)
):
    return update_table(table_id, table, db)


@router.delete("/{table_id}")
def delete(
    table_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(
    require_roles(
        "Admin",
        "Manager",
        "Waiter"
    )
)
):
    return delete_table(table_id, db)


@router.put("/{table_id}/reserve")
def reserve(
    table_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(
    require_roles(
        "Admin",
        "Manager",
        "Waiter"
    )
)
):
    return reserve_table(table_id, db)