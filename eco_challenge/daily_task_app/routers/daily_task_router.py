from fastapi import APIRouter
from sqlalchemy.orm import selectinload
import sqlmodel

from eco_challenge.auth.dependencies import CurrentAdmin
from eco_challenge.core.database import DbSession
from eco_challenge.core.storages.daily_task_storage import DailyTaskStorageDepends

from eco_challenge.daily_task_app.models.daily_task_model import DailyTaskCreate, DailyTaskGet, DailyTask

router = APIRouter(prefix='/daily_task', tags=['DailyTask'])


@router.post('/')
async def create_daily_task(
    daily_task_create: DailyTaskCreate,
    storage: DailyTaskStorageDepends,
    _: CurrentAdmin,
) -> DailyTaskGet:
    return await storage.save_object(daily_task_create)


@router.get('/')
async def get_daily_tasks(storage: DailyTaskStorageDepends, _: CurrentAdmin) -> list[DailyTaskGet]:
    return await storage.get_objects()


@router.delete('/{daily_task_id}')
async def delete_daily_task(daily_task_id: int, storage: DailyTaskStorageDepends, _: CurrentAdmin):
    return await storage.delete_object(daily_task_id)
