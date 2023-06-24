import fastapi
from fastapi import APIRouter

from eco_challenge.auth import CurrentUser
from eco_challenge.auth.dependencies import CurrentAdmin
from eco_challenge.core.models.points_transaction_model import PointsTransaction
from eco_challenge.core.storages.points_count_storage import PointsCountStorageDepends, PointsCountStorage
from eco_challenge.core.storages.points_transaction_storage import PointsTransactionStorageDepends
from eco_challenge.core.storages.user_response_storage import UserResponseStorageDepends
from eco_challenge.core.storages.user_storage import UserStorage
from eco_challenge.daily_task_app.models.user_response_model import (
    UserResponseGet, UserResponseCreate, ActionApprove, UserResponse,
)


router = APIRouter(prefix='/user_response', tags=['UserResponse'])


@router.post('/approve')
async def approve(
    approve_create: ActionApprove,
    storage: UserResponseStorageDepends,
    _: CurrentAdmin,
):
    user_response = await storage.get_obj(approve_create.user_response_id)
    history_task = user_response.task_history
    if history_task.is_completed is not None:
        raise fastapi.HTTPException(
            status_code=fastapi.status.HTTP_429_TOO_MANY_REQUESTS,
            detail='Action already processed',
        )
    if approve_create.is_completed:
        history_task.is_completed = True
        transaction = PointsTransaction(points=history_task.daily_task.points, user_id=history_task.user_id)
        storage.session.add(transaction)
        user_storage = UserStorage(storage.session)
        user = await user_storage.get_obj(history_task.user_id)
        point_storage = PointsCountStorage(storage.session)
        points_count = await point_storage.get_obj(user.points_count_id)
        points_count.points += transaction.points
        storage.session.add(points_count)
    else:
        history_task.is_completed = False

    storage.session.add(history_task)
    await storage.session.commit()



@router.post('/')
async def create_user_response(
    user_response_create: UserResponseCreate,
    storage: UserResponseStorageDepends,
    _: CurrentUser
) -> UserResponseGet:
    return await storage.save_object(user_response_create)


@router.get('/')
async def get_user_responses(storage: UserResponseStorageDepends, _: CurrentAdmin) -> list[UserResponseGet]:
    return await storage.get_objects()


@router.get('/{user_response_id}')
async def get_user_response(
    user_response_id: int,
    storage: UserResponseStorageDepends,
    _: CurrentAdmin
) -> UserResponseGet:
    return await storage.get_obj(user_response_id)


@router.delete('/{user_response_id}')
async def delete_user_response(
    user_response_id: int,
    storage: UserResponseStorageDepends,
    _: CurrentAdmin
) -> UserResponseGet:
    return await storage.delete_object(user_response_id)
