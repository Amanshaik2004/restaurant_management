from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from fastapi import UploadFile, File
from services.role_service import require_roles

from schemas.menu_item import (
    MenuItemCreate,
    MenuItemUpdate,
    MenuItemResponse
)
from services.menu_item_service import upload_menu_image

from services.menu_item_service import (
    create_menu_item,
    get_all_menu_items,
    get_menu_item_by_id,
    update_menu_item,
    delete_menu_item
)

router = APIRouter(
    prefix="/menu-items",
    tags=["Menu Items"]
)


@router.post(
    "/",
    response_model=MenuItemResponse
)
def create(
    menu_item: MenuItemCreate,
    db: Session = Depends(get_db),
    current_user=Depends(
    require_roles(
        "Admin",
        "Manager",
        "Chef"
    )
)
):
    return create_menu_item(menu_item, db)


@router.get(
    "/",
    response_model=list[MenuItemResponse]
)
def get_all(
    db: Session = Depends(get_db)
):
    return get_all_menu_items(db)


@router.get(
    "/{item_id}",
    response_model=MenuItemResponse
)
def get_one(
    item_id: int,
    db: Session = Depends(get_db)
):
    return get_menu_item_by_id(item_id, db)


@router.put(
    "/{item_id}",
    response_model=MenuItemResponse
)
def update(
    item_id: int,
    menu_item: MenuItemUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(
    require_roles(
        "Admin",
        "Manager",
        "Chef"
    )
)
):
    return update_menu_item(
        item_id,
        menu_item,
        db
    )


@router.delete("/{item_id}")
def delete(
    item_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(
    require_roles(
        "Admin",
        "Manager",
        "Chef"
    )
)
):
    return delete_menu_item(item_id, db)

@router.post("/{item_id}/upload-image")
def upload_image(
    item_id: int,
    image: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user=Depends(
    require_roles(
        "Admin",
        "Manager",
        "Chef"
    )
)
):
    return upload_menu_image(
        item_id,
        image,
        db
    )