from typing import (
    Optional,
)
from datetime import datetime
from pydantic import (
    BaseModel,
    EmailStr,
)


class UserBase(BaseModel):
    user_name: Optional[str]
    user_surname: Optional[str]


class User(UserBase):
    user_id: int
    user_email: EmailStr
    created_at: datetime
    updated_at: datetime
    is_active: bool

    class Config:
        orm_mode = True


class UserForAuth(User):
    hashed_password: str

