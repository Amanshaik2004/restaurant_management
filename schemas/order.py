from pydantic import BaseModel
from pydantic import ConfigDict


class OrderCreate(BaseModel):

    customer_name: str

    restaurant_id: int

    table_id: int


class OrderUpdate(BaseModel):

    customer_name: str

    restaurant_id: int

    table_id: int

    order_status: str


class OrderResponse(BaseModel):

    id: int

    customer_name: str

    restaurant_id: int

    table_id: int

    order_status: str

    model_config = ConfigDict(
        from_attributes=True
    )

class OrderStatusUpdate(BaseModel):

    order_status: str