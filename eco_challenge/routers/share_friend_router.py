from fastapi import APIRouter
from sqlalchemy.orm import selectinload
import sqlmodel

from eco_challenge.core.database import DbSession

from eco_challenge.core.models.share_friends_model import ShareFriendGet, ShareFriendCreate, ShareFriend

router = APIRouter(prefix='/share_friend', tags=['ShareFriends'])


@router.post('/')
async def create_shared_friend(share_friend_create: ShareFriendCreate, session: DbSession) -> ShareFriend:
    share_friend = ShareFriend(**share_friend_create.dict())
    session.add(share_friend)
    await session.commit()
    await session.refresh(share_friend)
    return share_friend


@router.get('/')
async def get_share_friends(session: DbSession) -> list[ShareFriendGet]:
    statement = sqlmodel.select(ShareFriend).options(selectinload('*'))
    results = await session.execute(statement)
    shared_friends = results.scalars().all()
    return shared_friends


@router.delete('/{share_friend_id}')
async def delete_share_friend(share_friend_id: int, session: DbSession):
    statement = sqlmodel.delete(ShareFriend).where(ShareFriend.share_friend_id == share_friend_id)
    await session.execute(statement)
    await session.commit()
