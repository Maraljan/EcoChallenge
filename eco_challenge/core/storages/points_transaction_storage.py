from typing import Annotated
from fastapi import Depends

from eco_challenge.core.models.points_transaction_model import PointsTransaction, PointsTransactionCreate
from .storage import Storage


class PointsTransactionStorage(Storage[PointsTransaction, PointsTransactionCreate]):
    model = PointsTransaction

    def get_pk(self):
        return self.model.points_transaction_id


PointsTransactionStorageDepends = Annotated[PointsTransactionStorage, Depends(PointsTransactionStorage)]
