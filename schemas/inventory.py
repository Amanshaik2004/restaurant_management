from decimal import Decimal

from pydantic import BaseModel
from pydantic import ConfigDict


class InventoryCreate(BaseModel):

    ingredient_name: str

    quantity: Decimal

    unit: str

    minimum_stock: Decimal


class InventoryUpdate(BaseModel):

    ingredient_name: str

    quantity: Decimal

    unit: str

    minimum_stock: Decimal


class StockUpdate(BaseModel):

    quantity: Decimal


class InventoryResponse(BaseModel):

    id: int

    ingredient_name: str

    quantity: Decimal

    unit: str

    minimum_stock: Decimal

    model_config = ConfigDict(
        from_attributes=True
    )