from typing import Annotated
from fastapi import Depends

from eco_challenge.core.models.points_count_model import PointsCountCreate, PointsCount
from .storage import Storage


class PointsCountStorage(Storage[PointsCount, PointsCountCreate]):
    model = PointsCount


PointsCountStorageDepends = Annotated[PointsCountStorage, Depends(PointsCountStorage)]






