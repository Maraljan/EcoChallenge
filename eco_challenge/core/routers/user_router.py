import datetime
from collections import defaultdict
import fastapi
import asyncpg
import sqlmodel

from eco_challenge.auth.dependencies import CurrentAdmin
from eco_challenge.core.database import DbSession
from eco_challenge.core.models.points_transaction_model import PointsTransaction
from eco_challenge.core.storages.user_storage import UserStorageDepends
from eco_challenge.core.models.user_model import UserGet, UserCreate

router = fastapi.APIRouter(prefix='/users', tags=['Users'])


@router.post('/')
async def create_user(user_create: UserCreate, storage: UserStorageDepends) -> UserGet:
    try:
        return await storage.save_object(user_create)
    except asyncpg.exceptions.UniqueViolationError:
        raise fastapi.HTTPException(status_code=fastapi.status.HTTP_409_CONFLICT, detail='this email already exists')


@router.get('/top_users')
async def get_top_users(session: DbSession) -> list[dict]:
    statement = sqlmodel.select(PointsTransaction).where(
        PointsTransaction.create_at >= (datetime.datetime.utcnow() - datetime.timedelta(days=7)),
        PointsTransaction.points > 0,
    )
    response = await session.execute(statement)
    transactions = response.scalars().all()
    points_agg = defaultdict(int)
    for transaction in transactions:
        points_agg[transaction.user_id] += transaction.points
    top_users = sorted(points_agg.items(), key=lambda t: t[1], reverse=True)
    return [
        {
            'user_id': user_id,
            'points': points
        }
        for user_id, points in top_users
    ]


@router.get('/')
async def get_users(storage: UserStorageDepends, _: CurrentAdmin) -> list[UserGet]:
    return await storage.get_objects()


@router.get('/{user_id}')
async def get_user(user_id: int, storage: UserStorageDepends, _: CurrentAdmin) -> UserGet:
    return await storage.get_obj(user_id)


@router.delete('/{user_id}')
async def delete_user(user_id: int, storage: UserStorageDepends, _: CurrentAdmin):
    return await storage.delete_object(user_id)
