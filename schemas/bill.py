from decimal import Decimal

from pydantic import BaseModel
from pydantic import ConfigDict


class BillCreate(BaseModel):

    order_id: int

    subtotal: Decimal

    tax: Decimal = 0

    discount: Decimal = 0


class TaxUpdate(BaseModel):

    tax: Decimal


class DiscountUpdate(BaseModel):

    discount: Decimal


class PaymentStatusUpdate(BaseModel):

    payment_status: str


class BillResponse(BaseModel):

    id: int

    order_id: int

    subtotal: Decimal

    tax: Decimal

    discount: Decimal

    total_amount: Decimal

    payment_status: str

    model_config = ConfigDict(
        from_attributes=True
    )