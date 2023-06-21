from typing import Annotated
from fastapi import Depends


from eco_challenge.core.models.user_model import User, UserCreate
from .storage import Storage
from ..models.points_count_model import PointsCount


class UserStorage(Storage[User, UserCreate]):
    model = User

    async def _create_instance(self, create_data: UserCreate, user: User | None = None) -> User:
        user = User(hashed_password='bla bla bla', points_count=PointsCount(), **create_data.dict())
        return user


UserStorageDepends = Annotated[UserStorage, Depends(UserStorage)]










