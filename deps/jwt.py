from datetime import datetime
from typing import Annotated

import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer
from sqlalchemy.orm import Session

from config.config import JWT_SECRET
from db.database import get_db
from schemas.auth import TokenPayload

DB = Annotated[Session, Depends(get_db)]
oauth2_scheme = HTTPBearer()


def get_current_user(token: HTTPBearer = Depends(oauth2_scheme)):
    try:
        decoded: TokenPayload = jwt.decode(token.credentials, JWT_SECRET, "HS256")
        if decoded is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="unauthorized"
            )
        return decoded
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="unauthorized"
        )
    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="invalid token"
        )
