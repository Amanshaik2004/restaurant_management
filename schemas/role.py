from pydantic import BaseModel


class RoleCreate(BaseModel):

    role_name: str


class RoleResponse(BaseModel):

    id: int

    role_name: str

    class Config:
        from_attributes = True