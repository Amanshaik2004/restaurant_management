from decimal import Decimal

from pydantic import BaseModel
from pydantic import ConfigDict


class MenuItemCreate(BaseModel):

    item_name: str

    description: str

    price: Decimal

    image_url: str | None = None

    category_id: int


class MenuItemUpdate(BaseModel):

    item_name: str

    description: str

    price: Decimal

    image_url: str | None = None

    is_available: bool

    category_id: int


class MenuItemResponse(BaseModel):

    id: int

    item_name: str

    description: str

    price: Decimal

    image_url: str | None

    is_available: bool

    category_id: int

    model_config = ConfigDict(
        from_attributes=True
    )