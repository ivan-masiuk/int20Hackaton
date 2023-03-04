from datetime import timedelta

from fastapi import (
    Depends,
    HTTPException,
    status
)

from server.settings import settings
from server.schemas.auth_scemas import (
    Token,
    SignInRequest
)
from server.services.auth import (
    authenticate_user, create_access_token
)
from server.services.user_actions import (
    UsersActions,
    get_user_actions
)


async def login_for_access_token(
    data: SignInRequest,
    user_actions: UsersActions = Depends(get_user_actions)
) -> Token:
    """
    Endpoint to get an access token for a user.
    :param data: The sign-in request data containing email and password.
    :param user_actions: The actions object to use to interact with the user data.
    :return: The result object containing the token and a success message.
    """
    user = await authenticate_user(
        email=data.user_email,
        password=data.user_password,
        user_actions=user_actions,
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )
    access_token_expires = timedelta(
        minutes=settings.access_token_expire_minutes
    )
    access_token = create_access_token(
        data={"email": user.user_email},
        expires_delta=access_token_expires,
    )

    return Token(
        access_token=access_token,
        token_type="Bearer"
    )

