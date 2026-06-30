from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from services.role_service import require_roles

from schemas.category import (
    CategoryCreate,
    CategoryUpdate,
    CategoryResponse
)

from services.category_service import (
    create_category,
    get_all_categories,
    get_category_by_id,
    update_category,
    delete_category
)

router = APIRouter(
    prefix="/categories",
    tags=["Categories"]
)


@router.post(
    "/",
    response_model=CategoryResponse
)
def create(
    category: CategoryCreate,
    db: Session = Depends(get_db),
    current_user=Depends(
    require_roles(
        "Admin",
        "Manager"
    )
)
):
    return create_category(category, db)


@router.get(
    "/",
    response_model=list[CategoryResponse]
)
def get_all(
    db: Session = Depends(get_db)
):
    return get_all_categories(db)


@router.get(
    "/{category_id}",
    response_model=CategoryResponse
)
def get_one(
    category_id: int,
    db: Session = Depends(get_db)
):
    return get_category_by_id(category_id, db)


@router.put(
    "/{category_id}",
    response_model=CategoryResponse
)
def update(
    category_id: int,
    category: CategoryUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(
    require_roles(
        "Admin",
        "Manager"
    )
)
):
    return update_category(
        category_id,
        category,
        db
    )


@router.delete("/{category_id}")
def delete(
    category_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(
    require_roles(
        "Admin",
        "Manager"
    )
)
):
    return delete_category(category_id, db)