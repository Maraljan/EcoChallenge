from fastapi import APIRouter

from eco_challenge.core.storages.user_response_storage import UserResponseStorageDepends
from eco_challenge.daily_task_app.models.user_response_model import UserResponseGet, UserResponseCreate


router = APIRouter(prefix='/user_response', tags=['UserResponse'])


@router.post('/')
async def create_user_response(
        user_response_create: UserResponseCreate,
        storage: UserResponseStorageDepends,
) -> UserResponseGet:
    return await storage.save_object(user_response_create)


@router.get('/')
async def get_user_responses(storage: UserResponseStorageDepends) -> list[UserResponseGet]:
    return await storage.get_objects()


@router.get('/{user_response_id}')
async def get_user_response(user_response_id: int, storage: UserResponseStorageDepends) -> UserResponseGet:
    return await storage.get_obj(user_response_id)


@router.delete('/{user_response_id}')
async def delete_user_response(user_response_id: int, storage: UserResponseStorageDepends) -> UserResponseGet:
    return await storage.delete_object(user_response_id)
