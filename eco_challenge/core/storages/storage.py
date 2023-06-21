from typing import Generic, TypeVar, Type
from fastapi import HTTPException, status

import sqlmodel

from eco_challenge.core.database import DbSession
from eco_challenge.core.models.user_model import User

_DbModel = TypeVar('_DbModel', bound=sqlmodel.SQLModel)
_CreateModel = TypeVar('_CreateModel', bound=sqlmodel.SQLModel)


class Storage(Generic[_DbModel, _CreateModel]):

    model: Type[_DbModel] = NotImplemented
    pk = NotImplemented

    def __init__(self, session:  DbSession):
        self.session = session

    async def get_objects(self) -> list[_DbModel]:
        statement = sqlmodel.select(self.model)
        response = await self.session.execute(statement)
        return response.scalars().all()

    async def get_obj(self, pk: int) -> _DbModel:
        obj = await self.session.get(self.model, pk)
        if obj is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return obj

    async def save_object(self, create_data: _CreateModel, user: User | None = None) -> _DbModel:
        create_obj = await self._create_instance(create_data, user=user)
        self.session.add(create_obj)
        await self.session.commit()
        await self.session.refresh(create_obj)
        return create_obj

    async def _create_instance(self, create_data: _CreateModel, user: User | None = None) -> _DbModel:
        return self.model.from_orm(create_data)

    async def delete_object(self, pk: int):
        statement = sqlmodel.delete(self.model).where(self.pk == pk)
        await self.session.execute(statement)
        await self.session.commit()

