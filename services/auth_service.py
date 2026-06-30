from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.user import User
from models.role import Role

from schemas.auth import UserRegister

from utils.password import (
    hash_password,
    verify_password
)

from utils.jwt import (
    create_access_token,
    create_refresh_token
)


def register_user(
    user: UserRegister,
    db: Session
):

    # Check Username

    existing_username = (
        db.query(User)
        .filter(User.username == user.username)
        .first()
    )

    if existing_username:
        raise HTTPException(
            status_code=400,
            detail="Username already exists"
        )

    # Check Email

    existing_email = (
        db.query(User)
        .filter(User.email == user.email)
        .first()
    )

    if existing_email:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    # Check Role

    role = (
        db.query(Role)
        .filter(Role.id == user.role_id)
        .first()
    )

    if not role:
        raise HTTPException(
            status_code=404,
            detail="Role not found"
        )

    # Hash Password

    hashed_password = hash_password(
        user.password
    )

    # Create User

    new_user = User(
        username=user.username,
        email=user.email,
        password_hash=hashed_password,
        role_id=user.role_id
    )

    db.add(new_user)

    db.commit()

    db.refresh(new_user)

    return {
        "message": "User registered successfully"
    }


def login_user(
    email: str,
    password: str,
    db: Session
):

    user = (
        db.query(User)
        .filter(User.email == email)
        .first()
    )

    if not user:

        raise HTTPException(
            status_code=401,
            detail="Invalid Email or Password"
        )

    if not verify_password(
        password,
        user.password_hash
    ):

        raise HTTPException(
            status_code=401,
            detail="Invalid Email or Password"
        )

    token_data = {
        "sub": user.email,
        "user_id": user.id,
        "role": user.role.role_name
    }

    access_token = create_access_token(
        token_data
    )

    refresh_token = create_refresh_token(
        token_data
    )

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer"
    }

from utils.jwt import (
    verify_refresh_token,
    create_access_token
)


def refresh_access_token(
    refresh_token: str
):

    payload = verify_refresh_token(refresh_token)

    if payload is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid Refresh Token"
        )

    token_data = {
        "sub": payload["sub"],
        "user_id": payload["user_id"],
        "role": payload["role"]
    }

    access_token = create_access_token(token_data)

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }