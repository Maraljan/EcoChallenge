import fastapi
import asyncpg

from eco_challenge.auth.dependencies import CurrentAdmin
from eco_challenge.core.storages.user_storage import UserStorageDepends
from eco_challenge.core.models.user_model import UserGet, UserCreate

router = fastapi.APIRouter(prefix='/users', tags=['Users'])


@router.post('/')
async def create_user(user_create: UserCreate, storage: UserStorageDepends) -> UserGet:
    try:
        return await storage.save_object(user_create)
    except asyncpg.exceptions.UniqueViolationError:
        raise fastapi.HTTPException(status_code=fastapi.status.HTTP_409_CONFLICT, detail='this email already exists')


@router.get('/')
async def get_users(storage: UserStorageDepends, _: CurrentAdmin) -> list[UserGet]:
    return await storage.get_objects()


@router.get('/{user_id}')
async def get_user(user_id: int, storage: UserStorageDepends, _: CurrentAdmin) -> UserGet:
    return await storage.get_obj(user_id)


@router.delete('/{user_id}')
async def delete_user(user_id: int, storage: UserStorageDepends, _: CurrentAdmin):
    return await storage.delete_object(user_id)
