from pydantic import (
    BaseModel,
    EmailStr,
)


class Token(BaseModel):
    access_token: str
    token_type: str


class SignInRequest(BaseModel):
    user_email: EmailStr
    user_password: str

