import sqlmodel
from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException
from sqlmodel import select

from eco_challenge.core.database import DbSession
from eco_challenge.core.models.points_count_model import PointsCount
from eco_challenge.core.models.user_model import UserGet, UserCreate, User

router = APIRouter(prefix='/users', tags=['Users'])


@router.post('/')
async def create_user(user_create: UserCreate, session: DbSession) -> UserGet:
    user = User(hashed_password='bla bla bla', points_count=PointsCount(), **user_create.dict())
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return user


@router.get('/')
async def get_users(session: DbSession) -> list[UserGet]:
    users = await session.execute(select(User))
    return users.scalars().all()


@router.get('/{user_id}')
async def get_user(user_id: int, session: DbSession) -> UserGet:
    response = await session.execute(select(User).where(User.user_id == user_id))
    user = response.scalars().one_or_none()
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return user


@router.delete('/{user_id}')
async def delete_user(user_id: int, session: DbSession):
    statement = sqlmodel.delete(User).where(User.user_id == user_id)
    await session.execute(statement)
    await session.commit()
