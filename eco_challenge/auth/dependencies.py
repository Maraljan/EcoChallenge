from typing import Annotated

import fastapi
import sqlmodel

from eco_challenge.core.models import user_model
from eco_challenge.core.database import DbSession


async def get_current_user(session: DbSession) -> user_model.User:
    """
    Get current user.
    TODO: replace this hack
    """
    statement = sqlmodel.select(user_model.User).where(user_model.User.username == 'Maral')
    response = await session.execute(statement)
    return response.scalars().first()


CurrentUser = Annotated[user_model.User, fastapi.Depends(get_current_user)]
