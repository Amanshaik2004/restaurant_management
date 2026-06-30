from pydantic import BaseModel
from pydantic import EmailStr


class UserRegister(BaseModel):

    username: str

    email: EmailStr

    password: str

    role_id: int


class UserLogin(BaseModel):

    email: EmailStr

    password: str


class RefreshTokenRequest(BaseModel):

    refresh_token: str


class TokenResponse(BaseModel):

    access_token: str

    refresh_token: str

    token_type: str = "bearer"

class RefreshTokenRequest(BaseModel):
    refresh_token: str