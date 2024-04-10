from typing import Annotated, List

import bcrypt
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from db.database import get_db
from deps.jwt import get_current_user
from models.users import Users
from schemas.common_reponse import CommonResponse
from schemas.users import AddUser, UserResponse

router = APIRouter(prefix="/users", tags=["User"])

DB = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]


@router.post("/", status_code=status.HTTP_201_CREATED)
def add_user(user: AddUser, db: DB) -> UserResponse:
    new_user = Users(**user.model_dump())
    new_user.password = bcrypt.hashpw(user.password.encode(), bcrypt.gensalt()).decode()
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get("/")
def get_user(user: user_dependency, db: DB) -> List[UserResponse]:
    users = db.query(Users).order_by(Users.created_at.desc()).all()
    return users


@router.get("/{user_id}")
def get_user_by_id(user_id: str, db: DB) -> UserResponse:
    user = db.query(Users).get(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="user not found")
    return user


@router.put("/{user_id}")
def update_user_by_id(user: AddUser, user_id: str, db: DB) -> UserResponse:
    update_user = get_user_by_id(user_id=user_id, db=db)
    if update_user is None:
        raise HTTPException(status_code=404, detail="user not found")
    update_user.id = user_id
    update_user.name = user.name
    update_user.age = user.age
    update_user.is_qualified = user.is_qualified
    db.commit()
    db.refresh(update_user)
    return update_user


@router.delete("/{user_id}")
def delete_user_by_id(user_id: str, db: DB) -> CommonResponse:
    user = db.query(Users).get(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="user not found")
    db.delete(user)
    db.commit()
    return {"message": "success"}
