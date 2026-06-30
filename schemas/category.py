from pydantic import BaseModel
from pydantic import ConfigDict


class CategoryCreate(BaseModel):

    category_name: str

    description: str


class CategoryUpdate(BaseModel):

    category_name: str

    description: str


class CategoryResponse(BaseModel):

    id: int

    category_name: str

    description: str

    model_config = ConfigDict(
        from_attributes=True
    )