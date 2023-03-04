from typing import Optional

from databases import Database
from fastapi import Depends
from sqlalchemy.sql.selectable import Select
from sqlalchemy import (
    select,
)

from server.schemas.users_schemas import User, UserForAuth
from server.models.user import User as UserModel
from server.db import get_db


class UsersActions:
    """
    This class encapsulates actions related to user operations.
    """
    def __init__(self, db: Database):
        self.db = db

    async def _get_user(self, query: Select) -> Optional[User]:
        """
        Support function for getting user by some query.
        :param query: Query which should be executed.
        :return: User instance or None if doesnt exist.
        """
        if user := await self.db.fetch_one(query=query):
            return User(
                user_id=user["user_id"],
                user_email=user["email"],
                user_name=user["name"],
                user_surname=user["surname"],
                is_active=user["is_active"],
                created_at=user["created_at"],
                updated_at=user["updated_at"],
            )
        else:
            return None

    async def get_user_by_email(self, email: str) -> Optional[User]:
        """
        Retrieves a single user with the given user email.
        :param email: Email of user
        :return: User instance if exists
        """
        query = (
            select(UserModel)
            .where(UserModel.email == email)
        )

        return await self._get_user(query=query)

    async def get_user_by_email_for_auth(self, email: str) -> Optional[UserForAuth]:
        """
        Retrieves the user by the given email.
        :param email: Email of user
        :return: The password of the user, or None if the user doesn't exist
        """
        query = (
            select(UserModel)
            .where(UserModel.email == email)
            .where(UserModel.is_active)
        )
        if user := await self.db.fetch_one(query=query):
            return UserForAuth(
                user_id=user["user_id"],
                user_email=user["email"],
                hashed_password=user["password"],
                user_name=user["name"],
                user_surname=user["surname"],
                is_active=user["is_active"],
                created_at=user["created_at"],
                updated_at=user["updated_at"],
            )
        else:
            return None


def get_user_actions(db: Database = Depends(get_db)):
    """
    A dependency for working with
    User CRUD actions
    """
    return UsersActions(db=db)
