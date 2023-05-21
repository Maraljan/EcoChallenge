from fastapi import APIRouter
from sqlalchemy.orm import selectinload
import sqlmodel

from eco_challenge.core.database import DbSession

from eco_challenge.daily_task_app.models.daily_task_model import DailyTaskCreate, DailyTaskGet, DailyTask

router = APIRouter(prefix='/daily_task', tags=['DailyTask'])


@router.post('/')
async def create_daily_task(daily_task_create: DailyTaskCreate, session: DbSession) -> DailyTaskGet:
    daily_task = DailyTask(**daily_task_create.dict())
    session.add(daily_task)
    await session.commit()
    await session.refresh(daily_task)
    return daily_task


@router.get('/')
async def get_daily_tasks(session: DbSession) -> list[DailyTaskGet]:
    statement = sqlmodel.select(DailyTask).options(selectinload('*'))
    results = await session.execute(statement)
    tasks = results.scalars().all()
    return tasks


@router.delete('/{daily_task_id}')
async def delete_daily_task(daily_task_id: int, session: DbSession):
    statement = sqlmodel.delete(DailyTask).where(DailyTask.task_id == daily_task_id)
    await session.execute(statement)
    await session.commit()
