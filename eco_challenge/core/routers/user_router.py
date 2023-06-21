from fastapi import APIRouter

from eco_challenge.core.storages.user_storage import UserStorageDepends
from eco_challenge.core.models.user_model import UserGet, UserCreate

router = APIRouter(prefix='/users', tags=['Users'])


@router.post('/')
async def create_user(user_create: UserCreate, storage: UserStorageDepends) -> UserGet:
    return await storage.save_object(user_create)


@router.get('/')
async def get_users(storage: UserStorageDepends) -> list[UserGet]:
    return await storage.get_objects()


@router.get('/{user_id}')
async def get_user(user_id: int, storage: UserStorageDepends) -> UserGet:
    return await storage.get_obj(user_id)


@router.delete('/{user_id}')
async def delete_user(user_id: int, storage: UserStorageDepends):
    return await storage.delete_object(user_id)
