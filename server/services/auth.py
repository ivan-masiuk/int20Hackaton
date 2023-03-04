from datetime import timedelta, datetime
from typing import Optional

from pydantic import EmailStr
from fastapi import (
    Depends,
    HTTPException,
    status,
)
from fastapi.security import OAuth2PasswordBearer
from jose import (
    jwt,
    JWTError,
    ExpiredSignatureError,
)

from server.schemas.users_schemas import User, UserForAuth
from server.services.hasher import Hasher
from server.services.user_actions import UsersActions, get_user_actions
from server.settings import settings


oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/login",
    auto_error=False
)


async def authenticate_user(
    email: str,
    password: str,
    user_actions: UsersActions,
) -> Optional[UserForAuth]:
    """
    Authenticates user's email and password
    :param email: The email of the user
    :param password: The password of the user
    :param user_actions: An instance of UsersActions
    :return: A UserForAuth instance if the user exists
             and password matches, else None
    """
    user = await user_actions.get_user_by_email_for_auth(
        email=email
    )

    if user is None:
        return None

    if not Hasher.verify_password(
            plain_password=password,
            hashed_password=user.hashed_password
    ):
        return None
    return user


async def auth_user_token(
    token: str = Depends(oauth2_scheme)
) -> EmailStr:
    """
    Validates the access token sent in the `Authorization` header and returns the
    email of the authenticated user.
    :param token: A string containing the access token to be validated.
    :return: An email address string representing the authenticated user, if the
             token is valid and the user is authorized. Otherwise, an HTTPException
             is raised with a corresponding error status code and detail message.
    """
    if token is None:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Token is missing"
        )
    email = valid_app_token(token=token)

    if email is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials"
        )
    return email


def valid_app_token(token: str) -> Optional[EmailStr]:
    """
    Validates app token
    :param token: The access token of the user
    :return: The email of the user if the token is valid, else None
    """
    try:
        payload = jwt.decode(
            token=token,
            key=settings.secret_key,
            algorithms=settings.algorithm,
        )

        if email := payload.get("email"):
            return email
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials"
            )

    except ExpiredSignatureError:
        raise HTTPException(
            status_code=401,
            detail="This has expired. Please fetch a new one"
        )

    except JWTError:
        return None


async def get_current_user_from_token(
    email: str = Depends(auth_user_token),
    user_actions: UsersActions = Depends(get_user_actions),
) -> User:
    """
    Authenticates user's token and retrieves user details
    :param email: The email address obtained from the access token.
    :param user_actions: An instance of UsersActions
    :return: A User object representing the authenticated user.
    :raises HTTPException: If the access token is invalid or expired, or if there
                           is an error while processing the request.
    """
    user = await user_actions.get_user_by_email(email=email)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials"
        )
    return user


def create_access_token(
        data: dict,
        expires_delta: Optional[timedelta] = None
) -> str:
    """
    Create an access token with the given data and expiration time.
    :param data: The data to encode in the access token.
    :param expires_delta: The expiration time of the token. If not provided,
                          the default expiration time from the app settings is used.
    :return: str: The encoded access token.
    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(
            minutes=settings.access_token_expire_minutes
        )
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        claims=to_encode,
        key=settings.secret_key,
        algorithm=settings.algorithm
    )
    return encoded_jwt


