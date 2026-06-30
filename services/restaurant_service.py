from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.restaurant import Restaurant
from schemas.restaurant import RestaurantCreate, RestaurantUpdate


from fastapi import HTTPException

from models.restaurant import Restaurant


def create_restaurant(
    restaurant,
    db
):

    existing_email = (
        db.query(Restaurant)
        .filter(
            Restaurant.email == restaurant.email
        )
        .first()
    )

    if existing_email:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    existing_phone = (
        db.query(Restaurant)
        .filter(
            Restaurant.phone == restaurant.phone
        )
        .first()
    )

    if existing_phone:
        raise HTTPException(
            status_code=400,
            detail="Phone number already exists"
        )

    db_restaurant = Restaurant(
        **restaurant.model_dump()
    )

    db.add(db_restaurant)

    db.commit()

    db.refresh(db_restaurant)

    return db_restaurant

def get_all_restaurants(
    db: Session
):

    return db.query(Restaurant).all()


def get_restaurant_by_id(
    restaurant_id: int,
    db: Session
):

    restaurant = (
        db.query(Restaurant)
        .filter(Restaurant.id == restaurant_id)
        .first()
    )

    if not restaurant:

        raise HTTPException(
            404,
            "Restaurant not found"
        )

    return restaurant


def update_restaurant(
    restaurant_id: int,
    restaurant_data: RestaurantUpdate,
    db: Session
):

    restaurant = (
        db.query(Restaurant)
        .filter(Restaurant.id == restaurant_id)
        .first()
    )

    if not restaurant:

        raise HTTPException(
            404,
            "Restaurant not found"
        )

    for key, value in restaurant_data.model_dump().items():
        setattr(
            restaurant,
            key,
            value
        )

    db.commit()

    db.refresh(restaurant)

    return restaurant


def delete_restaurant(
    restaurant_id: int,
    db: Session
):

    restaurant = (
        db.query(Restaurant)
        .filter(Restaurant.id == restaurant_id)
        .first()
    )

    if not restaurant:

        raise HTTPException(
            404,
            "Restaurant not found"
        )

    db.delete(restaurant)

    db.commit()

    return {
        "message":"Restaurant deleted successfully"
    }