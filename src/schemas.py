from datetime import date
from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    password: str
    zp: float
    growdate: date


class UserDisplay(BaseModel):
    username: str
    zp: float
    growdate: date

    class Config():
        orm_mode = True


class UserDisplayList(BaseModel):
    id: int
    username: str

    class Config():
        orm_mode = True
