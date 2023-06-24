from typing import Annotated
from fastapi import Depends

from eco_challenge.daily_task_app.models.daily_task_history_model import DailyTaskHistory, DailyTaskHistoryCreate
from .storage import Storage
from ..models.user_model import User


class DailyTaskHistoryStorage(Storage[DailyTaskHistory, DailyTaskHistoryCreate]):
    model = DailyTaskHistory

    def get_pk(self):
        return self.model.task_history_id

    async def _create_instance(self, create_data: DailyTaskHistoryCreate, user: User | None = None) -> DailyTaskHistory:
        daily_task_history = DailyTaskHistory(**create_data.dict(), user_id=user.user_id)
        return daily_task_history


DailyTaskHistoryStorageDepends = Annotated[DailyTaskHistoryStorage, Depends(DailyTaskHistoryStorage)]

