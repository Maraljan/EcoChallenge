from typing import Annotated

import sqlmodel
from fastapi import Depends

from eco_challenge.core.models.user_model import User, UserCreate
from eco_challenge.core.models.points_count_model import PointsCount
from .role_storage import RoleStorageDepends

from .storage import Storage
from eco_challenge.auth import authservice
from ..models.role_model import RoleName


class UserStorage(Storage[User, UserCreate]):

    model = User

    async def _create_instance(self, create_data: UserCreate, user: User | None = None) -> User:
        role_storage = RoleStorageDepends(self.session)
        user_role = await role_storage.get_by_name(RoleName.USER)
        points_count = PointsCount()
        self.session.add(points_count)
        user = User(
            role_id=user_role.role_id,
            hashed_password=authservice.AUTH_SERVICE.hash_password(create_data.password),
            points_count=points_count,
            **create_data.dict(),
        )
        return user

    async def get_by_email(self, email: str) -> User | None:
        statement = sqlmodel.select(User).where(User.email == email)
        response = await self.session.execute(statement)
        return response.scalar_one_or_none()

    def get_pk(self):
        return self.model.user_id


UserStorageDepends = Annotated[UserStorage, Depends(UserStorage)]










