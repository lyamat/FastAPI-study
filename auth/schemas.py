
from fastapi_users import schemas
from typing import Generic, List, Optional, TypeVar

from pydantic import BaseModel, EmailStr

from fastapi_users import models

class UserRead(schemas.BaseUser[int]):
    id: int
    username: str
    role_id: int
    email: str
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False

    class Config:
        orm_mode = True


class UserCreate(schemas.BaseUserCreate):
    username: str
    role_id: int
    email: str
    password: str
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False
