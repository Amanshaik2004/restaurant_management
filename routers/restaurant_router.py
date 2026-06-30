from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db

from schemas.restaurant import (
    RestaurantCreate,
    RestaurantUpdate,
    RestaurantResponse
)
from services.role_service import require_roles

from services.restaurant_service import (
    create_restaurant,
    get_all_restaurants,
    get_restaurant_by_id,
    update_restaurant,
    delete_restaurant
)

router = APIRouter(
    prefix="/restaurants",
    tags=["Restaurants"]
)


@router.post("/", response_model=RestaurantResponse)
def create(
    restaurant: RestaurantCreate,
    db: Session = Depends(get_db),
    current_user=Depends(
        require_roles(
            "Admin",
            "Manager"
        )
    )
):

    return create_restaurant(
        restaurant,
        db
    )


@router.get(
    "/",
    response_model=list[RestaurantResponse]
)
def get_all(
    db: Session = Depends(get_db)
):
    return get_all_restaurants(db)


@router.get(
    "/{restaurant_id}",
    response_model=RestaurantResponse
)
def get_one(
    restaurant_id: int,
    db: Session = Depends(get_db)
):
    return get_restaurant_by_id(
        restaurant_id,
        db
    )


@router.put("/{restaurant_id}", response_model=RestaurantResponse)
def update(
    restaurant_id: int,
    restaurant: RestaurantUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(
        require_roles(
            "Admin",
            "Manager"
        )
    )
):
    return update_restaurant(
        restaurant_id,
        restaurant,
        db
    )


@router.delete("/{restaurant_id}")
def delete(
    restaurant_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(
        require_roles(
            "Admin",
            "Manager"
        )
    )
):
    return delete_restaurant(
        restaurant_id,
        db
    )