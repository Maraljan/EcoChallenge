from fastapi import APIRouter

from eco_challenge.auth import CurrentUser
from eco_challenge.auth.dependencies import CurrentAdmin
from eco_challenge.core.storages.user_response_storage import UserResponseStorageDepends
from eco_challenge.daily_task_app.models.user_response_model import UserResponseGet, UserResponseCreate


router = APIRouter(prefix='/user_response', tags=['UserResponse'])


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
