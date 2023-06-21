from fastapi import APIRouter

from eco_challenge.auth import CurrentUser
from eco_challenge.core.storages.daily_task_history_storage import DailyTaskHistoryStorageDepends

from eco_challenge.daily_task_app.models.daily_task_history_model import DailyTaskHistoryGet, DailyTaskHistory, \
    DailyTaskHistoryCreate

router = APIRouter(prefix='/daily_task_history', tags=['DailyTaskHistory'])


@router.post('/', response_model=DailyTaskHistoryGet)
async def create_task_history(
        daily_task_create: DailyTaskHistoryCreate,
        storage: DailyTaskHistoryStorageDepends,
        user: CurrentUser,
) -> DailyTaskHistory:
    return await storage.save_object(daily_task_create, user=user)


@router.get('/')
async def get_task_history(storage: DailyTaskHistoryStorageDepends) -> list[DailyTaskHistoryGet]:
    return await storage.get_objects()


@router.delete('/{task_history_id}')
async def delete_task_history(task_history_id: int, storage: DailyTaskHistoryStorageDepends):
    return await storage.delete_object(task_history_id)
