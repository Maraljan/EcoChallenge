from fastapi import APIRouter

from eco_challenge.auth.dependencies import CurrentAdmin
from eco_challenge.core.models.points_count_model import PointsCountGet
from eco_challenge.core.storages.points_count_storage import PointsCountStorageDepends

router = APIRouter(prefix='/points_count', tags=['PointsCount'])


@router.get('/')
async def get_points_count(storage: PointsCountStorageDepends, _: CurrentAdmin) -> list[PointsCountGet]:
    return await storage.get_objects()


@router.get('/{points_count_id}')
async def get_one_points_count(
    points_count_id: int,
    storage: PointsCountStorageDepends,
    _: CurrentAdmin,
) -> PointsCountGet:
    return await storage.get_obj(points_count_id)
