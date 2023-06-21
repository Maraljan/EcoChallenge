from typing import Annotated
from fastapi import Depends

from eco_challenge.daily_task_app.models.daily_task_model import DailyTask, DailyTaskCreate
from .storage import Storage


class DailyTaskStorage(Storage[DailyTask, DailyTaskCreate]):
    model = DailyTask


DailyTaskStorageDepends = Annotated[DailyTaskStorage, Depends(DailyTaskStorage)]
