from typing import Annotated

import fastapi

from eco_challenge.auth import authservice
from eco_challenge.auth.jwt import JwtToken
from eco_challenge.core.database import DbSession
from eco_challenge.core.models.role_model import RoleName
from eco_challenge.core.models.user_model import User
from eco_challenge.core.storages import user_storage


async def auth_user_by_token(session: DbSession, token: JwtToken):
    storage = user_storage.UserStorage(session)
    user = await storage.get_by_email(token.email)

    if user is None:
        raise fastapi.HTTPException(
            status_code=fastapi.status.HTTP_401_UNAUTHORIZED,
            detail='Authorized user could not be found',
        )

    return user


async def get_current_user(
    session: DbSession,
    access_raw_token: str = fastapi.Depends(authservice.AUTH_SERVICE.oauth_scheme),
) -> User:
    token = JwtToken.decode(access_raw_token)
    return await auth_user_by_token(session, token)

CurrentUser = Annotated[User, fastapi.Depends(get_current_user)]


async def get_current_admin(user: CurrentUser) -> User:
    if user.user_role.role_name != RoleName.ADMIN:
        raise fastapi.HTTPException(status_code=fastapi.status.HTTP_403_FORBIDDEN)
    return user


CurrentAdmin = Annotated[User, fastapi.Depends(get_current_admin)]
