from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException
from sqlmodel import select

from eco_challenge.core.database import DbSession
from eco_challenge.core.models.points_count_model import PointsCount, PointsCountGet

router = APIRouter(prefix='/points_count', tags=['PointsCount'])


@router.get('/')
async def get_points_count(session: DbSession) -> list[PointsCountGet]:
    points_count = await session.execute(select(PointsCount))
    return points_count.scalars().all()


@router.get('/{points_count_id}')
async def get_one_points_count(points_count_id: int, session: DbSession) -> PointsCountGet:
    response = await session.execute(select(PointsCount).where(PointsCount.points_count_id == points_count_id))
    points_count = response.scalars().one_or_none()
    if points_count is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return points_count
