from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.role import Role

from schemas.role import RoleCreate


def create_role(
    role: RoleCreate,
    db: Session
):

    existing_role = (
        db.query(Role)
        .filter(Role.role_name == role.role_name)
        .first()
    )

    if existing_role:
        raise HTTPException(
            status_code=400,
            detail="Role already exists"
        )

    new_role = Role(
        role_name=role.role_name
    )

    db.add(new_role)

    db.commit()

    db.refresh(new_role)

    return new_role


def get_all_roles(db: Session):

    return db.query(Role).all()


def get_role_by_id(
    role_id: int,
    db: Session
):

    role = (
        db.query(Role)
        .filter(Role.id == role_id)
        .first()
    )

    if not role:
        raise HTTPException(
            status_code=404,
            detail="Role not found"
        )

    return role


def delete_role(
    role_id: int,
    db: Session
):

    role = (
        db.query(Role)
        .filter(Role.id == role_id)
        .first()
    )

    if not role:
        raise HTTPException(
            status_code=404,
            detail="Role not found"
        )

    db.delete(role)

    db.commit()

    return {
        "message": "Role deleted successfully"
    }

from fastapi import Depends, HTTPException

from services.security_service import get_current_user


def require_roles(*roles):

    def role_checker(
        current_user=Depends(get_current_user)
    ):

        if current_user.role.role_name not in roles:

            raise HTTPException(
                status_code=403,
                detail="Permission Denied"
            )

        return current_user

    return role_checker