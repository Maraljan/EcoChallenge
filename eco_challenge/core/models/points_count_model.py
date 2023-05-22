import typing
from typing import Annotated

from pydantic import conint


from sqlmodel import SQLModel, Field, Relationship
if typing.TYPE_CHECKING:
    from .user_model import User


class PointsCountCreate(SQLModel):
    points: Annotated[int, conint(ge=0)] = 0


class PointsCountGet(PointsCountCreate):
    points_count_id: int | None = Field(default=None, primary_key=True)


class PointsCount(PointsCountCreate, table=True):
    __tablename__ = 'points_count'
    points_count_id: int | None = Field(default=None, primary_key=True)
    user: 'User' = Relationship(back_populates='points_count', sa_relationship_kwargs={'uselist': False})
