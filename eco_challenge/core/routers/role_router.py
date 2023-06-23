from fastapi import APIRouter

from eco_challenge.auth.dependencies import CurrentAdmin
from eco_challenge.core.models.role_model import RoleCreate, RoleGet

from eco_challenge.core.storages.role_storage import RoleStorageDepends
router = APIRouter(prefix='/role', tags=['Role'])


@router.post('/')
async def create_role(role_create: RoleCreate, storage: RoleStorageDepends, _: CurrentAdmin) -> RoleGet:
    return await storage.save_object(role_create)


@router.get('/')
async def get_roles(storage: RoleStorageDepends, _: CurrentAdmin) -> list[RoleGet]:
    return await storage.get_objects()


@router.delete('/{role_id}')
async def delete_role(role_id: int, storage: RoleStorageDepends, _: CurrentAdmin):
    await storage.delete_object(role_id)
