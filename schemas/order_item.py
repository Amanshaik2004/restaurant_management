from decimal import Decimal

from pydantic import BaseModel
from pydantic import ConfigDict


class OrderItemCreate(BaseModel):

    menu_item_id: int

    quantity: int

    price: Decimal


class OrderItemResponse(BaseModel):

    id: int

    order_id: int

    menu_item_id: int

    quantity: int

    price: Decimal

    model_config = ConfigDict(
        from_attributes=True
    )