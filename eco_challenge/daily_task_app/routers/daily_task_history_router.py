from fastapi import APIRouter
from sqlalchemy.orm import selectinload
import sqlmodel

from eco_challenge.core.database import DbSession

from eco_challenge.daily_task_app.models.daily_task_history_model import \
    DailyTaskHistoryCreate, \
    DailyTaskHistoryGet, \
    DailyTaskHistory
from eco_challenge.daily_task_app.models.daily_task_model import DailyTask, DailyTaskGet

from eco_challenge.auth import CurrentUser

router = APIRouter(prefix='/daily_task_history', tags=['DailyTaskHistory'])


@router.post('/')
async def create_task_history(
    daily_task_create: DailyTaskHistoryCreate,
    user: CurrentUser,
    session: DbSession,
) -> DailyTaskHistoryGet:
    daily_task_history = DailyTaskHistory(**daily_task_create.dict(), user_id=user.user_id)
    session.add(daily_task_history)
    await session.commit()
    await session.refresh(daily_task_history)
    return daily_task_history


@router.get('/')
async def get_task_history(session: DbSession) -> list[DailyTaskHistoryGet]:
    statement = sqlmodel.select(DailyTaskHistory).options(selectinload('*'))
    results = await session.execute(statement)
    task_history = results.scalars().all()
    return task_history


@router.delete('/{task_history_id}')
async def delete_task_history(task_history_id: int, session: DbSession):
    statement = sqlmodel.delete(DailyTaskHistory).where(DailyTaskHistory.task_history_id == task_history_id)
    await session.execute(statement)
    await session.commit()
