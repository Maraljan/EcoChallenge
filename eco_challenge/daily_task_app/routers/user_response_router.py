from fastapi import APIRouter, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import selectinload
import sqlmodel
from starlette import status

from eco_challenge.core.database import DbSession

from eco_challenge.daily_task_app.models.user_response_model import \
    UserResponse, \
    UserResponseGet, \
    UserResponseCreate


router = APIRouter(prefix='/user_response', tags=['UserResponse'])


@router.post('/')
async def create_user_response(daily_task_create: UserResponseCreate, session: DbSession) -> UserResponseGet:
    user_response = UserResponse(**daily_task_create.dict())
    session.add(user_response)
    await session.commit()
    await session.refresh(user_response)
    return user_response


@router.get('/{user_response_id}')
async def get_user_response(user_response_id: int, session: DbSession) -> UserResponseGet:
    # statement = sqlmodel.select(UserResponse).options(selectinload('*'))
    # results = await session.execute(statement)
    # user_response = results.scalars().all()
    # return user_response

    response = await session.execute(select(UserResponse).where(UserResponse.user_response_id == user_response_id))
    user_response = response.scalars().one_or_none()
    if user_response is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return user_response


@router.delete('/{user_response_id}')
async def delete_user_response(user_response_id: int, session: DbSession):
    statement = sqlmodel.delete(UserResponse).where(UserResponse.user_response_id == user_response_id)
    await session.execute(statement)
    await session.commit()
