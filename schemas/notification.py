from pydantic import BaseModel
from pydantic import ConfigDict


class NotificationResponse(BaseModel):

    id: int

    message: str

    status: str

    model_config = ConfigDict(
        from_attributes=True
    )