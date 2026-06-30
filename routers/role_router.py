from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db

from schemas.role import (
    RoleCreate,
    RoleResponse
)

from services.role_service import (
    create_role,
    get_all_roles,
    get_role_by_id,
    delete_role
)

router = APIRouter(
    prefix="/roles",
    tags=["Roles"]
)


@router.post(
    "/",
    response_model=RoleResponse
)
def create(
    role: RoleCreate,
    db: Session = Depends(get_db)
):
    return create_role(
        role,
        db
    )


@router.get(
    "/",
    response_model=list[RoleResponse]
)
def get_all(
    db: Session = Depends(get_db)
):
    return get_all_roles(db)


@router.get(
    "/{role_id}",
    response_model=RoleResponse
)
def get_one(
    role_id: int,
    db: Session = Depends(get_db)
):
    return get_role_by_id(
        role_id,
        db
    )


@router.delete("/{role_id}")
def delete(
    role_id: int,
    db: Session = Depends(get_db)
):
    return delete_role(
        role_id,
        db
    )