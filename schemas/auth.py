from pydantic import BaseModel


class Login(BaseModel):
    email: str
    password: str


class TokenPayload(BaseModel):
    id: str
    exp: int
