from pydantic import BaseModel
from pydantic import ConfigDict


class RestaurantTableCreate(BaseModel):

    table_number: int

    capacity: int

    restaurant_id: int


class RestaurantTableUpdate(BaseModel):

    table_number: int

    capacity: int

    status: str

    restaurant_id: int


class RestaurantTableResponse(BaseModel):

    id: int

    table_number: int

    capacity: int

    status: str

    restaurant_id: int

    model_config = ConfigDict(
        from_attributes=True
    )