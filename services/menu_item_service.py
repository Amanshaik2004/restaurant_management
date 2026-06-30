from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.menu_item import MenuItem
from models.category import Category

from schemas.menu_item import (
    MenuItemCreate,
    MenuItemUpdate
)


def create_menu_item(
    menu_item: MenuItemCreate,
    db: Session
):

    category = (
        db.query(Category)
        .filter(Category.id == menu_item.category_id)
        .first()
    )

    if not category:
        raise HTTPException(
            status_code=404,
            detail="Category not found"
        )

    db_item = MenuItem(
        **menu_item.model_dump()
    )

    db.add(db_item)
    db.commit()
    db.refresh(db_item)

    return db_item


def get_all_menu_items(
    db: Session
):

    return db.query(MenuItem).all()


def get_menu_item_by_id(
    item_id: int,
    db: Session
):

    item = (
        db.query(MenuItem)
        .filter(MenuItem.id == item_id)
        .first()
    )

    if not item:
        raise HTTPException(
            status_code=404,
            detail="Menu Item not found"
        )

    return item


def update_menu_item(
    item_id: int,
    item_data: MenuItemUpdate,
    db: Session
):

    item = (
        db.query(MenuItem)
        .filter(MenuItem.id == item_id)
        .first()
    )

    if not item:
        raise HTTPException(
            status_code=404,
            detail="Menu Item not found"
        )

    category = (
        db.query(Category)
        .filter(Category.id == item_data.category_id)
        .first()
    )

    if not category:
        raise HTTPException(
            status_code=404,
            detail="Category not found"
        )

    for key, value in item_data.model_dump().items():
        setattr(item, key, value)

    db.commit()
    db.refresh(item)

    return item


def delete_menu_item(
    item_id: int,
    db: Session
):

    item = (
        db.query(MenuItem)
        .filter(MenuItem.id == item_id)
        .first()
    )

    if not item:
        raise HTTPException(
            status_code=404,
            detail="Menu Item not found"
        )

    db.delete(item)
    db.commit()

    return {
        "message": "Menu Item deleted successfully"
    }

from fastapi import HTTPException, UploadFile
from sqlalchemy.orm import Session

from models.menu_item import MenuItem


def upload_menu_image(
    item_id: int,
    image: UploadFile,
    db: Session
):

    menu_item = (
        db.query(MenuItem)
        .filter(MenuItem.id == item_id)
        .first()
    )

    if not menu_item:
        raise HTTPException(
            status_code=404,
            detail="Menu Item not found"
        )

    # Placeholder implementation
    # Save only the uploaded filename

    menu_item.image_url = image.filename

    db.commit()
    db.refresh(menu_item)

    return {
        "message": "Menu image uploaded successfully",
        "image_name": image.filename
    }