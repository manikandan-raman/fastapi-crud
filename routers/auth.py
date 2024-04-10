import time
from datetime import datetime, timedelta
from typing import Annotated

import bcrypt
import jwt
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from config.config import JWT_SECRET
from db.database import get_db
from models.users import Users
from schemas.auth import Login

router = APIRouter(prefix="/auth", tags=["Auth"])

DB = Annotated[Session, Depends(get_db)]


@router.post("/login")
def login(loginReq: Login, db: DB):
    user = db.query(Users).filter_by(email=loginReq.email).first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="user not found"
        )
    is_valid_password = bcrypt.checkpw(
        loginReq.password.encode("utf-8"), user.password.encode("utf-8")
    )
    if is_valid_password is False:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="incorrect password"
        )
    current_datetime = datetime.now()
    future_datetime = current_datetime + timedelta(minutes=30)
    future_epoch = int(future_datetime.timestamp())
    access_token = jwt.encode(
        {"id": str(user.id), "exp": future_epoch},
        JWT_SECRET,
        headers={"algorithm": "HS256"},
    )
    user.password = None
    return {"user": user, "access_token": access_token}
