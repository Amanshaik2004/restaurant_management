from datetime import time

from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import ConfigDict


class RestaurantCreate(BaseModel):

    restaurant_name: str

    owner_name: str

    email: EmailStr

    phone: str

    address: str

    opening_time: time

    closing_time: time


class RestaurantUpdate(BaseModel):

    restaurant_name: str

    owner_name: str

    email: EmailStr

    phone: str

    address: str

    opening_time: time

    closing_time: time


class RestaurantResponse(BaseModel):

    id: int

    restaurant_name: str

    owner_name: str

    email: EmailStr

    phone: str

    address: str

    opening_time: time

    closing_time: time

    model_config = ConfigDict(
        from_attributes=True
    )