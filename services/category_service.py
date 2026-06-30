from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.category import Category
from schemas.category import (
    CategoryCreate,
    CategoryUpdate
)


def create_category(
    category: CategoryCreate,
    db: Session
):

    existing = (
        db.query(Category)
        .filter(Category.category_name == category.category_name)
        .first()
    )

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Category already exists"
        )

    db_category = Category(
        **category.model_dump()
    )

    db.add(db_category)
    db.commit()
    db.refresh(db_category)

    return db_category


def get_all_categories(
    db: Session
):

    return db.query(Category).all()


def get_category_by_id(
    category_id: int,
    db: Session
):

    category = (
        db.query(Category)
        .filter(Category.id == category_id)
        .first()
    )

    if not category:
        raise HTTPException(
            status_code=404,
            detail="Category not found"
        )

    return category


def update_category(
    category_id: int,
    category_data: CategoryUpdate,
    db: Session
):

    category = (
        db.query(Category)
        .filter(Category.id == category_id)
        .first()
    )

    if not category:
        raise HTTPException(
            status_code=404,
            detail="Category not found"
        )

    for key, value in category_data.model_dump().items():
        setattr(category, key, value)

    db.commit()
    db.refresh(category)

    return category


def delete_category(
    category_id: int,
    db: Session
):

    category = (
        db.query(Category)
        .filter(Category.id == category_id)
        .first()
    )

    if not category:
        raise HTTPException(
            status_code=404,
            detail="Category not found"
        )

    db.delete(category)
    db.commit()

    return {
        "message": "Category deleted successfully"
    }