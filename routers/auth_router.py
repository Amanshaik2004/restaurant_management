from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from schemas.auth import RefreshTokenRequest
from services.auth_service import refresh_access_token
from database import get_db

from schemas.auth import UserRegister

from services.auth_service import (
    register_user,
    login_user
)

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/register")
def register(
    user: UserRegister,
    db: Session = Depends(get_db)
):
    return register_user(
        user,
        db
    )


@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    return login_user(
        form_data.username,
        form_data.password,
        db
    )

@router.post("/refresh-token")
def refresh_token(
    request: RefreshTokenRequest
):
    return refresh_access_token(
        request.refresh_token
    )