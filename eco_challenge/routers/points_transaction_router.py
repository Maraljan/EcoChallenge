from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException
from sqlmodel import select

from eco_challenge.core.database import DbSession
from eco_challenge.core.models.points_transaction_model import \
    PointsTransaction, \
    PointsTransactionGet, \
    PointsTransactionCreate

router = APIRouter(prefix='/points_transaction', tags=['PointsTransaction'])


@router.get('/')
async def get_points_transaction(session: DbSession) -> list[PointsTransactionCreate]:
    points_transaction = await session.execute(select(PointsTransaction))
    return points_transaction.scalars().all()


@router.get('/{points_transaction_id}')
async def get_one_points_transaction(points_transaction_id: int, session: DbSession) -> PointsTransactionGet:
    response = await session.execute(select(PointsTransaction).where(
        PointsTransaction.points_transaction_id == points_transaction_id)
    )
    points_transaction = response.scalars().one_or_none()
    if points_transaction is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return points_transaction
