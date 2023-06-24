from typing import Annotated

import sqlmodel
from fastapi import Depends
from sqlalchemy import func

from eco_challenge.daily_task_app.models.daily_task_model import DailyTask, DailyTaskCreate, DailyTaskGet
from .storage import Storage


class DailyTaskStorage(Storage[DailyTask, DailyTaskCreate]):
    model = DailyTask

    def get_pk(self):
        return self.model.task_id

    async def get_random_daily_tasks(self, limit: int) -> list[DailyTask]:
        statement = sqlmodel.select(DailyTask).order_by(func.random()).limit(limit)
        response = await self.session.execute(statement)
        return response.scalars().all()


DailyTaskStorageDepends = Annotated[DailyTaskStorage, Depends(DailyTaskStorage)]
