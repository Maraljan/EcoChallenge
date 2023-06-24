from typing import Annotated

import sqlmodel
from fastapi import Depends

from .storage import Storage
from eco_challenge.core.models import role_model


class RoleStorage(Storage[role_model.Role, role_model.RoleCreate]):
    model = role_model.Role

    async def get_by_name(self, role_name: role_model.RoleName) -> role_model.Role:
        statement = sqlmodel.select(role_model.Role).where(role_model.Role.role_name == role_name)
        response = await self.session.execute(statement)
        return response.scalar()

    def get_pk(self):
        return self.model.role_id


RoleStorageDepends = Annotated[RoleStorage, Depends(RoleStorage)]
