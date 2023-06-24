from fastapi import APIRouter

from eco_challenge.auth.dependencies import CurrentAdmin
from eco_challenge.core.models.points_transaction_model import PointsTransactionGet
from eco_challenge.core.storages.points_transaction_storage import PointsTransactionStorageDepends

router = APIRouter(prefix='/points_transaction', tags=['PointsTransaction'])


@router.get('/')
async def get_points_transaction(
    storage: PointsTransactionStorageDepends,
    _: CurrentAdmin
) -> list[PointsTransactionGet]:
    return await storage.get_objects()


@router.get('/{points_transaction_id}')
async def get_one_points_transaction(
    points_transaction_id: int,
    storage: PointsTransactionStorageDepends,
    _: CurrentAdmin
):
    return await storage.get_obj(points_transaction_id)
