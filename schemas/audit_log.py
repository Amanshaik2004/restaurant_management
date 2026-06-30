from pydantic import BaseModel
from pydantic import ConfigDict


class AuditLogResponse(BaseModel):

    id: int

    user_id: int

    activity: str

    model_config = ConfigDict(
        from_attributes=True
    )